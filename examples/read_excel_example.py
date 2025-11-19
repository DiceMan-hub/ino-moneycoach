"""
Excelファイル読み込みのサンプルコード

このファイルは、Claude Codeを使ってExcelファイルを読み込む実例です。
"""

import pandas as pd
import os

def read_excel_basic(file_path):
    """
    基本的なExcelファイルの読み込み
    
    Args:
        file_path (str): Excelファイルのパス
    
    Returns:
        pd.DataFrame: 読み込んだデータ
    """
    try:
        df = pd.read_excel(file_path)
        print(f"✓ ファイル '{file_path}' を正常に読み込みました")
        print(f"  データの形状: {df.shape[0]}行 × {df.shape[1]}列")
        return df
    except FileNotFoundError:
        print(f"✗ エラー: ファイル '{file_path}' が見つかりません")
        return None
    except Exception as e:
        print(f"✗ エラーが発生しました: {e}")
        return None


def read_excel_with_sheet(file_path, sheet_name=None):
    """
    シートを指定してExcelファイルを読み込む
    
    Args:
        file_path (str): Excelファイルのパス
        sheet_name (str or int, optional): シート名またはシート番号
    
    Returns:
        pd.DataFrame or dict: 読み込んだデータ
    """
    try:
        if sheet_name is None:
            # 全てのシートを読み込む
            excel_file = pd.ExcelFile(file_path)
            all_sheets = {}
            for sheet in excel_file.sheet_names:
                all_sheets[sheet] = pd.read_excel(excel_file, sheet_name=sheet)
            return all_sheets
        else:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"✓ シート '{sheet_name}' を読み込みました")
            return df
    except Exception as e:
        print(f"✗ エラーが発生しました: {e}")
        return None


def display_excel_info(df):
    """
    Excelデータの基本情報を表示
    
    Args:
        df (pd.DataFrame): データフレーム
    """
    if df is None:
        return
    
    print("\n" + "=" * 60)
    print("データの基本情報")
    print("=" * 60)
    print(f"\nデータの形状: {df.shape[0]}行 × {df.shape[1]}列")
    print(f"\n列名:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    
    print(f"\n最初の5行:")
    print(df.head())
    
    print(f"\nデータ型:")
    print(df.dtypes)
    
    print(f"\n欠損値の数:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("  欠損値はありません")
    
    print(f"\n統計情報:")
    print(df.describe())


def main():
    """
    メイン関数 - 使用例
    """
    # サンプルファイルパス（実際のファイルパスに置き換えてください）
    sample_file = 'sample.xlsx'
    
    # ファイルが存在するか確認
    if not os.path.exists(sample_file):
        print(f"⚠ '{sample_file}' が見つかりません")
        print("\n使用方法:")
        print("1. Excelファイルをワークスペースに配置")
        print("2. このスクリプトの 'sample_file' 変数を実際のファイル名に変更")
        print("3. スクリプトを実行")
        return
    
    # 基本的な読み込み
    print("【方法1: 基本的な読み込み】")
    df = read_excel_basic(sample_file)
    if df is not None:
        display_excel_info(df)
    
    # シートを指定して読み込み
    print("\n\n【方法2: シートを指定して読み込み】")
    df_sheet = read_excel_with_sheet(sample_file, sheet_name='Sheet1')
    if df_sheet is not None:
        display_excel_info(df_sheet)
    
    # 全てのシートを読み込み
    print("\n\n【方法3: 全てのシートを読み込み】")
    all_sheets = read_excel_with_sheet(sample_file)
    if all_sheets is not None:
        for sheet_name, sheet_df in all_sheets.items():
            print(f"\nシート名: {sheet_name}")
            print(f"  データの形状: {sheet_df.shape[0]}行 × {sheet_df.shape[1]}列")


if __name__ == "__main__":
    main()








