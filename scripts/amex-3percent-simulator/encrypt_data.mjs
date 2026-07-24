#!/usr/bin/env node
/**
 * scripts/amex-3percent-simulator/data.plain.json（平文）
 *   → docs/amex-3percent-simulator/data.json（暗号文）を生成するビルドスクリプト
 *
 * 目的（2026-07 セキュリティ修正）:
 *   店舗検索機能（PRO）は「知られていないURL」ではなく、実際のクライアント側
 *   暗号化で保護する。data.json には AES-256-GCM の暗号文のみを書き出し、
 *   平文の店舗リストは docs/ 配下（GitHub Pagesの公開ルート）に一切置かない。
 *
 * 暗号方式:
 *   鍵導出: PBKDF2-SHA256, iterations=210000, salt=乱数16byte
 *   暗号化: AES-256-GCM, iv=乱数12byte（Web Crypto API準拠。認証タグは
 *           暗号文の末尾に自動付加される＝ブラウザ側の crypto.subtle.decrypt
 *           とそのまま整合する）
 *
 * トークンの扱い（重要）:
 *   --token を指定しない場合は新しいランダムトークンを生成して標準出力に
 *   表示するだけで、このスクリプト自身はトークンをどのファイルにも書き込まない。
 *   購入者向けの最終アクセスURL（?k=<token>）は note記事側のリンクとして
 *   運営者が手動で管理する（このリポジトリには平文トークンを絶対にコミットしない）。
 *
 * 使い方:
 *   node scripts/amex-3percent-simulator/encrypt_data.mjs --token <トークン>
 *   node scripts/amex-3percent-simulator/encrypt_data.mjs            # トークンを新規生成
 *
 * オプション:
 *   --in   平文JSONの入力パス（既定: scripts/amex-3percent-simulator/data.plain.json）
 *   --out  暗号文JSONの出力パス（既定: docs/amex-3percent-simulator/data.json）
 */
import { webcrypto } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const { subtle } = webcrypto;
const __dirname = path.dirname(fileURLToPath(import.meta.url));

const PBKDF2_ITERATIONS = 210000;

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    if (argv[i].startsWith('--')) {
      const key = argv[i].slice(2);
      const hasVal = argv[i + 1] !== undefined && !argv[i + 1].startsWith('--');
      out[key] = hasVal ? argv[++i] : true;
    }
  }
  return out;
}

function bytesToHex(bytes) {
  return Buffer.from(bytes).toString('hex');
}

function randomBytes(len) {
  const b = new Uint8Array(len);
  webcrypto.getRandomValues(b);
  return b;
}

async function deriveEncryptKey(token, saltBytes) {
  const keyMaterial = await subtle.importKey(
    'raw',
    new TextEncoder().encode(token),
    'PBKDF2',
    false,
    ['deriveKey']
  );
  return subtle.deriveKey(
    { name: 'PBKDF2', salt: saltBytes, iterations: PBKDF2_ITERATIONS, hash: 'SHA-256' },
    keyMaterial,
    { name: 'AES-GCM', length: 256 },
    false,
    ['encrypt']
  );
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const inPath = path.resolve(__dirname, args.in || 'data.plain.json');
  const outPath = path.resolve(__dirname, args.out || '../../docs/amex-3percent-simulator/data.json');

  let token = typeof args.token === 'string' ? args.token : null;
  let generated = false;
  if (!token) {
    token = bytesToHex(randomBytes(24)); // 48桁の16進アクセストークン
    generated = true;
  }

  const plaintext = readFileSync(inPath, 'utf-8');
  // 入力がJSONとして妥当か検証（壊れたデータを暗号化しないため）
  JSON.parse(plaintext);

  const saltBytes = randomBytes(16);
  const ivBytes = randomBytes(12);

  const key = await deriveEncryptKey(token, saltBytes);
  const ctBuf = await subtle.encrypt(
    { name: 'AES-GCM', iv: ivBytes },
    key,
    new TextEncoder().encode(plaintext)
  );

  const payload = {
    v: 1,
    kdf: 'PBKDF2-SHA256',
    iterations: PBKDF2_ITERATIONS,
    salt: bytesToHex(saltBytes),
    iv: bytesToHex(ivBytes),
    ct: bytesToHex(new Uint8Array(ctBuf)),
  };

  writeFileSync(outPath, JSON.stringify(payload));

  console.log(`Encrypted ${inPath}`);
  console.log(`      -> ${outPath}`);
  if (generated) {
    console.log('');
    console.log('新しいアクセストークンを生成しました（このトークンはどこにもコミットされていません）:');
    console.log(`  ${token}`);
    console.log('');
    console.log('購入者向け最終アクセスURL（note記事側のリンクをこの値で更新すること）:');
    console.log(`  https://diceman-hub.github.io/ino-moneycoach/amex-3percent-simulator/simulator-55292a97.html?k=${token}`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
