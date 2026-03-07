#!/usr/bin/env python3
"""
ニュースレター フォルダ構造改善スクリプト

既存のアーカイブフォルダに以下を追加：
1. 各号フォルダにREADME.mdを作成
2. セクションファイルをsections/フォルダに整理
3. 全号インデックスファイルを作成

使用方法:
    python newsletter_enhance_structure.py --dry-run
    python newsletter_enhance_structure.py
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import re

# 設定
NEWSLETTER_DIR = Path("/Users/mba2024/Documents/Obsidian/Dai DB/03_NewsLetter")
ARCHIVE_DIR = NEWSLETTER_DIR / "_archive"

# 既知のボリューム情報
VOLUME_INFO = {
    "01": {
        "date": "2025-12-05",
        "title": "創刊号",
        "theme": "旅とお金を最適化する週刊レター、はじまります",
        "main_content": ["創刊号", "ビジネスゴールド特集"],
    },
    "02": {
        "date": "2025-12-13",
        "title": "第2号",
        "theme": "🎊 3周年記念：感謝を込めて特別ギフトをお届けします",
        "main_content": ["3周年記念", "ANAマイル×スターアライアンス攻略術"],
    },
    "03": {
        "date": "2025-12-20",
        "title": "第3号",
        "theme": "ANA新ルール完全解説＆年末やり残しチェックリスト",
        "main_content": ["ANA 2027年度ステイタス条件", "年末年始の決済最適化"],
    },
    "04": {
        "date": "2025-12-27",
        "title": "第4号",
        "theme": "年末決済最適化＆2026年Apple完全攻略ガイド",
        "main_content": ["Apple完全攻略ガイド", "金沢でグローバリスト達成"],
    },
}


def extract_sections_from_markdown(file_path: Path) -> List[str]:
    """Markdownファイルからセクションを抽出"""
    sections = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            # ## で始まる見出しを抽出
            for line in content.split("\n"):
                if line.startswith("## "):
                    section = line.replace("## ", "").strip()
                    # 絵文字や番号を除去
                    section = re.sub(r"^[\d\s📝📰🎯🧳✏️🎉📝🎁]+", "", section)
                    if section and len(section) < 100:  # 長すぎるものは除外
                        sections.append(section)
    except Exception as e:
        print(f"  警告: {file_path.name}の読み込みエラー - {str(e)}")
    
    return sections[:10]  # 最大10個まで


def create_readme(volume_dir: Path, info: Dict) -> str:
    """README.mdの内容を生成"""
    volume = volume_dir.name.split("_")[0].replace("Vol", "")
    year = volume_dir.parent.name
    
    # メインファイルを検索
    main_md = None
    main_html = None
    section_files = []
    asset_files = []
    
    for file_path in volume_dir.iterdir():
        if file_path.is_file():
            if file_path.name.endswith("_全体版_v2.md") or (file_path.name.endswith(".md") and "ドラフト" not in file_path.name and "section" not in file_path.name):
                if main_md is None:
                    main_md = file_path.name
            elif file_path.name.endswith(".html") and "section" not in file_path.name:
                if main_html is None:
                    main_html = file_path.name
            elif "section" in file_path.name:
                section_files.append(file_path.name)
            elif file_path.name.endswith((".xlsx", ".xls", ".csv")):
                asset_files.append(file_path.name)
    
    # セクションを抽出
    sections = []
    if main_md:
        main_file = volume_dir / main_md
        if main_file.exists():
            sections = extract_sections_from_markdown(main_file)
    
    readme_content = f"""# ニュースレター Vol.{volume} {info['title']}

**配信日**: {info['date']}  
**テーマ**: {info['theme']}

---

## 📋 目次

"""
    
    # セクションを追加
    for i, section in enumerate(sections, 1):
        readme_content += f"{i}. {section}\n"
    
    if not sections:
        readme_content += "1. 📝 今週のまとめ\n"
        readme_content += "2. 📰 今週の注目ニュース\n"
        readme_content += "3. 🧳 いのとぴよたのドタバタ旅行の舞台裏\n"
        readme_content += "4. ✏️ 編集後記\n"
    
    readme_content += f"""
---

## 📁 ファイル構成

"""
    
    if main_md:
        readme_content += f"- **メインファイル**: `{main_md}`\n"
    if main_html:
        readme_content += f"- **HTML版**: `{main_html}`\n"
    
    if section_files:
        readme_content += f"- **セクションファイル**: {len(section_files)}個\n"
    if asset_files:
        readme_content += f"- **関連ファイル**: {len(asset_files)}個\n"
    
    readme_content += f"""
---

## 🏷️ タグ

#newsletter #vol{volume.zfill(2)} #{info['title'].replace('第', '').replace('号', '')}

---

## 🔗 関連リンク

"""
    
    # 前後の号へのリンク
    vol_num = int(volume)
    if vol_num > 1:
        prev_vol = f"Vol{(vol_num-1):02d}"
        readme_content += f"- [[{prev_vol}_*]]\n"
    if vol_num < 4:  # 現在は4号まで
        next_vol = f"Vol{(vol_num+1):02d}"
        readme_content += f"- [[{next_vol}_*]]\n"
    
    readme_content += f"""
---

## 📝 主要コンテンツ

"""
    
    for content in info.get('main_content', []):
        readme_content += f"- {content}\n"
    
    return readme_content


def organize_sections(volume_dir: Path, dry_run: bool = False) -> int:
    """セクションファイルをsections/フォルダに整理"""
    sections_dir = volume_dir / "sections"
    moved_count = 0
    
    section_files = [f for f in volume_dir.iterdir() if f.is_file() and "section" in f.name.lower()]
    
    if not section_files:
        return 0
    
    if not dry_run:
        sections_dir.mkdir(exist_ok=True)
    
    for file_path in section_files:
        if not dry_run:
            try:
                dest = sections_dir / file_path.name
                if not dest.exists():
                    shutil.move(str(file_path), str(dest))
                    moved_count += 1
            except Exception as e:
                print(f"  エラー: {file_path.name}の移動に失敗 - {str(e)}")
    
    return moved_count


def create_index(dry_run: bool = False) -> str:
    """全号インデックスファイルを作成"""
    index_content = """# ニュースレター アーカイブ インデックス

このファイルは、すべてのニュースレターの概要を一覧化しています。

---

"""
    
    for year_dir in sorted(ARCHIVE_DIR.iterdir()):
        if not year_dir.is_dir() or year_dir.name.startswith("_"):
            continue
        
        year = year_dir.name
        index_content += f"## {year}年\n\n"
        
        for volume_dir in sorted(year_dir.iterdir()):
            if not volume_dir.is_dir():
                continue
            
            volume = volume_dir.name.split("_")[0].replace("Vol", "")
            if volume in VOLUME_INFO:
                info = VOLUME_INFO[volume]
                index_content += f"### Vol.{volume} {info['title']}\n"
                index_content += f"- **配信日**: {info['date']}\n"
                index_content += f"- **テーマ**: {info['theme']}\n"
                index_content += f"- **主要コンテンツ**: {', '.join(info.get('main_content', []))}\n"
                index_content += f"- **リンク**: [[{volume_dir.name}/README]]\n\n"
    
    if not dry_run:
        index_file = ARCHIVE_DIR / "INDEX.md"
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(index_content)
    
    return index_content


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="ニュースレター フォルダ構造改善スクリプト",
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="ドライラン（実際には変更しない）",
    )
    
    args = parser.parse_args()
    
    if not ARCHIVE_DIR.exists():
        print("エラー: アーカイブフォルダが見つかりません。")
        return
    
    print("\n📋 フォルダ構造改善計画:")
    print("=" * 60)
    
    total_readmes = 0
    total_sections = 0
    
    # 各号フォルダを処理
    for year_dir in sorted(ARCHIVE_DIR.iterdir()):
        if not year_dir.is_dir() or year_dir.name.startswith("_"):
            continue
        
        year = year_dir.name
        print(f"\n📁 {year}年")
        
        for volume_dir in sorted(year_dir.iterdir()):
            if not volume_dir.is_dir():
                continue
            
            volume = volume_dir.name.split("_")[0].replace("Vol", "")
            if volume not in VOLUME_INFO:
                continue
            
            info = VOLUME_INFO[volume]
            print(f"\n  📦 {volume_dir.name}")
            
            # README.mdを作成
            readme_file = volume_dir / "README.md"
            if readme_file.exists() and not args.dry_run:
                print(f"    ⚠️  README.mdは既に存在します（スキップ）")
            else:
                readme_content = create_readme(volume_dir, info)
                if not args.dry_run:
                    with open(readme_file, "w", encoding="utf-8") as f:
                        f.write(readme_content)
                print(f"    ✅ README.mdを作成")
                total_readmes += 1
            
            # セクションファイルを整理
            moved = organize_sections(volume_dir, dry_run=args.dry_run)
            if moved > 0:
                print(f"    ✅ {moved}個のセクションファイルをsections/フォルダに移動")
                total_sections += moved
    
    # インデックスファイルを作成
    print(f"\n📑 全号インデックスファイルを作成")
    index_content = create_index(dry_run=args.dry_run)
    if not args.dry_run:
        print(f"    ✅ INDEX.mdを作成")
    
    print("=" * 60)
    
    if args.dry_run:
        print("\n[DRY RUN] 実際には変更しません。")
    else:
        print(f"\n✅ 改善完了:")
        print(f"   - {total_readmes}個のREADME.mdを作成")
        print(f"   - {total_sections}個のセクションファイルを整理")
        print(f"   - INDEX.mdを作成")


if __name__ == "__main__":
    main()

