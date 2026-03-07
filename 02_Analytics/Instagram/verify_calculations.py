#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Analytics 数値検証スクリプト
"""

import re
from datetime import datetime
from collections import defaultdict

def parse_csv_content(content):
    """CSVファイルの内容をパース"""
    data = []
    lines = content.strip().split('\n')
    
    # ヘッダー行をスキップ（最初の3行）
    for line in lines[3:]:
        if not line.strip():
            continue
        
        # CSV形式をパース（引用符を考慮）
        match = re.match(r'"([^"]+)"\s*,\s*"(\d+)"', line)
        if match:
            date_str = match.group(1).replace('T00:00:00', '').replace('T01:00:00', '')
            try:
                date_obj = datetime.strptime(date_str[:10], '%Y-%m-%d')
                value = int(match.group(2))
                data.append({'Date': date_str[:10], 'Value': value})
            except:
                continue
    
    return data

# CSVファイルを読み込む
with open('Follows.csv', 'r', encoding='utf-8') as f:
    follows_data = parse_csv_content(f.read())

with open('Interactions.csv', 'r', encoding='utf-8') as f:
    interactions_data = parse_csv_content(f.read())

with open('Reach.csv', 'r', encoding='utf-8') as f:
    reach_data = parse_csv_content(f.read())

with open('Visits.csv', 'r', encoding='utf-8') as f:
    visits_data = parse_csv_content(f.read())

with open('Link clicks.csv', 'r', encoding='utf-8') as f:
    linkclicks_data = parse_csv_content(f.read())

# データを日付で辞書化
follows_dict = {d['Date']: d['Value'] for d in follows_data}
interactions_dict = {d['Date']: d['Value'] for d in interactions_data}
reach_dict = {d['Date']: d['Value'] for d in reach_data}
visits_dict = {d['Date']: d['Value'] for d in visits_data}
linkclicks_dict = {d['Date']: d['Value'] for d in linkclicks_data}

# 統計計算
def calc_stats(data_list):
    values = [d['Value'] for d in data_list]
    total = sum(values)
    avg = total / len(values) if len(values) > 0 else 0
    sorted_vals = sorted(values)
    median = sorted_vals[len(sorted_vals) // 2] if sorted_vals else 0
    min_val = min(values) if values else 0
    max_val = max(values) if values else 0
    min_date = next((d['Date'] for d in data_list if d['Value'] == min_val), None)
    max_date = next((d['Date'] for d in data_list if d['Value'] == max_val), None)
    
    variance = sum((v - avg) ** 2 for v in values) / len(values) if len(values) > 0 else 0
    std_dev = variance ** 0.5
    cv = (std_dev / avg * 100) if avg > 0 else 0
    
    return {
        'total': total,
        'avg': avg,
        'median': median,
        'min': min_val,
        'max': max_val,
        'minDate': min_date,
        'maxDate': max_date,
        'cv': cv,
        'count': len(values)
    }

print("=" * 80)
print("統計値検証")
print("=" * 80)

stats_follows = calc_stats(follows_data)
stats_interactions = calc_stats(interactions_data)
stats_reach = calc_stats(reach_data)
stats_visits = calc_stats(visits_data)

print(f"\nフォロー数:")
print(f"  総計: {stats_follows['total']}")
print(f"  平均: {stats_follows['avg']:.2f}")
print(f"  中央値: {stats_follows['median']}")
print(f"  最小値: {stats_follows['min']} ({stats_follows['minDate']})")
print(f"  最大値: {stats_follows['max']} ({stats_follows['maxDate']})")
print(f"  変動係数: {stats_follows['cv']:.1f}%")
print(f"  データ数: {stats_follows['count']}")

print(f"\nインタラクション:")
print(f"  総計: {stats_interactions['total']}")
print(f"  平均: {stats_interactions['avg']:.2f}")
print(f"  中央値: {stats_interactions['median']}")
print(f"  最小値: {stats_interactions['min']} ({stats_interactions['minDate']})")
print(f"  最大値: {stats_interactions['max']} ({stats_interactions['maxDate']})")
print(f"  変動係数: {stats_interactions['cv']:.1f}%")
print(f"  データ数: {stats_interactions['count']}")

print(f"\nリーチ:")
print(f"  総計: {stats_reach['total']}")
print(f"  平均: {stats_reach['avg']:.2f}")
print(f"  中央値: {stats_reach['median']}")
print(f"  最小値: {stats_reach['min']} ({stats_reach['minDate']})")
print(f"  最大値: {stats_reach['max']} ({stats_reach['maxDate']})")
print(f"  変動係数: {stats_reach['cv']:.1f}%")
print(f"  データ数: {stats_reach['count']}")

print(f"\n訪問数:")
print(f"  総計: {stats_visits['total']}")
print(f"  平均: {stats_visits['avg']:.2f}")
print(f"  中央値: {stats_visits['median']}")
print(f"  最小値: {stats_visits['min']} ({stats_visits['minDate']})")
print(f"  最大値: {stats_visits['max']} ({stats_visits['maxDate']})")
print(f"  変動係数: {stats_visits['cv']:.1f}%")
print(f"  データ数: {stats_visits['count']}")

# 転換率計算
print("\n" + "=" * 80)
print("転換率検証（サンプル日付）")
print("=" * 80)

sample_dates = ['2025-10-23', '2025-11-03', '2025-12-13', '2026-01-01', '2026-01-19']

for date in sample_dates:
    reach = reach_dict.get(date, 0)
    interactions = interactions_dict.get(date, 0)
    follows = follows_dict.get(date, 0)
    visits = visits_dict.get(date, 0)
    clicks = linkclicks_dict.get(date, 0)
    
    if reach > 0:
        interaction_rate = (interactions / reach) * 100
        follow_rate = (follows / reach) * 100
        visit_rate = (visits / reach) * 100
        click_rate = (clicks / reach) * 100
    else:
        interaction_rate = follow_rate = visit_rate = click_rate = 0
    
    if visits > 0:
        visit_to_follow_rate = (follows / visits) * 100
    else:
        visit_to_follow_rate = 0
    
    engagement_rate = ((interactions + follows) / reach * 100) if reach > 0 else 0
    
    print(f"\n{date}:")
    print(f"  リーチ: {reach:,}")
    print(f"  インタラクション: {interactions:,}")
    print(f"  フォロー: {follows:,}")
    print(f"  訪問: {visits:,}")
    print(f"  クリック: {clicks:,}")
    print(f"  インタラクション率: {interaction_rate:.2f}%")
    print(f"  フォロー率: {follow_rate:.2f}%")
    print(f"  訪問率: {visit_rate:.2f}%")
    print(f"  クリック率: {click_rate:.2f}%")
    print(f"  訪問→フォロー転換率: {visit_to_follow_rate:.2f}%")
    print(f"  エンゲージメント率: {engagement_rate:.2f}%")

# 平均転換率計算
print("\n" + "=" * 80)
print("平均転換率")
print("=" * 80)

interaction_rates = []
follow_rates = []
visit_rates = []
click_rates = []
visit_to_follow_rates = []
engagement_rates = []

for date in sorted(reach_dict.keys()):
    reach = reach_dict.get(date, 0)
    interactions = interactions_dict.get(date, 0)
    follows = follows_dict.get(date, 0)
    visits = visits_dict.get(date, 0)
    clicks = linkclicks_dict.get(date, 0)
    
    if reach > 0:
        interaction_rates.append((interactions / reach) * 100)
        follow_rates.append((follows / reach) * 100)
        visit_rates.append((visits / reach) * 100)
        click_rates.append((clicks / reach) * 100)
        engagement_rates.append(((interactions + follows) / reach) * 100)
    
    if visits > 0:
        visit_to_follow_rates.append((follows / visits) * 100)

print(f"平均インタラクション率: {sum(interaction_rates) / len(interaction_rates):.2f}%")
print(f"平均フォロー率: {sum(follow_rates) / len(follow_rates):.2f}%")
print(f"平均訪問率: {sum(visit_rates) / len(visit_rates):.2f}%")
print(f"平均クリック率: {sum(click_rates) / len(click_rates):.2f}%")
print(f"平均訪問→フォロー転換率: {sum(visit_to_follow_rates) / len(visit_to_follow_rates):.2f}%")
print(f"平均エンゲージメント率: {sum(engagement_rates) / len(engagement_rates):.2f}%")
