import pandas as pd
import datetime

# Load data
df = pd.read_csv('/Users/mba2024/Documents/Obsidian/Dai DB/01_OurStory/旅行計画/宿泊料金データベース_日別USD.csv', on_bad_lines='skip')
df['Date'] = pd.to_datetime(df['日付'])
# Clean names
df['Hotel'] = df['ホテル名'].str.strip()
df['Price'] = pd.to_numeric(df['USD_1泊'], errors='coerce')

def get_nights_cost(hotel, start_date_str, nights, offer_type=None):
    start = pd.to_datetime(start_date_str)
    cost = 0
    details = []
    
    for i in range(nights):
        d = start + datetime.timedelta(days=i)
        d_str = d.strftime('%Y-%m-%d')
        row = df[(df['Hotel'] == hotel) & (df['Date'] == d)]
        if len(row) > 0:
            price = float(row.iloc[0]['Price'])
        else:
            price = 0 # Error
        
        # Apply daily discount if any (Std BKK 15% off)
        if hotel == 'The Standard Bangkok Mahanakhon' and nights >= 2:
            price = price * 0.85
            
        details.append(price)
        cost += price
        
    # Apply total stay offers (3rd Night Free)
    if offer_type == '3rd_Free' and nights >= 3:
        # Subtract the 3rd night cost? Or average?
        # Typically "Pay for 2 nights". Usually the cheapest or last night is free.
        # Assuming last night free for simplicity, or average adjustment.
        # Let's subtract the 3rd night price (index 2).
        if len(details) >= 3:
            deduct = details[2]
            cost -= deduct
            
    return cost, details

plan = [
    # BKK Loop 1
    {'date': '2026-08-01', 'hotel': 'Conrad Bangkok', 'nights': 3, 'program': 'FHR', 'offer': None},
    {'date': '2026-08-04', 'hotel': 'SO/ Bangkok', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-08-06', 'hotel': 'The Standard Bangkok Mahanakhon', 'nights': 2, 'program': 'THC', 'offer': '15%Off'},
    {'date': '2026-08-08', 'hotel': 'Kimpton Maa-Lai Bangkok', 'nights': 3, 'program': 'FHR', 'offer': '3rd_Free'},
    {'date': '2026-08-11', 'hotel': 'Madi Paidi Bangkok', 'nights': 2, 'program': 'THC', 'offer': None},
    
    # BKK Loop 2
    {'date': '2026-08-13', 'hotel': 'Conrad Bangkok', 'nights': 3, 'program': 'FHR', 'offer': None},
    {'date': '2026-08-16', 'hotel': 'SO/ Bangkok', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-08-18', 'hotel': 'The Standard Bangkok Mahanakhon', 'nights': 2, 'program': 'THC', 'offer': '15%Off'},
    {'date': '2026-08-20', 'hotel': 'Kimpton Maa-Lai Bangkok', 'nights': 3, 'program': 'FHR', 'offer': '3rd_Free'},
    
    # Hua Hin
    {'date': '2026-08-23', 'hotel': 'The Standard Hua Hin', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-08-25', 'hotel': 'InterContinental Hua Hin Resort', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-08-27', 'hotel': 'The Standard Hua Hin', 'nights': 2, 'program': 'THC', 'offer': None},
    {'date': '2026-08-29', 'hotel': 'InterContinental Hua Hin Resort', 'nights': 2, 'program': 'THC', 'offer': None}
]

total_usd = 0
csv_rows = []

for p in plan:
    c, d_list = get_nights_cost(p['hotel'], p['date'], p['nights'], p['offer'])
    total_usd += c
    
    # Format details
    note = f"{p['program']} {p['nights']}泊"
    if p['offer'] == '3rd_Free':
        note += " (3泊目無料)"
    if p['offer'] == '15%Off':
        note += " (15%OFF適用)"
    
    # Check consecutive
    end_date = pd.to_datetime(p['date']) + datetime.timedelta(days=p['nights']-1)
    date_range = f"{pd.to_datetime(p['date']).strftime('%Y/%-m/%-d')}〜{end_date.strftime('%-m/%-d')}"
    
    csv_rows.append(f"{date_range},{p['hotel']},{p['program']},{p['nights']},{c:.2f},{note}")

print("日付,ホテル,プラン,泊数,料金(USD),備考")
for r in csv_rows:
    print(r)
print(f"合計,,,{30},{total_usd:.2f},1USD=153円換算 約{total_usd*153:,.0f}円")

