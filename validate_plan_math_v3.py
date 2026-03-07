import pandas as pd
import datetime

# Load data
try:
    df = pd.read_csv('/Users/mba2024/Documents/Obsidian/Dai DB/01_OurStory/旅行計画/宿泊料金データベース_日別USD.csv', on_bad_lines='skip')
    df['Date'] = pd.to_datetime(df['日付'], errors='coerce')
    df['Hotel'] = df['ホテル名'].str.strip()
    df['Price'] = pd.to_numeric(df['USD_1泊'], errors='coerce')
except Exception as e:
    print(f"Error loading CSV: {e}")
    exit(1)

def get_price(hotel, date_obj):
    row = df[(df['Hotel'] == hotel) & (df['Date'] == date_obj)]
    if len(row) > 0 and not pd.isna(row.iloc[0]['Price']):
        return float(row.iloc[0]['Price'])
    # Fallback
    if 'Kimpton' in hotel:
        return 325.0
    return 0.0

def calculate_stay(hotel_name, start_input, n_nights, prog, offer_code):
    start_d = pd.to_datetime(start_input)
    daily_rates = []
    
    for i in range(n_nights):
        cur_d = start_d + datetime.timedelta(days=i)
        p = get_price(hotel_name, cur_d)
        daily_rates.append(p)
        
    base_sum = sum(daily_rates)
    final_sum = 0
    note = ""
    
    if offer_code == '3rd_Free' and n_nights >= 3:
        if len(daily_rates) >= 3:
            discount = daily_rates[2]
            final_sum = base_sum - discount
            note = f"3泊目(${discount:.0f})無料"
        else:
            final_sum = base_sum
    elif offer_code == '15%Off' and n_nights >= 2:
        d_rates = [r * 0.85 for r in daily_rates]
        final_sum = sum(d_rates)
        note = "全日15%OFF"
    else:
        final_sum = base_sum
        note = "-"
        
    return {
        'hotel': hotel_name,
        'start': start_input,
        'nights': n_nights,
        'program': prog,
        'base': base_sum,
        'final': final_sum,
        'rates': daily_rates,
        'note': note
    }

# The Plan List
plan_list = [
    # (Date, Hotel, Nights, Program, Offer)
    ('2026-08-23', 'Conrad Bangkok', 3, 'FHR', '3rd_Free'),
    ('2026-08-26', 'SO/ Bangkok', 2, 'THC', None),
    ('2026-08-28', 'The Standard Bangkok Mahanakhon', 2, 'THC', '15%Off'),
    ('2026-08-30', 'Kimpton Maa-Lai Bangkok', 3, 'FHR', '3rd_Free'),
    ('2026-09-02', 'Madi Paidi Bangkok', 2, 'THC', None),
    ('2026-09-04', 'Conrad Bangkok', 3, 'FHR', '3rd_Free'),
    ('2026-09-07', 'SO/ Bangkok', 2, 'THC', None),
    ('2026-09-09', 'The Standard Bangkok Mahanakhon', 2, 'THC', '15%Off'),
    ('2026-09-11', 'Madi Paidi Bangkok', 2, 'THC', None),
    ('2026-09-13', 'The Standard Hua Hin', 2, 'THC', None),
    ('2026-09-15', 'InterContinental Hua Hin Resort', 2, 'THC', None),
    ('2026-09-17', 'The Standard Hua Hin', 2, 'THC', None),
    ('2026-09-19', 'InterContinental Hua Hin Resort', 2, 'THC', None),
    ('2026-09-21', 'Kimpton Maa-Lai Bangkok', 1, 'FHR', None)
]

grand_total = 0
csv_lines = []

print(f"{'Date':<10} {'Hotel':<15} {'BaseRates':<20} {'Total':<10} {'Note':<15}")
print("-" * 100)

for p in plan_list:
    res = calculate_stay(p[1], p[0], p[2], p[3], p[4])
    grand_total += res['final']
    
    rates_str = "/".join([f"{x:.0f}" for x in res['rates']])
    print(f"{p[0][5:]:<10} {res['hotel'][:15]:<15} {rates_str:<20} {res['final']:<10.2f} {res['note']:<25}")
    
    end_d = pd.to_datetime(p[0]) + datetime.timedelta(days=p[2])
    range_s = f"{pd.to_datetime(p[0]).strftime('%-m/%-d')}〜{end_d.strftime('%-m/%-d')}"
    
    perks = "$100クレジット"
    if res['program'] == 'FHR': perks += ",朝食無料"
    
    note_detail = f"{res['program']} {res['nights']}泊"
    if "無料" in res['note']:
         note_detail += f" ({res['note']})"
    elif "OFF" in res['note']:
         note_detail += f" ({res['note']})"
    
    full_note = f"{note_detail}, {perks}"
    csv_lines.append(f"{range_s},{res['hotel']},{res['program']},{res['nights']},{res['final']:.2f},{full_note}")

print("-" * 100)
print(f"Grand Total: {grand_total:.2f}")

with open('/Users/mba2024/Documents/Obsidian/Dai DB/01_OurStory/旅行計画/宿泊料金データベース_最適プラン.csv', 'w') as f:
    f.write("日付,ホテル,プラン,泊数,料金(USD),特典・備考\n")
    for l in csv_lines:
        f.write(l + "\n")
    f.write(f"合計,,,30,{grand_total:.2f},約{grand_total*153:,.0f}円 ($1=153円), クレジット$1,400付与\n")
