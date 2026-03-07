#!/usr/bin/env python3
"""
既存ファイル整理スクリプト

Vol.01-04の既存ファイルを整理し、アーカイブフォルダに移動します。
一度だけ実行することを想定しています。

使用方法:
    python newsletter_organize_existing.py --dry-run
    python newsletter_organize_existing.py
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

# 設定
NEWSLETTER_DIR = Path("/Users/mba2024/Documents/Obsidian/Dai DB/03_NewsLetter")
ARCHIVE_DIR = NEWSLETTER_DIR / "_archive"
LOG_FILE = ARCHIVE_DIR / ".organize_log.txt"

# 既知のボリューム情報
KNOWN_VOLUMES = {
    "01": {
        "date": "2025-12-05",
        "title": "創刊号",
        "files": [
            "2025_12_05_Vol01_いのマネーニュースレター_創刊号.html",
            "2025_12_05_Vol01_いのマネーニュースレター_創刊号.md",
        ],
    },
    "02": {
        "date": "2025-12-13",
        "title": "第2号",
        "files": [
            "2025_12_13_Vol02_いのマネーニュースレター.html",
            "2025_12_13_Vol02_いのマネーニュースレター_全体版_v1.md",
            "2025_12_13_Vol02_いのマネーニュースレター_全体版_v2.md",
            "2025_12_13_Vol02_gift_amex_offer_guide.html",
            "2025_12_13_Vol02_section_3rd_anniversary_UPDATED.md",
            "2025_12_13_Vol02_section_3rd_anniversary.md",
            "2025_12_13_Vol02_section_ana_star_alliance.md",
            "2025_12_13_Vol02_section_store_list.md",
            "2025_12_13_Vol02_訂正メール.html",
        ],
    },
    "03": {
        "date": "2025-12-20",
        "title": "第3号",
        "files": [
            "2025_12_20_Vol03_いのマネーニュースレター.html",
            "2025_12_20_Vol03_いのマネーニュースレター_ドラフト.md",
        ],
    },
    "04": {
        "date": "2025-12-27",
        "title": "第4号",
        "files": [
            "2025_12_27_Vol04_いのマネーニュースレター.html",
            "2025_12_27_Vol04_いのマネーニュースレター_ドラフト.md",
        ],
    },
}

# 関連ファイル（ボリューム番号で検索）
RELATED_PATTERNS = [
    "campaign_list_2025_12",
    "news_summary_2025",
    "金融機関ニュース_キャンペーン情報_202512",
]


def log(message: str):
    """ログを記録"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}\n"
    
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_message)
    
    print(f"  {message}")


def organize_existing_files(dry_run: bool = False):
    """既存ファイルを整理"""
    moved_files: List[Tuple[Path, Path]] = []
    errors: List[str] = []
    
    # アーカイブフォルダを作成
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n📋 既存ファイル整理計画:")
    print("=" * 60)
    
    # 各ボリュームを処理
    for volume, info in KNOWN_VOLUMES.items():
        year = "2025"
        title = info["title"]
        archive_folder = ARCHIVE_DIR / year / f"Vol{volume}_{title}"
        
        print(f"\n📁 {year}年 Vol.{volume} {title}")
        print(f"   移動先: {archive_folder.relative_to(NEWSLETTER_DIR)}")
        
        # 既知のファイルを移動
        for filename in info["files"]:
            file_path = NEWSLETTER_DIR / filename
            
            if not file_path.exists():
                log(f"ファイルが見つかりません: {filename}")
                continue
            
            archive_path = archive_folder / filename
            
            print(f"   - {filename}")
            print(f"     → {archive_path.relative_to(NEWSLETTER_DIR)}")
            
            if not dry_run:
                try:
                    archive_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    if archive_path.exists():
                        log(f"スキップ（既に存在）: {filename}")
                        continue
                    
                    shutil.move(str(file_path), str(archive_path))
                    moved_files.append((file_path, archive_path))
                    log(f"移動完了: {filename}")
                    
                except Exception as e:
                    error_msg = f"エラー: {filename} - {str(e)}"
                    errors.append(error_msg)
                    log(error_msg)
        
        # 関連ファイルを検索
        related_files = []
        for pattern in RELATED_PATTERNS:
            for file_path in NEWSLETTER_DIR.glob(f"{pattern}*"):
                if file_path.is_file():
                    related_files.append(file_path)
        
        if related_files:
            print(f"   - 関連ファイル ({len(related_files)}個):")
            for file_path in related_files:
                archive_path = archive_folder / file_path.name
                print(f"     - {file_path.name}")
                print(f"       → {archive_path.relative_to(NEWSLETTER_DIR)}")
                
                if not dry_run:
                    try:
                        archive_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        if archive_path.exists():
                            log(f"スキップ（既に存在）: {file_path.name}")
                            continue
                        
                        shutil.move(str(file_path), str(archive_path))
                        moved_files.append((file_path, archive_path))
                        log(f"移動完了: {file_path.name}")
                        
                    except Exception as e:
                        error_msg = f"エラー: {file_path.name} - {str(e)}"
                        errors.append(error_msg)
                        log(error_msg)
    
    print("=" * 60)
    
    if dry_run:
        print("\n[DRY RUN] 実際には移動しません。")
        return
    
    # 結果を表示
    print(f"\n✅ 整理完了: {len(moved_files)}個のファイルを移動しました。")
    
    if errors:
        print(f"\n⚠️  エラー: {len(errors)}個のエラーが発生しました。")
        for error in errors:
            print(f"   - {error}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="既存ファイル整理スクリプト（Vol.01-04）",
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="ドライラン（実際には移動しない）",
    )
    
    args = parser.parse_args()
    
    # 確認
    if not args.dry_run:
        print("\n⚠️  このスクリプトは既存ファイル（Vol.01-04）を整理します。")
        response = input("実行しますか？ (yes/no): ").strip().lower()
        if response not in ["yes", "y"]:
            print("キャンセルしました。")
            return
    
    organize_existing_files(dry_run=args.dry_run)


if __name__ == "__main__":
    main()

