"""
Excelファイルの列順序を変更するスクリプト
"""

import pandas as pd
import os
import sys

def reorder_columns(excel_path, output_path=None):
    """
    Excelファイルの列順序を変更
    
    Args:
        excel_path (str): Excelファイルのパス
        output_path (str): 出力Excelファイルのパス（省略時は上書き）
    """
    try:
        # ファイルの存在確認
        if not os.path.exists(excel_path):
            print(f"❌ エラー: ファイル '{excel_path}' が見つかりません")
            return None
        
        # Excelファイルを読み込む
        excel_file = pd.ExcelFile(excel_path)
        
        # 出力パスの決定
        if output_path is None:
            output_path = excel_path
        
        # 各シートを処理
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
                
                # 現在の列名を取得
                columns = list(df.columns)
                
                # 「ローソンPontaプラス」の位置を確認
                if 'ローソンPontaプラス' in columns:
                    # 「ローソンPontaプラス」を削除
                    columns.remove('ローソンPontaプラス')
                    
                    # 「JCB還元率」の位置を確認
                    if 'JCB還元率' in columns:
                        jcb_index = columns.index('JCB還元率')
                        # 「JCB還元率」の右（次の位置）に挿入
                        columns.insert(jcb_index + 1, 'ローソンPontaプラス')
                    else:
                        # 「JCB還元率」が見つからない場合は最後に追加
                        columns.append('ローソンPontaプラス')
                    
                    # 列順序を変更
                    df = df[columns]
                    print(f"✅ シート '{sheet_name}': 列順序を変更しました")
                    print(f"   「ローソンPontaプラス」を「JCB還元率」の右に移動")
                else:
                    print(f"⚠️  シート '{sheet_name}': 「ローソンPontaプラス」列が見つかりません")
                
                # シートを書き込み
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"✅ Excelファイルを保存しました: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    # コマンドライン引数からファイルパスを取得
    if len(sys.argv) > 1:
        excel_path = sys.argv[1]
    else:
        excel_path = "00_Projects/高還元決済/キャッシュレス決済対応状況_完全版.xlsx"
    
    # 出力パス（オプション）
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 絶対パスに変換
    if not os.path.isabs(excel_path):
        workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        excel_path = os.path.join(workspace_root, excel_path)
    
    if output_path and not os.path.isabs(output_path):
        output_path = os.path.join(workspace_root, output_path)
    
    reorder_columns(excel_path, output_path)




