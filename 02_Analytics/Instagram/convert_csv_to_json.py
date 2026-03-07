#!/usr/bin/env python3
"""
CSVファイルをJSON形式に変換して保存するスクリプト
Instagram Analyticsデータを構造化されたJSON形式で保存
"""

import csv
import json
import re
from datetime import datetime
from pathlib import Path

def parse_date(date_str):
    """日付文字列をYYYY-MM-DD形式に変換"""
    try:
        # ISO形式の日付をパース
        if 'T' in date_str:
            dt = datetime.fromisoformat(date_str.replace('T', ' ').split('.')[0])
        else:
            dt = datetime.strptime(date_str, '%Y-%m-%d')
        return dt.strftime('%Y-%m-%d')
    except:
        return date_str

def parse_csv_file(file_path):
    """CSVファイルをパースしてJSON形式のデータを返す"""
    data = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # sep=,行を削除
        content = re.sub(r'^sep=,.*?\n', '', content, flags=re.MULTILINE)
        lines = content.strip().split('\n')
        
        if len(lines) < 3:
            return data
        
        # ヘッダー行をスキップ（通常2行目がヘッダー）
        header_line = lines[1] if len(lines) > 1 else lines[0]
        
        # データ行を処理
        for line in lines[2:]:
            if not line.strip():
                continue
            
            # CSV行をパース（クォートで囲まれたフィールドを考慮）
            parts = re.findall(r'\"([^\"]*)\"|([^,]+)', line)
            if len(parts) >= 2:
                date_str = parts[0][0] if parts[0][0] else parts[0][1]
                value_str = parts[1][0] if parts[1][0] else parts[1][1]
                
                try:
                    date_formatted = parse_date(date_str.strip())
                    value = int(value_str.strip().replace(',', ''))
                    data.append({
                        "Date": date_formatted,
                        "Value": value
                    })
                except ValueError:
                    pass
    
    # 日付でソート
    data.sort(key=lambda x: x['Date'])
    return data

def parse_audience_csv(file_path):
    """Audience.csvを特別にパース"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        content = re.sub(r'^sep=,.*?\n', '', content, flags=re.MULTILINE)
        lines = [l.strip() for l in content.split('\n') if l.strip()]
    
    result = {
        "ageGender": [],
        "topCities": [],
        "topCountries": []
    }
    
    # 年齢・性別データ
    age_gender_start = None
    for i, line in enumerate(lines):
        if '"Age & gender"' in line:
            age_gender_start = i + 1
            break
    
    if age_gender_start:
        # ヘッダー行をスキップ
        for line in lines[age_gender_start + 1:]:
            if not line.strip() or line.startswith('"Top'):
                break
            parts = re.findall(r'\"([^\"]*)\"|([^,]+)', line)
            if len(parts) >= 3:
                age = parts[0][0] if parts[0][0] else parts[0][1]
                men = float(parts[1][0] if parts[1][0] else parts[1][1])
                women = float(parts[2][0] if parts[2][0] else parts[2][1])
                result["ageGender"].append({
                    "age": age,
                    "men": men,
                    "women": women
                })
    
    # 都市データ
    cities_start = None
    for i, line in enumerate(lines):
        if '"Top cities"' in line:
            cities_start = i + 1
            break
    
    if cities_start and cities_start + 1 < len(lines):
        cities_line = lines[cities_start]
        values_line = lines[cities_start + 1]
        
        cities = re.findall(r'\"([^\"]*)\"|([^,]+)', cities_line)
        values = re.findall(r'\"([^\"]*)\"|([^,]+)', values_line)
        
        for city_part, value_part in zip(cities, values):
            city = city_part[0] if city_part[0] else city_part[1]
            value = float(value_part[0] if value_part[0] else value_part[1])
            result["topCities"].append({
                "city": city,
                "value": value
            })
    
    # 国データ
    countries_start = None
    for i, line in enumerate(lines):
        if '"Top countries"' in line:
            countries_start = i + 1
            break
    
    if countries_start and countries_start + 1 < len(lines):
        countries_line = lines[countries_start]
        values_line = lines[countries_start + 1]
        
        countries = re.findall(r'\"([^\"]*)\"|([^,]+)', countries_line)
        values = re.findall(r'\"([^\"]*)\"|([^,]+)', values_line)
        
        for country_part, value_part in zip(countries, values):
            country = country_part[0] if country_part[0] else country_part[1]
            value = float(value_part[0] if value_part[0] else value_part[1])
            result["topCountries"].append({
                "country": country,
                "value": value
            })
    
    return result

def main():
    """メイン処理"""
    base_dir = Path(__file__).parent
    
    # 変換するCSVファイルのマッピング
    csv_files = {
        "Follows.csv": "follows",
        "Interactions.csv": "interactions",
        "Reach.csv": "reach",
        "Views.csv": "views",
        "Visits.csv": "visits",
        "Link clicks.csv": "link_clicks"
    }
    
    # 時系列データを変換
    all_data = {}
    for csv_file, key in csv_files.items():
        csv_path = base_dir / csv_file
        if csv_path.exists():
            print(f"Processing {csv_file}...")
            data = parse_csv_file(csv_path)
            all_data[key] = data
            print(f"  Converted {len(data)} records")
    
    # Audience.csvを特別に処理
    audience_path = base_dir / "Audience.csv"
    if audience_path.exists():
        print("Processing Audience.csv...")
        audience_data = parse_audience_csv(audience_path)
        all_data["audience"] = audience_data
        print("  Converted audience data")
    
    # Storiesデータも追加（既存のstories_data.jsから読み込むか、CSVから直接）
    stories_path = base_dir / "StoriesInsightDec-22-2025_Jan-20-2026_1610451196635627.csv"
    if stories_path.exists():
        print("Processing Stories CSV...")
        # Stories CSVは複雑な構造なので、既存のparse_stories.pyのロジックを使用
        # ここでは簡易的にスキップ（必要に応じて後で追加）
        print("  Stories data will be processed separately")
    
    # JSONファイルに保存
    output_path = base_dir / "instagram_data.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ All data saved to {output_path}")
    print(f"   Total keys: {len(all_data)}")
    for key, value in all_data.items():
        if isinstance(value, list):
            print(f"   - {key}: {len(value)} records")
        elif isinstance(value, dict):
            print(f"   - {key}: {len(value)} sections")

if __name__ == "__main__":
    main()
