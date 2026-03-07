#!/usr/bin/env python3
"""
Amex Travel Planner - ホテルプランオプティマイザー
スクレイピングしたFHR/THCデータから最適プランを計算する

Usage:
    python optimize_plan.py --data <scraped_data.json> --nights <total_nights>
"""

import json
import itertools
import argparse
from typing import List, Dict, Any, Tuple


CHAIN_PRIORITY = {
    "marriott": 1, "marriott bonvoy": 1, "sheraton": 1, "westin": 1, "w hotel": 1,
    "ihg": 2, "intercontinental": 2, "kimpton": 2, "crowne plaza": 2, "holiday inn": 2,
    "hyatt": 3, "park hyatt": 3, "grand hyatt": 3, "andaz": 3, "alila": 3,
    "hilton": 4, "waldorf": 4, "waldorf astoria": 4, "conrad": 4, "doubletree": 4,
}


def get_chain_priority(chain_name: str) -> int:
    if not chain_name:
        return 5
    chain_lower = chain_name.lower()
    for key, priority in CHAIN_PRIORITY.items():
        if key in chain_lower:
            return priority
    return 5


def get_member_benefits(chain_name: str, category: str) -> str:
    """会員資格に応じた特典を返す"""
    chain_lower = (chain_name or "").lower()
    benefits = []
    
    if any(k in chain_lower for k in ["marriott", "sheraton", "westin", "w hotel"]):
        benefits.append("Marriottチタン：スイートアップグレード申請・ラウンジ/朝食・ポイント17倍+α")
    elif any(k in chain_lower for k in ["ihg", "intercontinental", "kimpton", "crowne"]):
        benefits.append("IHGダイヤモンド+アンバサダー：ラウンジアクセス・スイートアップグレード・ミニバー等")
    elif any(k in chain_lower for k in ["hyatt", "park hyatt", "grand hyatt", "andaz"]):
        benefits.append("Hyattグローバリスト：スイートアップグレード・午後4時チェックアウト・朝食(一部)")
    elif any(k in chain_lower for k in ["hilton", "waldorf", "conrad", "doubletree"]):
        benefits.append("Hiltonゴールド：朝食（一部ホテル）・ポイント積算・アップグレード申請")
    
    return " / ".join(benefits) if benefits else "ポイント積算（ホテルに要確認）"


def get_fhr_benefits(category: str, special_offer: str) -> str:
    """FHR/THCカテゴリに応じた付帯特典"""
    base = ""
    if category == "FHR":
        base = "✓ 朝食2名分 / ✓ 施設クレジット$100〜$150 / ✓ 客室アップグレード（空室次第） / ✓ アーリーCI/レイトCO"
    elif category == "THC":
        base = "✓ ホテルクレジット$100 / ✓ 客室アップグレード（空室次第）"
    
    if special_offer:
        base = f"★ {special_offer} / {base}"
    
    return base


def calculate_effective_rate(hotel: Dict) -> Tuple[float, float]:
    """特別オファーを考慮した実質料金を計算"""
    nightly = hotel.get("nightly_rate", 0)
    nights = hotel.get("nights", 1)
    total = nightly * nights
    special = (hotel.get("special_offer", "") or "").lower()
    
    effective_total = total
    effective_nightly = nightly
    
    if "3rd night free" in special or "3泊目無料" in special:
        if nights >= 3:
            effective_total = nightly * (nights - nights // 3)
            effective_nightly = effective_total / nights
    elif "4th night free" in special or "4泊目無料" in special:
        if nights >= 4:
            effective_total = nightly * (nights - nights // 4)
            effective_nightly = effective_total / nights
    elif "15% off" in special or "15%オフ" in special:
        effective_total = total * 0.85
        effective_nightly = nightly * 0.85
    elif "10% off" in special or "10%オフ" in special:
        effective_total = total * 0.90
        effective_nightly = nightly * 0.90
    
    return round(effective_nightly, 2), round(effective_total, 2)


def score_plan(plan: List[Dict]) -> float:
    """プランのスコアを計算（高いほど良い）"""
    if not plan:
        return 0
    
    total_cost = sum(h.get("effective_total", h.get("total_rate", 0)) for h in plan)
    total_nights = sum(h.get("nights", 1) for h in plan)
    avg_nightly = total_cost / total_nights if total_nights > 0 else 0
    
    # チェーン優先度スコア (1=最高, 5=最低)
    chain_scores = []
    for h in plan:
        priority = get_chain_priority(h.get("chain", ""))
        chain_scores.append(6 - priority)  # 優先度を逆転（高い数字=良い）
    avg_chain_score = sum(chain_scores) / len(chain_scores)
    
    # エリア変更ペナルティ
    areas = [h.get("area", "") for h in plan]
    area_changes = sum(1 for i in range(1, len(areas)) if areas[i] != areas[i-1])
    
    # オファー特典ボーナス
    offer_bonus = sum(1 for h in plan if h.get("special_offer", ""))
    
    # 特典価値（FHR/THCの付帯特典を金額換算）
    benefit_value = 0
    for h in plan:
        if h.get("category") == "FHR":
            benefit_value += 150 + 100  # 朝食$150 + クレジット$100（概算）
        elif h.get("category") == "THC":
            benefit_value += 100  # クレジット$100（概算）
    
    # スコア計算（100点満点ベース）
    # コスト: 低いほど良い（正規化）
    cost_score = max(0, 100 - avg_nightly / 10)  # $1000/泊で0点
    
    # チェーン: 1〜5点（最大5点×5ホテル=25点 → 20点に正規化）
    chain_score_normalized = (avg_chain_score / 5) * 20
    
    # 移動距離: エリア変更が少ないほど良い
    travel_score = max(0, 20 - area_changes * 5)
    
    # オファー・特典: ボーナス
    offer_score = min(10, offer_bonus * 3 + benefit_value / 50)
    
    total_score = (
        cost_score * 0.5 +        # 50%
        chain_score_normalized * 0.2 +  # 20%
        travel_score * 0.2 +      # 20%
        offer_score * 0.1         # 10%
    )
    
    return total_score


def find_optimal_plan(fhr_hotels: List[Dict], thc_hotels: List[Dict],
                      max_fhr_stays: int = 2, max_thc_stays: int = 2,
                      min_thc_nights: int = 2, top_n: int = 3) -> List[List[Dict]]:
    """
    制約条件を満たす全組み合わせを探索し、上位N件を返す
    
    制約:
    - FHRチェックアウトは最大max_fhr_stays回
    - THCチェックアウトは最大max_thc_stays回
    - THC各滞在はmin_thc_nights泊以上
    """
    valid_plans = []
    
    # FHRの組み合わせ（0〜max_fhr_stays件）
    for n_fhr in range(max_fhr_stays + 1):
        fhr_combinations = list(itertools.combinations(fhr_hotels, min(n_fhr, len(fhr_hotels))))
        
        # THCの組み合わせ（0〜max_thc_stays件、各2泊以上）
        valid_thc = [h for h in thc_hotels if h.get("nights", 1) >= min_thc_nights]
        
        for n_thc in range(max_thc_stays + 1):
            thc_combinations = list(itertools.combinations(valid_thc, min(n_thc, len(valid_thc))))
            
            # FHR+THCの組み合わせ
            for fhr_combo in (fhr_combinations if fhr_combinations else [[]]):
                for thc_combo in (thc_combinations if thc_combinations else [[]]):
                    plan = list(fhr_combo) + list(thc_combo)
                    if not plan:
                        continue
                    
                    # エリアでソート（移動距離最小化）
                    plan_sorted = sorted(plan, key=lambda h: (h.get("area", ""), h.get("check_in", "")))
                    
                    score = score_plan(plan_sorted)
                    valid_plans.append((score, plan_sorted))
    
    # スコア降順でソート
    valid_plans.sort(key=lambda x: x[0], reverse=True)
    
    # 重複除去（同じホテルセットは除外）
    seen = set()
    unique_plans = []
    for score, plan in valid_plans:
        plan_key = frozenset(h.get("hotel_name", "") + h.get("check_in", "") for h in plan)
        if plan_key not in seen:
            seen.add(plan_key)
            unique_plans.append((score, plan))
            if len(unique_plans) >= top_n:
                break
    
    return [plan for _, plan in unique_plans]


def enrich_plan(plan: List[Dict]) -> List[Dict]:
    """プランに詳細情報を追加"""
    enriched = []
    prev_area = None
    
    for i, hotel in enumerate(plan):
        h = hotel.copy()
        
        # 実質料金の計算
        eff_nightly, eff_total = calculate_effective_rate(h)
        h["effective_nightly_rate"] = eff_nightly
        h["effective_total"] = eff_total
        
        # 会員特典の追加
        h["member_benefits"] = get_member_benefits(h.get("chain", ""), h.get("category", ""))
        h["fhr_benefits"] = get_fhr_benefits(h.get("category", ""), h.get("special_offer", ""))
        
        # 移動情報
        current_area = h.get("area", "")
        if i == 0:
            h["travel_from_prev"] = "—（旅行開始）"
        elif prev_area and current_area != prev_area:
            h["travel_from_prev"] = f"{prev_area} → {current_area}"
        else:
            h["travel_from_prev"] = "（同エリア内移動）"
        
        prev_area = current_area
        enriched.append(h)
    
    return enriched


def calculate_total_info(plan: List[Dict]) -> Dict:
    """プランの集計情報を計算"""
    total_cost = sum(h.get("effective_total", h.get("total_rate", 0)) for h in plan)
    total_nights = sum(h.get("nights", 1) for h in plan)
    
    fhr_stays = sum(1 for h in plan if h.get("category") == "FHR")
    thc_stays = sum(1 for h in plan if h.get("category") == "THC")
    
    # 付帯特典価値（概算）
    benefit_value = 0
    for h in plan:
        if h.get("category") == "FHR":
            benefit_value += 150 + 100  # 朝食 + クレジット
        elif h.get("category") == "THC":
            benefit_value += 100  # クレジット
    
    # 特別オファー節約額
    savings = sum(
        h.get("nightly_rate", 0) * h.get("nights", 1) - h.get("effective_total", h.get("total_rate", 0))
        for h in plan
    )
    
    # エリア変更回数
    areas = [h.get("area", "") for h in plan]
    area_changes = sum(1 for i in range(1, len(areas)) if areas[i] != areas[i-1])
    
    return {
        "total_cost": round(total_cost, 2),
        "total_savings": round(max(0, savings), 2),
        "benefit_value": round(benefit_value, 2),
        "net_cost": round(total_cost - benefit_value, 2),
        "total_nights": total_nights,
        "fhr_stays": fhr_stays,
        "thc_stays": thc_stays,
        "area_changes": area_changes,
    }


def main():
    parser = argparse.ArgumentParser(description="Amex Travel Plan Optimizer")
    parser.add_argument("--data", type=str, help="スクレイピングデータJSONファイル")
    parser.add_argument("--nights", type=int, default=7, help="旅行総泊数")
    parser.add_argument("--max-fhr", type=int, default=2, help="FHR最大滞在回数")
    parser.add_argument("--max-thc", type=int, default=2, help="THC最大滞在回数")
    parser.add_argument("--output", type=str, default="optimized_plan.json", help="出力JSONファイル")
    
    args = parser.parse_args()
    
    if args.data:
        with open(args.data, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    else:
        # テスト用サンプルデータ
        raw_data = {
            "fhr": [
                {"hotel_name": "Park Hyatt Tokyo", "chain": "Hyatt", "area": "西新宿",
                 "check_in": "2025-03-05", "check_out": "2025-03-06",
                 "nights": 1, "nightly_rate": 650, "special_offer": "", "category": "FHR"},
                {"hotel_name": "Aman Tokyo", "chain": "Aman", "area": "大手町",
                 "check_in": "2025-03-08", "check_out": "2025-03-11",
                 "nights": 3, "nightly_rate": 1200, "special_offer": "3rd Night Free", "category": "FHR"},
            ],
            "thc": [
                {"hotel_name": "InterContinental Tokyo Bay", "chain": "IHG", "area": "竹芝",
                 "check_in": "2025-03-01", "check_out": "2025-03-03",
                 "nights": 2, "nightly_rate": 320, "special_offer": "", "category": "THC"},
                {"hotel_name": "ANA InterContinental Tokyo", "chain": "IHG", "area": "赤坂",
                 "check_in": "2025-03-03", "check_out": "2025-03-06",
                 "nights": 3, "nightly_rate": 380, "special_offer": "", "category": "THC"},
            ],
        }
    
    fhr_data = raw_data.get("fhr", [])
    thc_data = raw_data.get("thc", [])
    
    print(f"最適化開始: FHR {len(fhr_data)}件、THC {len(thc_data)}件")
    print(f"制約: FHR最大{args.max_fhr}回、THC最大{args.max_thc}回（各2泊以上）")
    
    # 最適化実行
    top_plans = find_optimal_plan(fhr_data, thc_data, args.max_fhr, args.max_thc)
    
    if not top_plans:
        print("有効なプランが見つかりませんでした")
        return
    
    best_plan = enrich_plan(top_plans[0])
    total_info = calculate_total_info(best_plan)
    
    # 結果を表示
    print(f"\n✅ 最適プランが見つかりました（{len(best_plan)}滞在）:")
    for stay in best_plan:
        print(f"  {stay.get('category')} | {stay.get('hotel_name')} | "
              f"{stay.get('check_in')}〜{stay.get('check_out')} | "
              f"${stay.get('effective_nightly_rate', 0):,.0f}/泊")
    
    print(f"\n  総コスト: ${total_info['total_cost']:,.0f}")
    print(f"  節約額: ${total_info['total_savings']:,.0f}")
    print(f"  特典価値: ${total_info['benefit_value']:,.0f}")
    print(f"  実質負担: ${total_info['net_cost']:,.0f}")
    
    # JSONに保存
    result = {
        "plan": best_plan,
        "total_info": total_info,
        "alternative_plans": [enrich_plan(p) for p in top_plans[1:]],
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n  結果を保存: {args.output}")


if __name__ == "__main__":
    main()
