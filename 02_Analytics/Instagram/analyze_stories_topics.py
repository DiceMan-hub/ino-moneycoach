#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Stories トピック別パフォーマンス分析
"""

import csv
import re
from collections import defaultdict
from datetime import datetime

def parse_date(date_str):
    """日付をパース"""
    if not date_str or date_str == 'Lifetime':
        return None
    try:
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

def categorize_topic(description):
    """Descriptionからトピックを分類"""
    if not description or description.strip() == '':
        return '説明なし'
    
    desc_lower = description.lower()
    
    # キーワードベースの分類
    if 'sfc' in desc_lower or '修行' in description:
        return 'SFC修行'
    elif 'プライオリティパス' in description or 'priority' in desc_lower:
        return 'プライオリティパス'
    elif 'アメックス' in description or 'amex' in desc_lower:
        return 'アメックス'
    elif 'クレカ' in description or 'クレジットカード' in description or 'カード' in description:
        return 'クレジットカード情報'
    elif 'マイル' in description or 'mile' in desc_lower:
        return 'マイル情報'
    elif 'ホテル' in description or 'hotel' in desc_lower or 'ラウンジ' in description:
        return 'ホテル情報'
    elif 'キャンペーン' in description or '年会費' in description:
        return 'キャンペーン情報'
    elif 'リール' in description or 'reel' in desc_lower:
        return 'リール紹介'
    elif 'ニュースレター' in description or 'newsletter' in desc_lower:
        return 'ニュースレター'
    elif 'note' in desc_lower or '購入' in description:
        return '商品・サービス紹介'
    elif 'フォロー' in description or 'follow' in desc_lower:
        return 'フォロー促進'
    elif 'ダウンロード' in description or '招待コード' in description or 'ポイントサイト' in description:
        return 'アプリ・サービス紹介'
    elif 'ハイライト' in description or 'highlight' in desc_lower:
        return 'ハイライト案内'
    elif '富士山' in description or '旅行' in description or '飛行機' in description or '✈️' in description:
        return '旅行・日常'
    elif '質問' in description or 'シリーズ' in description:
        return 'Q&A・解説'
    else:
        return 'その他'

# CSVファイルを読み込む
stories = []
with open('StoriesInsightDec-22-2025_Jan-20-2026_1610451196635627.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        date = parse_date(row.get('Publish time', ''))
        if date:
            description = row.get('Description', '') or ''
            stories.append({
                'Date': date,
                'Description': description,
                'Topic': categorize_topic(description),
                'Views': safe_int(row.get('Views', 0)),
                'Reach': safe_int(row.get('Reach', 0)),
                'Likes': safe_int(row.get('Likes', 0)),
                'Shares': safe_int(row.get('Shares', 0)),
                'ProfileVisits': safe_int(row.get('Profile visits', 0)),
                'Replies': safe_int(row.get('Replies', 0)),
                'Navigation': safe_int(row.get('Navigation', 0)),
                'LinkClicks': safe_int(row.get('Link clicks', 0)),
                'StickerTaps': safe_int(row.get('Sticker taps', 0)),
                'Follows': safe_int(row.get('Follows', 0))
            })

# トピック別に集計
topic_stats = defaultdict(lambda: {
    'count': 0,
    'totalViews': 0,
    'totalReach': 0,
    'totalLikes': 0,
    'totalShares': 0,
    'totalProfileVisits': 0,
    'totalReplies': 0,
    'totalNavigation': 0,
    'totalLinkClicks': 0,
    'totalStickerTaps': 0,
    'totalFollows': 0,
    'stories': []
})

for story in stories:
    topic = story['Topic']
    topic_stats[topic]['count'] += 1
    topic_stats[topic]['totalViews'] += story['Views']
    topic_stats[topic]['totalReach'] += story['Reach']
    topic_stats[topic]['totalLikes'] += story['Likes']
    topic_stats[topic]['totalShares'] += story['Shares']
    topic_stats[topic]['totalProfileVisits'] += story['ProfileVisits']
    topic_stats[topic]['totalReplies'] += story['Replies']
    topic_stats[topic]['totalNavigation'] += story['Navigation']
    topic_stats[topic]['totalLinkClicks'] += story['LinkClicks']
    topic_stats[topic]['totalStickerTaps'] += story['StickerTaps']
    topic_stats[topic]['totalFollows'] += story['Follows']
    topic_stats[topic]['stories'].append(story)

# トピック別の平均パフォーマンスを計算
topic_performance = []
for topic, stats in topic_stats.items():
    count = stats['count']
    if count > 0:
        avgViews = stats['totalViews'] / count
        avgReach = stats['totalReach'] / count
        avgLikes = stats['totalLikes'] / count
        avgProfileVisits = stats['totalProfileVisits'] / count
        avgFollows = stats['totalFollows'] / count
        
        # エンゲージメント率
        engagementRate = (stats['totalLikes'] + stats['totalReplies'] + stats['totalShares']) / stats['totalReach'] * 100 if stats['totalReach'] > 0 else 0
        
        # プロフィール訪問率
        visitRate = stats['totalProfileVisits'] / stats['totalReach'] * 100 if stats['totalReach'] > 0 else 0
        
        # フォロー獲得率
        followRate = stats['totalFollows'] / stats['totalReach'] * 100 if stats['totalReach'] > 0 else 0
        
        # 閲覧完了率
        viewCompletionRate = stats['totalViews'] / stats['totalReach'] * 100 if stats['totalReach'] > 0 else 0
        
        # 訪問→フォロー転換率
        visitToFollowRate = stats['totalFollows'] / stats['totalProfileVisits'] * 100 if stats['totalProfileVisits'] > 0 else 0
        
        topic_performance.append({
            'topic': topic,
            'count': count,
            'avgViews': avgViews,
            'avgReach': avgReach,
            'avgLikes': avgLikes,
            'avgProfileVisits': avgProfileVisits,
            'avgFollows': avgFollows,
            'engagementRate': engagementRate,
            'visitRate': visitRate,
            'followRate': followRate,
            'viewCompletionRate': viewCompletionRate,
            'visitToFollowRate': visitToFollowRate,
            'totalViews': stats['totalViews'],
            'totalReach': stats['totalReach'],
            'totalLikes': stats['totalLikes'],
            'totalProfileVisits': stats['totalProfileVisits'],
            'totalFollows': stats['totalFollows']
        })

# エンゲージメント率でソート
topic_performance.sort(key=lambda x: x['engagementRate'], reverse=True)

print("=" * 80)
print("ストーリーズ トピック別パフォーマンス分析")
print("=" * 80)
print(f"\n総ストーリーズ数: {len(stories)}")
print(f"トピック数: {len(topic_performance)}\n")

print("\n【トピック別 エンゲージメント率ランキング】")
print("-" * 80)
for i, perf in enumerate(topic_performance[:10], 1):
    print(f"\n{i}. {perf['topic']} (投稿数: {perf['count']})")
    print(f"   エンゲージメント率: {perf['engagementRate']:.2f}%")
    print(f"   平均閲覧数: {perf['avgViews']:.0f}")
    print(f"   平均リーチ: {perf['avgReach']:.0f}")
    print(f"   平均いいね: {perf['avgLikes']:.2f}")
    print(f"   プロフィール訪問率: {perf['visitRate']:.2f}%")
    print(f"   フォロー獲得率: {perf['followRate']:.2f}%")
    print(f"   閲覧完了率: {perf['viewCompletionRate']:.1f}%")
    print(f"   訪問→フォロー転換率: {perf['visitToFollowRate']:.2f}%")

print("\n\n【トピック別 プロフィール訪問率ランキング】")
print("-" * 80)
topic_performance_visit = sorted(topic_performance, key=lambda x: x['visitRate'], reverse=True)
for i, perf in enumerate(topic_performance_visit[:10], 1):
    print(f"\n{i}. {perf['topic']} (投稿数: {perf['count']})")
    print(f"   プロフィール訪問率: {perf['visitRate']:.2f}%")
    print(f"   平均プロフィール訪問: {perf['avgProfileVisits']:.1f}")

print("\n\n【トピック別 フォロー獲得率ランキング】")
print("-" * 80)
topic_performance_follow = sorted(topic_performance, key=lambda x: x['followRate'], reverse=True)
for i, perf in enumerate(topic_performance_follow[:10], 1):
    if perf['count'] > 0:
        print(f"\n{i}. {perf['topic']} (投稿数: {perf['count']})")
        print(f"   フォロー獲得率: {perf['followRate']:.2f}%")
        print(f"   総フォロー獲得: {perf['totalFollows']}")

print("\n\n【トピック別 閲覧完了率ランキング】")
print("-" * 80)
topic_performance_completion = sorted(topic_performance, key=lambda x: x['viewCompletionRate'], reverse=True)
for i, perf in enumerate(topic_performance_completion[:10], 1):
    print(f"\n{i}. {perf['topic']} (投稿数: {perf['count']})")
    print(f"   閲覧完了率: {perf['viewCompletionRate']:.1f}%")
    print(f"   平均閲覧数: {perf['avgViews']:.0f}")

# JavaScript形式で出力
print("\n\n// トピック別パフォーマンスデータ（JavaScript形式）")
print("const topicPerformanceData = [")
for i, perf in enumerate(topic_performance):
    comma = "," if i < len(topic_performance) - 1 else ""
    print(f'    {{"topic": "{perf["topic"]}", "count": {perf["count"]}, "avgViews": {perf["avgViews"]:.0f}, "avgReach": {perf["avgReach"]:.0f}, "avgLikes": {perf["avgLikes"]:.2f}, "avgProfileVisits": {perf["avgProfileVisits"]:.2f}, "avgFollows": {perf["avgFollows"]:.2f}, "engagementRate": {perf["engagementRate"]:.2f}, "visitRate": {perf["visitRate"]:.2f}, "followRate": {perf["followRate"]:.2f}, "viewCompletionRate": {perf["viewCompletionRate"]:.1f}, "visitToFollowRate": {perf["visitToFollowRate"]:.2f}}}{comma}')
print("];")
