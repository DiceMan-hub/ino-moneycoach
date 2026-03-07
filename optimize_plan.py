import pandas as pd
import datetime

# Load CSV
df = pd.read_csv('/Users/mba2024/Documents/Obsidian/Dai DB/01_OurStory/旅行計画/宿泊料金データベース_日別USD.csv', on_bad_lines='skip')
# Clean up columns just in case
df.columns = [c.strip() for c in df.columns]

# Helper to parse price
def parse_price(x):
    try:
        return float(x)
    except:
        return None

df['Price'] = df['USD_1泊'].apply(parse_price)
df['Date'] = pd.to_datetime(df['日付'])
df = df.dropna(subset=['Price', 'Date'])

# Filter Data (Aug - Sep 2026)
start_aug = pd.to_datetime('2026-08-01')
end_sep = pd.to_datetime('2026-09-30')

# Get hotel list
hotels = df['ホテル名'].unique()
avg_aug = {}
avg_sep = {}

# Calculate avg for Aug and Sep
for h in hotels:
    d_aug = df[(df['ホテル名'] == h) & (df['Date'] >= start_aug) & (df['Date'] <  pd.to_datetime('2026-09-01'))]
    d_sep = df[(df['ホテル名'] == h) & (df['Date'] >= pd.to_datetime('2026-09-01')) & (df['Date'] <= end_sep)]
    
    if len(d_aug) > 0: avg_aug[h] = d_aug['Price'].mean()
    if len(d_sep) > 0: avg_sep[h] = d_sep['Price'].mean()

print("--- Aug vs Sep Averages ---")
for h in hotels:
    p_aug = avg_aug.get(h, float('inf'))
    p_sep = avg_sep.get(h, float('inf'))
    print(f"{h}: Aug={p_aug:.1f}, Sep={p_sep:.1f}")

