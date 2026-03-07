"""
ExcelファイルをHTMLテーブルに変換するスクリプト
"""

import pandas as pd
import os
import sys

def excel_to_html(excel_path, output_path=None):
    """
    Excelファイルを読み込んでHTMLテーブルに変換
    
    Args:
        excel_path (str): Excelファイルのパス
        output_path (str): 出力HTMLファイルのパス（省略時は自動生成）
    """
    try:
        # ファイルの存在確認
        if not os.path.exists(excel_path):
            print(f"❌ エラー: ファイル '{excel_path}' が見つかりません")
            return None
        
        # Excelファイルを読み込む
        excel_file = pd.ExcelFile(excel_path, engine='openpyxl')
        sheet_names = excel_file.sheet_names
        
        # HTMLの開始部分
        html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>キャッシュレス決済対応状況</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1600px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            padding: 30px;
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
            font-weight: 600;
        }
        
        .info {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }
        
        .content {
            overflow-x: auto;
        }
        
        .sheet-section {
            margin-bottom: 40px;
        }
        
        .sheet-title {
            font-size: 22px;
            font-weight: 600;
            color: #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #2c3e50;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            overflow-x: auto;
        }
        
        thead {
            background-color: #2c3e50;
            color: white;
            position: sticky;
            top: 0;
        }
        
        th {
            padding: 15px;
            text-align: left;
            font-weight: 600;
            font-size: 13px;
            border: 1px solid #34495e;
            white-space: nowrap;
        }
        
        td {
            padding: 12px 15px;
            border: 1px solid #ecf0f1;
            font-size: 13px;
        }
        
        th.card-name, td.card-name {
            white-space: nowrap;
        }
        
        tbody tr:nth-child(odd) {
            background-color: #f9f9f9;
        }
        
        tbody tr:hover {
            background-color: #f0f0f0;
        }
        
        tbody tr td:first-child {
            font-weight: 600;
            color: #2c3e50;
            background-color: #ecf0f1;
        }
        
        tbody tr td:nth-child(2) {
            color: #7f8c8d;
            font-size: 12px;
        }
        
        .category {
            font-weight: 600;
            color: #2c3e50;
        }
        
        .percentage {
            color: #2e7d32;
            font-weight: 500;
        }
        
        .check-mark {
            color: #2e7d32;
            font-weight: bold;
        }
        
        .cross-mark {
            color: #d32f2f;
            font-weight: bold;
        }
        
        .info-section {
            margin-top: 20px;
            padding: 15px;
            background-color: #ecf0f1;
            border-left: 4px solid #2c3e50;
            border-radius: 4px;
            font-size: 12px;
            color: #555;
            line-height: 1.8;
        }
        
        .info-section h3 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 16px;
        }
        
        .info-section p {
            color: #555;
            font-size: 14px;
            line-height: 1.6;
        }
        
        .category-header {
            background-color: #34495e !important;
            color: white !important;
            font-weight: 700 !important;
            font-size: 14px !important;
            text-align: center !important;
            padding: 12px 15px !important;
            border: 1px solid #2c3e50 !important;
        }
        
        .category-header td {
            background-color: #34495e !important;
            color: white !important;
            border: 1px solid #2c3e50 !important;
        }
        
        @media print {
            body {
                background: white;
                padding: 0;
            }
            
            .container {
                box-shadow: none;
            }
        }
        
        @media (max-width: 1024px) {
            .container {
                padding: 15px;
            }
            
            table {
                font-size: 11px;
            }
            
            th, td {
                padding: 8px 10px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>キャッシュレス決済対応状況</h1>
        <div class="info">店舗別・決済手段別の還元率一覧</div>
        <div class="content">
"""
        
        # 各シートを処理
        for sheet_idx, sheet_name in enumerate(sheet_names, 1):
            df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')
            
            # 列順序を変更: 「ローソンPontaプラス」を「JCB還元率」の右に移動
            columns = list(df.columns)
            if 'ローソンPontaプラス' in columns and 'JCB還元率' in columns:
                columns.remove('ローソンPontaプラス')
                jcb_index = columns.index('JCB還元率')
                columns.insert(jcb_index + 1, 'ローソンPontaプラス')
                df = df[columns]
            
            # カード比較表の列（d払いより前）
            card_columns = []
            code_columns = []
            split_index = None
            
            for i, col in enumerate(df.columns):
                if col == 'd払い':
                    split_index = i
                    break
            
            if split_index is not None:
                card_columns = list(df.columns[:split_index])
                code_columns = ['店舗名', 'カテゴリー'] + list(df.columns[split_index:])
            else:
                card_columns = list(df.columns)
            
            # シート情報セクション
            html_content += f"""
            <div class="sheet-section">
                <div class="sheet-title">📋 シート {sheet_idx}: {sheet_name}</div>
                <div class="info-section">
                    <h3>データ情報</h3>
                    <p>データ行数: {df.shape[0]}行 | 列数: {df.shape[1]}列</p>
                </div>
"""
            
            # カード比較表
            html_content += """
                <h2 style="margin-top: 30px; margin-bottom: 15px; font-size: 20px; color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 8px;">💳 カード比較表</h2>
                <table>
                    <thead>
                        <tr>
"""
            
            # カード比較表のヘッダー
            for col in card_columns:
                card_class = ' class="card-name"' if col in ['三井住友カード', '三菱UFJカード', 'JCB還元率', 'ローソンPontaプラス'] else ''
                html_content += f'                            <th{card_class}>{col}</th>\n'
            
            html_content += """                        </tr>
                    </thead>
                    <tbody>
"""
            
            # カード比較表のデータ行
            category_icons = {
                'コンビニ': '🏪',
                'スーパー': '🛒',
                'ドラッグストア': '💊',
                '100円ショップ': '💰',
                'ファストフード': '🍔',
                'ファミレス': '🍽️',
                '外食': '🍜',
                'カフェ': '☕',
                '弁当': '🍱',
                '家電量販店': '📺',
                '百貨店': '🏬',
                '雑貨': '🛍️',
                'カラオケ': '🎤',
                'アミューズメント': '🎮',
                'エンタメ': '🎬',
                'オンライン': '💻',
                '駐車場': '🅿️',
                'カーサービス': '🚗',
                '自販機': '🥤'
            }
            
            prev_category = None
            for idx, row in df.iterrows():
                # カテゴリー列を取得
                if 'カテゴリー' in card_columns:
                    current_category = str(row['カテゴリー']) if pd.notna(row['カテゴリー']) else None
                    
                    # カテゴリーが変わった場合、見出しを追加
                    if current_category and current_category != prev_category:
                        icon = category_icons.get(current_category, '📋')
                        html_content += f'                        <tr class="category-header"><td colspan="{len(card_columns)}">{icon} {current_category}</td></tr>\n'
                        prev_category = current_category
                
                html_content += "                        <tr>\n"
                for col in card_columns:
                    value = row[col]
                    
                    # NaNの処理
                    if pd.isna(value):
                        cell_value = ""
                    else:
                        cell_value = str(value)
                    
                    # セルのスタイルクラスを決定
                    cell_class = ""
                    if col == "カテゴリー":
                        cell_class = ' class="category"'
                    elif col in ['三井住友カード', '三菱UFJカード', 'JCB還元率', 'ローソンPontaプラス']:
                        cell_class = ' class="card-name'
                        if "%" in cell_value or any(x in cell_value for x in ["0.5%", "1%", "1.5%", "7%", "5%", "8%", "10%"]):
                            cell_class += ' percentage"'
                        else:
                            cell_class += '"'
                    elif "%" in cell_value or any(x in cell_value for x in ["0.5%", "1%", "1.5%", "7%", "5%", "8%", "10%"]):
                        cell_class = ' class="percentage"'
                    elif cell_value == "○":
                        cell_class = ' class="check-mark"'
                    elif cell_value == "×":
                        cell_class = ' class="cross-mark"'
                    
                    html_content += f'                            <td{cell_class}>{cell_value}</td>\n'
                
                html_content += "                        </tr>\n"
            
            html_content += """                    </tbody>
                </table>
"""
            
            # コード決済表（d払い以降）
            if code_columns:
                html_content += """
                <h2 style="margin-top: 50px; margin-bottom: 15px; font-size: 20px; color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 8px;">📱 コード決済対応状況</h2>
                <table>
                    <thead>
                        <tr>
"""
                
                # コード決済表のヘッダー
                for col in code_columns:
                    html_content += f'                            <th>{col}</th>\n'
                
                html_content += """                        </tr>
                    </thead>
                    <tbody>
"""
                
                # コード決済表のデータ行
                for idx, row in df.iterrows():
                    html_content += "                        <tr>\n"
                    for col in code_columns:
                        value = row[col]
                        
                        # NaNの処理
                        if pd.isna(value):
                            cell_value = ""
                        else:
                            cell_value = str(value)
                        
                        # セルのスタイルクラスを決定
                        cell_class = ""
                        if col == "カテゴリー":
                            cell_class = ' class="category"'
                        elif "%" in cell_value or any(x in cell_value for x in ["0.5%", "1%", "1.5%", "7%", "5%", "8%", "10%"]):
                            cell_class = ' class="percentage"'
                        elif cell_value == "○":
                            cell_class = ' class="check-mark"'
                        elif cell_value == "×":
                            cell_class = ' class="cross-mark"'
                        
                        html_content += f'                            <td{cell_class}>{cell_value}</td>\n'
                    
                    html_content += "                        </tr>\n"
                
                html_content += """                    </tbody>
                </table>
"""
            
            html_content += """            </div>
"""
        
        # HTMLの終了部分
        html_content += """        </div>
    </div>
</body>
</html>"""
        
        # 出力パスの決定
        if output_path is None:
            base_name = os.path.splitext(os.path.basename(excel_path))[0]
            output_dir = os.path.dirname(excel_path)
            output_path = os.path.join(output_dir, f"{base_name}.html")
        
        # HTMLファイルを保存
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTMLファイルを作成しました: {output_path}")
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
    
    excel_to_html(excel_path, output_path)

