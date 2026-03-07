import pandas as pd
import datetime

df = pd.read_csv('/Users/mba2024/Documents/Obsidian/Dai DB/01_OurStory/旅行計画/宿泊料金データベース_日別USD.csv', on_bad_lines='skip')
df['Date'] = pd.to_datetime(df['日付']).dt.strftime('%Y-%m-%d')
# Clean names
df['Hotel'] = df['ホテル名'].str.strip()
df['Price'] = pd.to_numeric(df['USD_1泊'], errors='coerce')

def get_price(hotel, date_str):
    row = df[(df['Hotel'] == hotel) & (df['Date'] == date_str)]
    if len(row) > 0:
        return float(row.iloc[0]['Price'])
    return 0.0

total = 0

# 1. Conrad FHR (Aug 1)
p = get_price('Conrad Bangkok', '2026-08-01')
print(f"Aug 1: Conrad - {p}")
total += p

# 2. SO/ Regular (Aug 2)
p = get_price('SO/ Bangkok', '2026-08-02')
print(f"Aug 2: SO/ - {p}")
total += p

# 3. Conrad Reg (Aug 3-15)
sub = 0
for i in range(3, 16):
    d = f"2026-08-{i:02d}"
    v = get_price('Conrad Bangkok', d)
    sub += v
print(f"Aug 3-15: Conrad - {sub}")
total += sub

# 4. Std HH Reg (Aug 16-30)
sub = 0
for i in range(16, 31):
    d = f"2026-08-{i:02d}"
    v = get_price('The Standard Hua Hin', d)
    sub += v
print(f"Aug 16-30: Std HH - {sub}")
total += sub

print(f"Total: {total}")
