#!/usr/bin/env python3
"""
ニュースレター ファイル整理スクリプト

配信後のファイルを自動的に整理し、アーカイブフォルダに移動します。
実行前に確認プロセスを含み、安全にファイルを整理できます。

使用方法:
    python newsletter_organize.py --volume 04 --date 2025-12-27
    python newsletter_organize.py --auto
    python newsletter_organize.py --list
"""

import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import json

# 設定
NEWSLETTER_DIR = Path("/Users/mba2024/Documents/Obsidian/Dai DB/03_NewsLetter")
ARCHIVE_DIR = NEWSLETTER_DIR / "_archive"
WORKING_DIR = NEWSLETTER_DIR / "_working"
TEMPLATE_DIR = NEWSLETTER_DIR / "_template"
LOG_FILE = ARCHIVE_DIR / ".organize_log.txt"

# 移動しないファイル・フォルダ
EXCLUDE_PATTERNS = [
    "_template",
    "_archive",
    "_working",
    "README",
    ".git",
    ".DS_Store",
]


class NewsletterOrganizer:
    """ニュースレター ファイル整理クラス"""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.moved_files: List[Tuple[Path, Path]] = []
        self.errors: List[str] = []

    def log(self, message: str):
        """ログを記録"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}\n"
        
        if not self.dry_run:
            LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(log_message)
        
        print(f"  {message}")

    def should_exclude(self, path: Path) -> bool:
        """ファイルを除外すべきかチェック"""
        # ディレクトリ名でチェック
        for part in path.parts:
            if any(pattern in part for pattern in EXCLUDE_PATTERNS):
                return True
        
        # READMEファイルは除外
        if path.name.startswith("README"):
            return True
        
        return False

    def parse_volume_info(self, filename: str) -> Dict[str, str]:
        """ファイル名からボリューム情報を抽出"""
        # 例: 2025_12_27_Vol04_いのマネーニュースレター.html
        parts = filename.split("_")
        
        if len(parts) < 4 or not parts[3].startswith("Vol"):
            return {}
        
        year = parts[0]
        month = parts[1]
        day = parts[2]
        volume = parts[3].replace("Vol", "")
        
        # 号タイトルを抽出（Vol04以降の部分）
        title_parts = parts[4:] if len(parts) > 4 else []
        title = "_".join(title_parts).replace(".html", "").replace(".md", "")
        
        return {
            "year": year,
            "month": month,
            "day": day,
            "volume": volume.zfill(2),  # 01, 02, 03形式
            "title": title,
            "date": f"{year}-{month}-{day}",
        }

    def find_newsletter_files(self, volume: str = None, date: str = None) -> List[Path]:
        """ニュースレターファイルを検索（ルートのみ）"""
        files = []
        
        for file_path in NEWSLETTER_DIR.iterdir():
            if not file_path.is_file():
                continue
            
            if self.should_exclude(file_path):
                continue
            
            # ボリューム情報を抽出
            info = self.parse_volume_info(file_path.name)
            
            if not info:
                continue
            
            # フィルタリング
            if volume and info["volume"] != volume.zfill(2):
                continue
            
            if date and info["date"] != date:
                continue
            
            files.append(file_path)
        
        return files

    def find_working_files(self, volume: str, date: str) -> List[Path]:
        """_working 内の該当号関連ファイルを検索（配信後アーカイブ用）"""
        if not WORKING_DIR.exists():
            return []
        vol_str = volume.zfill(2)
        pattern_upper = f"Vol{vol_str}"
        pattern_lower = f"vol{vol_str}"
        files = []
        for file_path in WORKING_DIR.iterdir():
            if not file_path.is_file():
                continue
            name = file_path.name
            if pattern_upper in name or pattern_lower in name:
                files.append(file_path)
        return files

    def get_archive_path(self, file_path: Path, info: Dict[str, str]) -> Path:
        """アーカイブ先のパスを取得"""
        year = info["year"]
        volume = info["volume"]
        title = info["title"] or f"第{volume}号"
        
        archive_folder = ARCHIVE_DIR / year / f"Vol{volume}_{title}"
        return archive_folder / file_path.name

    def organize_files(
        self,
        files: List[Path],
        confirm: bool = True,
        optional_infos: Optional[Dict[Path, Dict[str, str]]] = None,
    ) -> bool:
        """ファイルを整理（ルート＋_working の該当号をアーカイブに移動）"""
        if not files:
            print("整理するファイルが見つかりませんでした。")
            return False
        
        optional_infos = optional_infos or {}
        # ファイルをグループ化（ボリュームごと）
        file_groups: Dict[str, List[Path]] = {}
        for file_path in files:
            info = optional_infos.get(file_path) or self.parse_volume_info(file_path.name)
            if not info:
                continue
            
            key = f"{info['year']}_Vol{info['volume']}"
            if key not in file_groups:
                file_groups[key] = []
            file_groups[key].append(file_path)
        
        # 移動計画を表示
        print("\n📋 移動計画:")
        print("=" * 60)
        
        for key, group_files in file_groups.items():
            info = self.parse_volume_info(group_files[0].name) or (optional_infos or {}).get(group_files[0])
            year = info["year"]
            volume = info["volume"]
            # フォルダ名は「第X号」に統一（optional_infos で渡された canonical を優先）
            title = info["title"] or f"第{int(volume)}号"
            if optional_infos:
                for fp in group_files:
                    if fp in optional_infos and optional_infos[fp].get("title", "").startswith("第") and "号" in optional_infos[fp].get("title", ""):
                        title = optional_infos[fp]["title"]
                        break
            archive_folder = ARCHIVE_DIR / year / f"Vol{volume}_{title}"
            resolved_info = {**info, "title": title}
            
            print(f"\n📁 {year}年 Vol.{volume} {title}")
            print(f"   移動先: {archive_folder.relative_to(NEWSLETTER_DIR)}")
            print(f"   ファイル数: {len(group_files)}")
            
            for file_path in group_files:
                archive_path = self.get_archive_path(file_path, resolved_info)
                print(f"   - {file_path.name}")
                print(f"     → {archive_path.relative_to(NEWSLETTER_DIR)}")
        
        print("=" * 60)
        
        # 確認
        if confirm:
            response = input("\nこの計画で実行しますか？ (yes/no): ").strip().lower()
            if response not in ["yes", "y"]:
                print("キャンセルしました。")
                return False
        
        # 実行
        if self.dry_run:
            print("\n[DRY RUN] 実際には移動しません。")
            return True
        
        # ファイルを移動
        for key, group_files in file_groups.items():
            info = self.parse_volume_info(group_files[0].name) or (optional_infos or {}).get(group_files[0])
            volume = info["volume"]
            year = info["year"]
            title = info["title"] or f"第{int(volume)}号"
            if optional_infos:
                for fp in group_files:
                    if fp in optional_infos and optional_infos[fp].get("title", "").startswith("第") and "号" in optional_infos[fp].get("title", ""):
                        title = optional_infos[fp]["title"]
                        break
            info = {**info, "title": title}
            
            for file_path in group_files:
                try:
                    archive_path = self.get_archive_path(file_path, info)
                    archive_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # 既に存在する場合はスキップ
                    if archive_path.exists():
                        self.log(f"スキップ（既に存在）: {file_path.name}")
                        continue
                    
                    shutil.move(str(file_path), str(archive_path))
                    self.moved_files.append((file_path, archive_path))
                    self.log(f"移動完了: {file_path.name} → {archive_path.relative_to(NEWSLETTER_DIR)}")
                    
                except Exception as e:
                    error_msg = f"エラー: {file_path.name} - {str(e)}"
                    self.errors.append(error_msg)
                    self.log(error_msg)
        
        # 結果を表示
        print(f"\n✅ 整理完了: {len(self.moved_files)}個のファイルを移動しました。")
        
        if self.errors:
            print(f"\n⚠️  エラー: {len(self.errors)}個のエラーが発生しました。")
            for error in self.errors:
                print(f"   - {error}")
        
        return True

    def list_files(self):
        """現在のファイル状況を一覧表示"""
        print("\n📊 現在のファイル状況:")
        print("=" * 60)
        
        # ルートのファイル
        root_files = []
        for file_path in NEWSLETTER_DIR.iterdir():
            if file_path.is_file() and not self.should_exclude(file_path):
                info = self.parse_volume_info(file_path.name)
                if info:
                    root_files.append((file_path, info))
        
        if root_files:
            print(f"\n📁 ルートフォルダ ({len(root_files)}個のファイル):")
            for file_path, info in sorted(root_files, key=lambda x: (x[1]["date"], x[1]["volume"])):
                print(f"   - {file_path.name}")
                print(f"     ({info['year']}年 Vol.{info['volume']} {info['date']})")
        else:
            print("\n📁 ルートフォルダ: ファイルなし")
        
        # アーカイブフォルダ
        if ARCHIVE_DIR.exists():
            archive_count = sum(1 for _ in ARCHIVE_DIR.rglob("*") if _.is_file())
            print(f"\n📁 アーカイブフォルダ: {archive_count}個のファイル")
        else:
            print("\n📁 アーカイブフォルダ: 未作成")

        # _working フォルダ（貯まっていると配信後の整理漏れの可能性）
        if WORKING_DIR.exists():
            working_files = list(WORKING_DIR.iterdir())
            working_count = sum(1 for _ in working_files if _.is_file())
            print(f"\n📁 _working: {working_count}個のファイル")
            if working_count > 0:
                for f in sorted(working_files, key=lambda p: p.name):
                    if f.is_file():
                        print(f"   - {f.name}")
        else:
            print("\n📁 _working: 未作成")
        
        print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="ニュースレター ファイル整理スクリプト",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # 特定の号を整理
  python newsletter_organize.py --volume 04 --date 2025-12-27
  
  # 自動整理（確認なし）
  python newsletter_organize.py --auto --no-confirm
  
  # ファイル一覧を表示
  python newsletter_organize.py --list
  
  # ドライラン（実際には移動しない）
  python newsletter_organize.py --volume 04 --dry-run
        """,
    )
    
    parser.add_argument(
        "--volume",
        type=str,
        help="ボリューム番号（例: 04）",
    )
    
    parser.add_argument(
        "--date",
        type=str,
        help="配信日（例: 2025-12-27）",
    )
    
    parser.add_argument(
        "--auto",
        action="store_true",
        help="すべての配信済みファイルを自動的に整理",
    )
    
    parser.add_argument(
        "--list",
        action="store_true",
        help="現在のファイル状況を一覧表示",
    )
    
    parser.add_argument(
        "--no-confirm",
        action="store_true",
        help="確認プロセスをスキップ",
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="ドライラン（実際には移動しない）",
    )
    
    args = parser.parse_args()
    
    organizer = NewsletterOrganizer(dry_run=args.dry_run)
    
    # ディレクトリの初期化
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    WORKING_DIR.mkdir(parents=True, exist_ok=True)
    
    if args.list:
        organizer.list_files()
        return
    
    optional_infos: Optional[Dict[Path, Dict[str, str]]] = None
    if args.auto:
        # すべての配信済みファイルを検索（ルートのみ；_working は --volume --date 時のみ対象）
        files = organizer.find_newsletter_files()
    elif args.volume and args.date:
        # 特定の号：ルート＋_working の該当号をまとめてアーカイブ
        files = organizer.find_newsletter_files(
            volume=args.volume,
            date=args.date,
        )
        working_files = organizer.find_working_files(args.volume, args.date)
        files = files + working_files
        # _working のうち parse できないファイル用の info（例: Vol09_精密チェック.md）
        year, month, day = args.date.split("-")[0], args.date.split("-")[1], args.date.split("-")[2]
        vol_str = args.volume.zfill(2)
        default_info = {
            "year": year,
            "month": month,
            "day": day,
            "volume": vol_str,
            "title": f"第{int(vol_str)}号",
            "date": args.date,
        }
        optional_infos = {}
        for p in working_files:
            if not organizer.parse_volume_info(p.name):
                optional_infos[p] = default_info
    elif args.volume or args.date:
        files = organizer.find_newsletter_files(
            volume=args.volume,
            date=args.date,
        )
    else:
        parser.print_help()
        return
    
    if not files:
        print("整理するファイルが見つかりませんでした。")
        return
    
    # ファイルを整理
    organizer.organize_files(files, confirm=not args.no_confirm, optional_infos=optional_infos)


if __name__ == "__main__":
    main()

