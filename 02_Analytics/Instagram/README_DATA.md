# Instagram Analytics データ構造

このフォルダには、Instagram Analyticsのデータが複数の形式で保存されています。

## データファイル

### JSON形式（推奨）
- **`instagram_data.json`**: すべてのデータを構造化されたJSON形式で保存
  - プログラムからアクセスしやすい
  - 型が明確
  - メタデータを含む

### CSV形式（元データ）
- `Follows.csv`: フォロー数（日次）
- `Interactions.csv`: インタラクション数（日次）
- `Reach.csv`: リーチ数（日次）
- `Views.csv`: 閲覧数（日次）
- `Visits.csv`: プロフィール訪問数（日次）
- `Link clicks.csv`: リンククリック数（日次）
- `Audience.csv`: オーディエンス分析（年齢・性別、都市、国）
- `StoriesInsightDec-22-2025_Jan-20-2026_1610451196635627.csv`: ストーリーズ分析データ

## JSONデータ構造

### 時系列データ
すべての時系列データは以下の形式です：
```json
{
  "Date": "YYYY-MM-DD",
  "Value": number
}
```

#### 利用可能なデータセット
- `follows`: フォロー数（90日間）
- `interactions`: インタラクション数（90日間）
- `reach`: リーチ数（90日間）
- `visits`: プロフィール訪問数（90日間）
- `views`: 閲覧数（90日間）
- `linkClicks`: リンククリック数（90日間）

### オーディエンスデータ
```json
{
  "audience": {
    "ageGender": [
      {"age": "18-24", "men": 2.0, "women": 0.5},
      ...
    ],
    "topCities": [
      {"city": "Yokohama, Kanagawa, Japan", "value": 4.4},
      ...
    ],
    "topCountries": [
      {"country": "Japan", "value": 97.4},
      ...
    ]
  }
}
```

### ストーリーズデータ
```json
{
  "stories": [
    {
      "Date": "YYYY-MM-DD",
      "Views": number,
      "Reach": number,
      "Likes": number,
      "ProfileVisits": number,
      "Follows": number,
      "StoryCount": number
    },
    ...
  ]
}
```

### メタデータ
```json
{
  "metadata": {
    "dataPeriod": {
      "startDate": "2025-10-23",
      "endDate": "2026-01-20",
      "totalDays": 90
    },
    "storiesPeriod": {
      "startDate": "2025-12-22",
      "endDate": "2026-01-20",
      "totalDays": 30
    },
    "lastUpdated": "2026-01-20",
    "dataSource": "Instagram Analytics Export",
    "version": "1.0"
  }
}
```

## データの使用例

### Python
```python
import json

with open('instagram_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# フォロー数の合計
total_follows = sum(item['Value'] for item in data['follows'])

# 特定の日のデータを取得
date = "2026-01-01"
follows_on_date = next((item['Value'] for item in data['follows'] if item['Date'] == date), None)
```

### JavaScript
```javascript
const data = require('./instagram_data.json');

// フォロー数の合計
const totalFollows = data.follows.reduce((sum, item) => sum + item.Value, 0);

// 特定の日のデータを取得
const date = "2026-01-01";
const followsOnDate = data.follows.find(item => item.Date === date)?.Value;
```

## データ更新

新しいCSVデータが追加された場合は、`convert_csv_to_json.py`スクリプトを実行してJSONファイルを更新できます。

```bash
python3 convert_csv_to_json.py
```

## 注意事項

- すべての日付は `YYYY-MM-DD` 形式です
- 数値は整数または浮動小数点数です
- オーディエンスデータの割合はパーセンテージ（%）です
- データは日付順にソートされています
