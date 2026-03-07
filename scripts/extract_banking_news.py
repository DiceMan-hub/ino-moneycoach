#!/usr/bin/env python3
"""
Banking news extraction script for Vol.04 newsletter
Extracts banking news and campaign information from Excel file
"""

import pandas as pd
import sys
import os
from datetime import datetime

def extract_banking_news(file_path):
    """
    Extract banking news and format for newsletter
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name='ニュース・キャンペーン情報')
        
        # Filter for banking-related entries (exclude non-banking financial services)
        banking_keywords = ['銀行', 'Bank', 'BANK', 'ネット銀行', 'neobank']
        banking_data = df[df['金融機関'].str.contains('|'.join(banking_keywords), case=False, na=False)]
        
        print("=" * 100)
        print("🏦 銀行・金融（金利アップラッシュ）- Vol.04 Newsletter Update")
        print("=" * 100)
        
        # Group by bank type
        major_banks = []
        net_banks = []
        regional_banks = []
        
        for _, row in banking_data.iterrows():
            bank_name = row['金融機関']
            
            # Categorize banks
            if any(mega in bank_name for mega in ['三菱UFJ', '三井住友銀行', 'みずほ']):
                major_banks.append(row)
            elif any(net in bank_name for net in ['auじぶん', 'SBI', '楽天', 'GMO', 'PayPay', 'MATSUI', 'みんなの銀行']):
                net_banks.append(row)
            else:
                regional_banks.append(row)
        
        # Format output for newsletter
        print("\n📊 **メガバンク金利改定情報**")
        print("-" * 50)
        if major_banks:
            for bank in major_banks:
                print(f"• **{bank['金融機関']}** | {bank['リリース日']}")
                print(f"  💰 {bank['概要']}")
                if pd.notna(bank['詳細ニュースURL']):
                    print(f"  🔗 [詳細]({bank['詳細ニュースURL']})")
                print()
        
        print("\n🌐 **ネット銀行・新興銀行**")
        print("-" * 50)
        if net_banks:
            for bank in net_banks:
                print(f"• **{bank['金融機関']}** | {bank['リリース日']}")
                print(f"  💰 {bank['概要']}")
                if pd.notna(bank['詳細ニュースURL']):
                    print(f"  🔗 [詳細]({bank['詳細ニュースURL']})")
                print()
        
        print("\n🏛️ **地方銀行・信託銀行**")
        print("-" * 50)
        if regional_banks:
            for bank in regional_banks:
                print(f"• **{bank['金融機関']}** | {bank['リリース日']}")
                print(f"  💰 {bank['概要']}")
                if pd.notna(bank['詳細ニュースURL']):
                    print(f"  🔗 [詳細]({bank['詳細ニュースURL']})")
                print()
        
        # Summary table for quick reference
        print("\n📋 **金利改定一覧表（HTML用）**")
        print("=" * 100)
        print("| 銀行名 | 実施日 | 改定前金利 | 改定後金利 | 特別条件 | 優先度 |")
        print("|--------|--------|------------|------------|----------|--------|")
        
        for _, row in banking_data.iterrows():
            bank_name = row['金融機関']
            release_date = row['リリース日']
            overview = row['概要']
            
            # Extract interest rate information
            if '年0.' in overview:
                if '0.20%から' in overview and '0.30%' in overview:
                    old_rate = "0.20%"
                    new_rate = "0.30%"
                elif '0.21%から' in overview and '0.31%' in overview:
                    old_rate = "0.21%"
                    new_rate = "0.31%"
                elif '0.30%から' in overview and '0.50%' in overview:
                    old_rate = "0.30%"
                    new_rate = "0.50%"
                elif '0.50%から' in overview and '0.70%' in overview:
                    old_rate = "0.50%"
                    new_rate = "0.70%"
                elif '0.50%から' in overview and '0.75%' in overview:
                    old_rate = "0.50%"
                    new_rate = "0.75%"
                elif '0.41%から' in overview and '0.65%' in overview:
                    old_rate = "0.41%"
                    new_rate = "0.65%"
                elif '0.57%から' in overview and '0.80%' in overview:
                    old_rate = "0.57%"
                    new_rate = "0.80%"
                else:
                    # Extract any percentage mentioned
                    import re
                    rates = re.findall(r'年(\d+\.\d+)%', overview)
                    if len(rates) >= 2:
                        old_rate = f"{rates[0]}%"
                        new_rate = f"{rates[1]}%"
                    elif len(rates) == 1:
                        old_rate = "-"
                        new_rate = f"{rates[0]}%"
                    else:
                        old_rate = "-"
                        new_rate = "要確認"
            else:
                old_rate = "-"
                new_rate = "要確認"
            
            # Determine special conditions
            special_conditions = ""
            if 'プレミアム' in overview:
                special_conditions = "プレミアム会員"
            elif '優遇' in overview:
                special_conditions = "条件達成時"
            elif '100万円以下' in overview:
                special_conditions = "100万円以下"
            elif '残高' in overview:
                special_conditions = "残高連動"
            
            # Determine priority
            priority = ""
            if any(mega in bank_name for mega in ['三菱UFJ', '三井住友銀行', 'みずほ']):
                priority = "🔥 高"
            elif '最高水準' in overview or '0.7' in new_rate or '0.8' in new_rate:
                priority = "⭐ 最高"
            elif 'ネット銀行' in overview or any(net in bank_name for net in ['auじぶん', 'SBI', '楽天']):
                priority = "📱 中"
            else:
                priority = "📋 低"
            
            print(f"| {bank_name} | {release_date} | {old_rate} | {new_rate} | {special_conditions} | {priority} |")
        
        print("\n" + "=" * 100)
        print("✅ Newsletter用データ抽出完了")
        print("💡 年末〜2026年初頭にかけて金利アップラッシュが継続中")
        print("🎯 特にネット銀行の高金利競争が激化")
        print("=" * 100)
        
    except Exception as e:
        print(f"❌ エラー: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    file_path = "/Users/mba2024/Documents/Obsidian/Dai DB/03_NewsLetter/金融機関ニュース_キャンペーン情報_20251226(1).xlsx"
    extract_banking_news(file_path)