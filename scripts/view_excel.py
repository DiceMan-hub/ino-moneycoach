"""
Excelファイルを読み込んで表示するスクリプト
現在開いているExcelファイルの内容を表示します
"""

import pandas as pd
import sys
import os

def view_excel(file_path):
    """
    Excelファイルを読み込んで内容を表示
    
    Args:
        file_path (str): Excelファイルのパス
    """
    try:
        # ファイルの存在確認
        if not os.path.exists(file_path):
            print(f"❌ エラー: ファイル '{file_path}' が見つかりません")
            return
        
        print("=" * 80)
        print(f"📊 Excelファイル: {os.path.basename(file_path)}")
        print("=" * 80)
        
        # 全てのシートを読み込む
        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names
        
        print(f"\n📑 シート数: {len(sheet_names)}")
        print(f"📋 シート名: {', '.join(sheet_names)}")
        print("\n" + "=" * 80)
        
        # 各シートを表示
        for idx, sheet_name in enumerate(sheet_names, 1):
            print(f"\n【シート {idx}: {sheet_name}】")
            print("-" * 80)
            
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            
            print(f"📐 データの形状: {df.shape[0]}行 × {df.shape[1]}列")
            
            if df.shape[0] > 0:
                print(f"\n📊 列名:")
                for i, col in enumerate(df.columns, 1):
                    print(f"  {i}. {col}")
                
                print(f"\n📝 データの最初の20行:")
                print(df.head(20).to_string())
                
                if df.shape[0] > 20:
                    print(f"\n... (残り {df.shape[0] - 20} 行)")
                
                # データ型と欠損値の情報
                print(f"\n📈 データ型:")
                print(df.dtypes)
                
                print(f"\n🔍 欠損値:")
                missing = df.isnull().sum()
                if missing.sum() > 0:
                    for col, count in missing[missing > 0].items():
                        print(f"  {col}: {count}個")
                else:
                    print("  欠損値はありません")
            else:
                print("  (データがありません)")
            
            if idx < len(sheet_names):
                print("\n" + "=" * 80)
        
        print("\n" + "=" * 80)
        print("✅ 読み込み完了")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # コマンドライン引数からファイルパスを取得
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # デフォルトのファイルパス
        file_path = "00_Projects/高還元決済/キャッシュレス決済対応状況_完全版.xlsx"
    
    # 絶対パスに変換
    if not os.path.isabs(file_path):
        workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(workspace_root, file_path)
    
    view_excel(file_path)




