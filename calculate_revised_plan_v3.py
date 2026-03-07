import pandas as pd
import datetime

# Load data
df = pd.read_csv('/Users/mba2024/Documents/Obsidian/Dai DB/01_OurStory/旅行計画/宿泊料金データベース_日別USD.csv', on_bad_lines='skip')
df['Date'] = pd.to_datetime(df['日付'])
# Clean names
df['Hotel'] = df['ホテル名'].str.strip()
df['Price'] = pd.to_numeric(df['USD_1泊'], errors='coerce')

# Manual override for missing Kimpton dates
# 2026-08-30, 31 are missing. 
# Kimpton avg around 320-330. Set to 325.
def get_price_safe(hotel, date_obj):
    row = df[(df['Hotel'] == hotel) & (df['Date'] == date_obj)]
    if len(row) > 0 and not pd.isna(row.iloc[0]['Price']):
        return float(row.iloc[0]['Price'])
    # Fallback
    if hotel == 'Kimpton Maa-Lai Bangkok':
        return 325.0
    return 0.0

def get_nights_cost(hotel, start_date_str, nights, offer_type=None):
    start = pd.to_datetime(start_date_str)
    cost = 0
    details = []
    
    for i in range(nights):
        d = start + datetime.timedelta(days=i)
        p = get_price_safe(hotel, d)
        
        # Apply daily discount if any (Std BKK 15% off)
        if hotel == 'The Standard Bangkok Mahanakhon' and nights >= 2:
            p = p * 0.85
            
        details.append(p)
        cost += p
        
    # Apply total stay offers (3rd Night Free)
    if offer_type == '3rd_Free' and nights >= 3:
        if len(details) >= 3:
            deduct = details[2]
            cost -= deduct
            
    return cost, details

plan = [
    # BKK Loop
    {'date': '2026-08-23', 'hotel': 'Conrad Bangkok', 'nights': 3, 'program': 'FHR', 'offer': '3rd_Free'},
    {'date': '2026-08-26', 'hotel': 'SO/ Bangkok', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-08-28', 'hotel': 'The Standard Bangkok Mahanakhon', 'nights': 2, 'program': 'THC', 'offer': '15%Off'},
    {'date': '2026-08-30', 'hotel': 'Kimpton Maa-Lai Bangkok', 'nights': 3, 'program': 'FHR', 'offer': '3rd_Free'},
    {'date': '2026-09-02', 'hotel': 'Madi Paidi Bangkok', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-09-04', 'hotel': 'Conrad Bangkok', 'nights': 3, 'program': 'FHR', 'offer': '3rd_Free'},
    {'date': '2026-09-07', 'hotel': 'SO/ Bangkok', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-09-09', 'hotel': 'The Standard Bangkok Mahanakhon', 'nights': 2, 'program': 'THC', 'offer': '15%Off'},
    {'date': '2026-09-11', 'hotel': 'Madi Paidi Bangkok', 'nights': 2, 'program': 'THC', 'offer': None},
    
    # Hua Hin Loop
    {'date': '2026-09-13', 'hotel': 'The Standard Hua Hin', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-09-15', 'hotel': 'InterContinental Hua Hin Resort', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-09-17', 'hotel': 'The Standard Hua Hin', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-09-19', 'hotel': 'InterContinental Hua Hin Resort', 'nights': 2, 'program': 'THC', 'offer': None},
    
    # Final Night in BKK (Kimpton)
    {'date': '2026-09-21', 'hotel': 'Kimpton Maa-Lai Bangkok', 'nights': 1, 'program': 'FHR', 'offer': None}
]

total_usd = 0
csv_rows = []

for p in plan:
    c, d_list = get_nights_cost(p['hotel'], p['date'], p['nights'], p['offer'])
    total_usd += c
    
    # Note formatting
    note = f"{p['program']} {p['nights']}泊"
    if p['offer'] == '3rd_Free':
        note += " (3泊目無料)"
    if p['offer'] == '15%Off':
        note += " (15%OFF)"
    
    # Date range string
    end_date = pd.to_datetime(p['date']) + datetime.timedelta(days=p['nights'])
    date_range = f"{pd.to_datetime(p['date']).strftime('%-m/%-d')}〜{end_date.strftime('%-m/%-d')}"
    
    # Perks
    perks = "クレジット"
    if p['program'] == 'FHR':
        perks += ", 朝食無料"
    
    # Combine Note + Perks
    full_note = f"{note}, {perks}"
    
    csv_rows.append(f"{date_range},{p['hotel']},{p['program']},{p['nights']},{c:.2f},{full_note}")

print("日付,ホテル,プラン,泊数,料金(USD),備考・特典")
for r in csv_rows:
    print(r)
print(f"合計,,,{30},{total_usd:.2f},約{total_usd*153:,.0f}円 (1USD=153円), クレジット総額,400付与")

