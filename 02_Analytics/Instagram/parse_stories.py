#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Stories CSV パーサー
"""

import csv
import re
from datetime import datetime
from collections import defaultdict

def parse_date(date_str):
    """日付をパース（MM/DD/YYYY HH:MM形式またはMM/DD/YYYY形式をYYYY-MM-DDに変換）"""
    if not date_str or date_str == 'Lifetime':
        return None
    try:
        # "01/01/2026 08:47"形式をパース
        if ' ' in date_str:
            dt = datetime.strptime(date_str.split()[0], "%m/%d/%Y")
        else:
            dt = datetime.strptime(date_str, "%m/%d/%Y")
        return dt.strftime("%Y-%m-%d")
    except:
        return None

def safe_int(value):
    """安全に整数に変換"""
    if value == '' or value is None:
        return 0
    try:
        return int(value)
    except:
        return 0

# CSVファイルを読み込む
stories_data = []
with open('StoriesInsightDec-22-2025_Jan-20-2026_1610451196635627.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Publish timeから日付を取得
        date = parse_date(row.get('Publish time', ''))
        if date:
            stories_data.append({
                'Date': date,
                'Views': safe_int(row.get('Views', 0)),
                'Reach': safe_int(row.get('Reach', 0)),
                'Likes': safe_int(row.get('Likes', 0)),
                'Shares': safe_int(row.get('Shares', 0)),
                'Profile visits': safe_int(row.get('Profile visits', 0)),
                'Replies': safe_int(row.get('Replies', 0)),
                'Navigation': safe_int(row.get('Navigation', 0)),
                'Link clicks': safe_int(row.get('Link clicks', 0)),
                'Sticker taps': safe_int(row.get('Sticker taps', 0)),
                'Follows': safe_int(row.get('Follows', 0))
            })

# 日付ごとに集計
daily_data = defaultdict(lambda: {
    'Views': [],
    'Reach': [],
    'Likes': [],
    'Shares': [],
    'Profile visits': [],
    'Replies': [],
    'Navigation': [],
    'Link clicks': [],
    'Sticker taps': [],
    'Follows': [],
    'Count': 0
})

for story in stories_data:
    date = story['Date']
    daily_data[date]['Views'].append(story['Views'])
    daily_data[date]['Reach'].append(story['Reach'])
    daily_data[date]['Likes'].append(story['Likes'])
    daily_data[date]['Shares'].append(story['Shares'])
    daily_data[date]['Profile visits'].append(story['Profile visits'])
    daily_data[date]['Replies'].append(story['Replies'])
    daily_data[date]['Navigation'].append(story['Navigation'])
    daily_data[date]['Link clicks'].append(story['Link clicks'])
    daily_data[date]['Sticker taps'].append(story['Sticker taps'])
    daily_data[date]['Follows'].append(story['Follows'])
    daily_data[date]['Count'] += 1

# 日付ごとの合計値を計算
daily_totals = []
for date in sorted(daily_data.keys()):
    data = daily_data[date]
    daily_totals.append({
        'Date': date,
        'Views': sum(data['Views']),
        'Reach': sum(data['Reach']),
        'Likes': sum(data['Likes']),
        'Shares': sum(data['Shares']),
        'Profile visits': sum(data['Profile visits']),
        'Replies': sum(data['Replies']),
        'Navigation': sum(data['Navigation']),
        'Link clicks': sum(data['Link clicks']),
        'Sticker taps': sum(data['Sticker taps']),
        'Follows': sum(data['Follows']),
        'Story count': data['Count']
    })

# JavaScript形式で出力
print("// Stories data (daily aggregated)")
print("const storiesData = [")
for i, day in enumerate(daily_totals):
    comma = "," if i < len(daily_totals) - 1 else ""
    print(f'    {{"Date": "{day["Date"]}", "Views": {day["Views"]}, "Reach": {day["Reach"]}, "Likes": {day["Likes"]}, "Shares": {day["Shares"]}, "ProfileVisits": {day["Profile visits"]}, "Replies": {day["Replies"]}, "Navigation": {day["Navigation"]}, "LinkClicks": {day["Link clicks"]}, "StickerTaps": {day["Sticker taps"]}, "Follows": {day["Follows"]}, "StoryCount": {day["Story count"]}}}{comma}')
print("];")
