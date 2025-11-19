# Excelファイル編集ガイド（Claude Code対応）

## 概要

このワークスペースでClaude Code拡張機能を使用してExcelファイルを編集する方法を説明します。

## インストール済み拡張機能

### Excel編集用拡張機能
- **GrapeCity Excel Viewer** (v4.2.58) - Excelファイルのビューアーとエディター
- **VS Code Office** (v3.5.4) - Officeファイル（Excel、Word、PowerPoint）のサポート

### Claude Code統合
- **Anthropic Claude Code** - AIアシスタントによるコード生成と編集支援

## Excelファイルの編集方法

### 方法1: Excel Viewer拡張機能を使用（推奨）

1. **Excelファイルを開く**
   - `.xlsx` または `.xls` ファイルをCursorで開く
   - 自動的にExcel Viewerで表示されます

2. **編集機能**
   - セルをクリックして直接編集
   - 数式の入力と編集
   - 行・列の追加・削除
   - フォーマットの変更

3. **Claude Codeとの連携**
   - Excelファイルを開いた状態で `Cmd+I` (Mac) または `Ctrl+I` (Windows/Linux) を押す
   - Claude Codeに「このセルに数式を追加して」などと指示できます
   - Claude Codeが適切な数式やデータを提案します

### 方法2: Pythonスクリプトで編集（高度な操作）

Claude Codeを使用してPythonスクリプトを生成し、Excelファイルをプログラムで編集できます。

#### 必要なPythonライブラリのインストール

```bash
pip install pandas openpyxl xlrd
```

#### Claude Codeでスクリプトを生成

1. 新しいPythonファイル（例：`edit_excel.py`）を作成
2. `Cmd+I` でClaude Codeを開く
3. 以下のような指示を入力：
   ```
   Excelファイルを読み込んで、特定のセルを編集するPythonスクリプトを書いて
   ```

#### 使用例

```python
import pandas as pd

# Excelファイルを読み込む
df = pd.read_excel('your_file.xlsx')

# データを編集
df['列名'] = df['列名'].apply(lambda x: x * 2)

# 保存
df.to_excel('output.xlsx', index=False)
```

### 方法3: CSVとして編集

シンプルなデータの場合、CSV形式で編集することもできます：

1. ExcelファイルをCSVとしてエクスポート（またはPythonで変換）
2. CSVファイルを開いて編集
3. Claude Codeでデータ処理スクリプトを生成
4. 必要に応じてExcel形式に戻す

## Claude CodeでExcel操作を支援してもらう方法

### 基本的な使い方

1. **Excelファイルを開く**
2. **`Cmd+I` (Mac) または `Ctrl+I` (Windows/Linux) を押す**
3. **以下のような指示を入力：**

   - 「この列の合計を計算する数式を追加して」
   - 「A列のデータをB列にコピーするスクリプトを書いて」
   - 「特定の条件で行をフィルターするPythonスクリプトを生成して」
   - 「このセル範囲の平均値を計算して」

### 高度な操作例

#### データ分析スクリプトの生成

```
Excelファイルを読み込んで、各列の統計情報を表示するPythonスクリプトを書いて
```

#### データ変換スクリプトの生成

```
CSVファイルを読み込んで、特定の列を変換してExcelファイルとして保存するスクリプトを書いて
```

#### データ可視化スクリプトの生成

```
Excelファイルのデータを読み込んで、グラフを作成するPythonスクリプトを書いて
```

## トラブルシューティング

### Excelファイルが開けない場合

1. **拡張機能が有効になっているか確認**
   - 拡張機能ビューで「GrapeCity Excel Viewer」と「VS Code Office」が有効になっているか確認

2. **ファイル形式の確認**
   - `.xlsx` 形式（Excel 2007以降）が推奨です
   - 古い `.xls` 形式もサポートされていますが、一部機能が制限される場合があります

### Claude CodeがExcelファイルを認識しない場合

1. **ファイルを一度閉じて再度開く**
2. **拡張機能を再読み込み**
   - `Cmd+Shift+P` → "Developer: Reload Window"

### Pythonスクリプトでエラーが発生する場合

1. **必要なライブラリがインストールされているか確認**
   ```bash
   pip list | grep -E "(pandas|openpyxl|xlrd)"
   ```

2. **Pythonパスの確認**
   - Cursorの設定でPythonインタープリターのパスが正しく設定されているか確認

## 参考リンク

- [GrapeCity Excel Viewer Documentation](https://marketplace.visualstudio.com/items?itemName=GrapeCity.gc-excelviewer)
- [VS Code Office Documentation](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-office)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [OpenPyXL Documentation](https://openpyxl.readthedocs.io/)

## 次のステップ

1. Excelファイルを開いて、Excel Viewerの機能を試してみてください
2. `Cmd+I` でClaude Codeを開いて、Excel操作の支援を依頼してみてください
3. 複雑な操作が必要な場合は、Pythonスクリプトを生成して実行してください








