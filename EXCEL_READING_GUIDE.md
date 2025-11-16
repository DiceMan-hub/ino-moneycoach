# Excelファイル読み込みガイド

## 概要

CursorでExcelファイルを読み込む方法を説明します。Claude Code拡張機能を使用して、効率的にExcelファイルを操作できます。

## 方法1: CursorでExcelファイルを直接開く（最も簡単）

### 手順

1. **ファイルエクスプローラーから開く**
   - サイドバーのファイルエクスプローラーで `.xlsx` または `.xls` ファイルを探す
   - ファイルをダブルクリックまたは右クリック → 「Open」

2. **コマンドパレットから開く**
   - `Cmd+P` (Mac) または `Ctrl+P` (Windows/Linux) でクイックオープンを開く
   - ファイル名を入力して選択

3. **ドラッグ&ドロップ**
   - Finder（Mac）またはエクスプローラー（Windows）からExcelファイルをCursorのウィンドウにドラッグ&ドロップ

### 表示方法

Excel Viewer拡張機能が自動的にファイルを読み込み、以下のように表示されます：
- セルをクリックして編集可能
- 数式バーで数式を確認・編集
- 行・列の追加・削除が可能

## 方法2: Pythonスクリプトで読み込む（データ分析・処理に最適）

### 必要なライブラリのインストール

まず、Pythonライブラリをインストールします：

```bash
pip install pandas openpyxl xlrd
```

### 基本的な読み込みコード

新しいPythonファイル（例：`read_excel.py`）を作成し、以下のコードを使用：

```python
import pandas as pd

# Excelファイルを読み込む
df = pd.read_excel('your_file.xlsx')

# データを表示
print(df.head())  # 最初の5行を表示
print(df.info())  # データの基本情報を表示
```

### シートを指定して読み込む

```python
import pandas as pd

# 特定のシートを読み込む
df = pd.read_excel('your_file.xlsx', sheet_name='Sheet1')

# またはシート番号で指定
df = pd.read_excel('your_file.xlsx', sheet_name=0)

# 全てのシートを読み込む
all_sheets = pd.read_excel('your_file.xlsx', sheet_name=None)
for sheet_name, df in all_sheets.items():
    print(f"シート名: {sheet_name}")
    print(df.head())
```

### 特定の範囲を読み込む

```python
import pandas as pd

# 特定の範囲（A1:D10）を読み込む
df = pd.read_excel('your_file.xlsx', 
                   sheet_name='Sheet1',
                   usecols='A:D',  # A列からD列まで
                   nrows=10)       # 最初の10行のみ
```

## 方法3: Claude Codeを使って読み込む（推奨）

### 手順

1. **新しいPythonファイルを作成**
   - `read_excel.py` などのファイルを作成

2. **Claude Codeを開く**
   - `Cmd+I` (Mac) または `Ctrl+I` (Windows/Linux) を押す

3. **指示を入力**
   ```
   Excelファイルを読み込んで、データの最初の5行を表示するPythonコードを書いて
   ```

   または：

   ```
   pandasを使ってExcelファイルを読み込むコードを書いて。ファイル名は'data.xlsx'で、シート名は'Sheet1'です。
   ```

### 使用例

#### 例1: 基本的な読み込み

Claude Codeに以下を入力：
```
Excelファイル（data.xlsx）を読み込んで、データの基本情報を表示するPythonスクリプトを書いて
```

生成されるコード：
```python
import pandas as pd

# Excelファイルを読み込む
df = pd.read_excel('data.xlsx')

# データの基本情報を表示
print("データの形状:", df.shape)
print("\n最初の5行:")
print(df.head())
print("\nデータの基本情報:")
print(df.info())
print("\n統計情報:")
print(df.describe())
```

#### 例2: データ分析スクリプト

Claude Codeに以下を入力：
```
Excelファイルを読み込んで、各列の合計値と平均値を計算するPythonスクリプトを書いて
```

#### 例3: データ変換スクリプト

Claude Codeに以下を入力：
```
Excelファイルを読み込んで、特定の列をフィルターして、新しいExcelファイルとして保存するスクリプトを書いて
```

## 実践的なサンプルコード

### サンプル1: データの読み込みと表示

```python
import pandas as pd

# Excelファイルを読み込む
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# データを確認
print("=" * 50)
print("データの形状:", df.shape)
print("=" * 50)
print("\n最初の10行:")
print(df.head(10))
print("\n列名:")
print(df.columns.tolist())
print("\nデータ型:")
print(df.dtypes)
```

### サンプル2: 複数シートの読み込み

```python
import pandas as pd

# 全てのシートを読み込む
excel_file = pd.ExcelFile('data.xlsx')

print("利用可能なシート:", excel_file.sheet_names)

# 各シートを読み込む
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    print(f"\nシート '{sheet_name}' のデータ:")
    print(df.head())
```

### サンプル3: データのフィルタリングと保存

```python
import pandas as pd

# Excelファイルを読み込む
df = pd.read_excel('input.xlsx')

# データをフィルタリング（例：特定の値以上）
filtered_df = df[df['列名'] > 100]

# 新しいExcelファイルとして保存
filtered_df.to_excel('output.xlsx', index=False)
print("フィルタリングされたデータを保存しました")
```

## Claude Codeを使った効率的な作業フロー

### ステップ1: ファイルパスの確認

Claude Codeに以下を入力：
```
現在のワークスペース内のExcelファイルを検索して、パスを表示するPythonコードを書いて
```

### ステップ2: データの確認

Claude Codeに以下を入力：
```
Excelファイルを読み込んで、欠損値の有無とデータ型を確認するコードを書いて
```

### ステップ3: データの処理

Claude Codeに以下を入力：
```
読み込んだExcelデータに対して、データクリーニングと変換を行うスクリプトを書いて
```

## トラブルシューティング

### エラー: ModuleNotFoundError: No module named 'pandas'

**解決方法:**
```bash
pip install pandas openpyxl
```

### エラー: FileNotFoundError

**解決方法:**
- ファイルパスが正しいか確認
- 相対パスと絶対パスの違いを確認
- ファイルがワークスペース内にあるか確認

### エラー: XLRDError: Excel xlsx file; not supported

**解決方法:**
```bash
pip install openpyxl
```

`.xlsx` ファイルを読み込むには `openpyxl` が必要です。

### 日本語の文字化け

**解決方法:**
```python
df = pd.read_excel('file.xlsx', engine='openpyxl')
```

または、エンコーディングを指定：
```python
df = pd.read_excel('file.xlsx', engine='openpyxl')
df.to_csv('output.csv', index=False, encoding='utf-8-sig')
```

## 参考リンク

- [Pandas read_excel Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- [OpenPyXL Documentation](https://openpyxl.readthedocs.io/)
- [GrapeCity Excel Viewer](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)

## 次のステップ

1. **ExcelファイルをCursorで開いてみる**
2. **Claude Codeを使って読み込みスクリプトを生成する**
3. **データ分析や変換スクリプトを作成する**








