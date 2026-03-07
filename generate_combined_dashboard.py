import csv
import json
import os

jal_csv_path = '/Users/mba2024/Documents/Obsidian/Dai DB/00_Projects/JAL/JALカード/JAL_Card_Special_Stores_DoubleMiles_List.csv'
ana_csv_path = '/Users/mba2024/Documents/Obsidian/Dai DB/00_Projects/ANA/ANAカード/ANA_Card_Special_Stores_List.csv'
output_path = '/Users/mba2024/Documents/Obsidian/Dai DB/00_Projects/JAL/JALカード/Combined_Card_Dashboard.html'

data = []
categories = set()

# Process JAL Data
if os.path.exists(jal_csv_path):
    with open(jal_csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            store_name = row.get('Store Name', '').strip()
            category = row.get('Category', '').strip()
            
            if store_name:
                data.append({
                    'name': store_name,
                    'category': category,
                    'program': 'JAL',
                    'rate': '100円=2マイル' # Default heavily implied for this list
                })
                if category:
                    categories.add(category)

# Process ANA Data
if os.path.exists(ana_csv_path):
    with open(ana_csv_path, 'r', encoding='utf-8') as f: # standard utf-8 for this file based on previous interaction
        reader = csv.DictReader(f)
        for row in reader:
            store_name = row.get('Store Name', '').strip()
            category = row.get('Category', '').strip()
            rate = row.get('Mile Rate', '').strip()
            desc = row.get('Description', '').strip()

            # Normalize category names if needed, or just add them
            if store_name:
                data.append({
                    'name': store_name,
                    'category': category,
                    'program': 'ANA',
                    'rate': rate,
                    'description': desc
                })
                if category:
                    categories.add(category)

categories = sorted(list(categories))
json_data = json.dumps(data, ensure_ascii=False)
json_categories = json.dumps(categories, ensure_ascii=False)

html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JAL & ANA 特約店比較ダッシュボード</title>
    <style>
        :root {{
            --jal-red: #D30000;
            --ana-blue: #003e7e;
            --ana-cyan: #00A0E9;
            --bg-color: #f4f6f9;
            --card-bg: rgba(255, 255, 255, 0.95);
            --text-color: #333;
            --glass-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }}

        header {{
            background: linear-gradient(135deg, #2c3e50, #4b6cb7);
            color: white;
            padding: 2rem 1rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        header h1 {{
            margin: 0;
            font-size: 2rem;
            font-weight: 700;
        }}

        header p {{
            margin-top: 0.5rem;
            opacity: 0.9;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}

        /* Controls */
        .controls {{
            background: white;
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }}

        .search-box {{
            width: 100%;
            padding: 1rem;
            font-size: 1.1rem;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            transition: border-color 0.3s;
            box-sizing: border-box;
        }}

        .search-box:focus {{
            outline: none;
            border-color: #4b6cb7;
        }}

        .filter-group {{
            margin-bottom: 1rem;
        }}
        
        .filter-label {{
            font-weight: bold;
            margin-bottom: 0.5rem;
            display: block;
            font-size: 0.9rem;
            color: #666;
        }}

        .filter-chips {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .chip {{
            padding: 0.5rem 1rem;
            background-color: #f0f0f0;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.2s;
            font-size: 0.85rem;
            user-select: none;
            border: 1px solid transparent;
        }}

        .chip:hover {{
            background-color: #e0e0e0;
        }}

        /* Program Filter Styles */
        .chip.program-jal.active {{
            background-color: var(--jal-red);
            color: white;
        }}
        .chip.program-ana.active {{
            background-color: var(--ana-blue);
            color: white;
        }}
        .chip.program-all.active {{
            background-color: #555;
            color: white;
        }}

        /* Category Filter Styles */
        .chip.cat-chip.active {{
            background-color: #4b6cb7;
            color: white;
        }}

        /* Results Grid */
        .results-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }}

        .store-card {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border-top: 5px solid #ccc;
            position: relative;
            overflow: hidden;
        }}

        .store-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }}

        .store-card.jal {{ border-top-color: var(--jal-red); }}
        .store-card.ana {{ border-top-color: var(--ana-blue); }}

        .program-badge {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            font-size: 0.75rem;
            font-weight: bold;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            color: white;
        }}
        
        .jal .program-badge {{ background-color: var(--jal-red); }}
        .ana .program-badge {{ background-color: var(--ana-blue); }}

        .store-name {{
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            padding-right: 3rem; /* space for badge */
            color: var(--text-color);
        }}

        .store-meta {{
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 0.8rem;
        }}

        .store-desc {{
            font-size: 0.85rem;
            color: #555;
            flex-grow: 1;
            margin-bottom: 1rem;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        .rate-info {{
            background-color: #f8f9fa;
            padding: 0.5rem;
            border-radius: 6px;
            font-size: 0.85rem;
            text-align: center;
            font-weight: 600;
            color: #444;
        }}

        .no-results {{
            text-align: center;
            grid-column: 1 / -1;
            padding: 3rem;
            color: #888;
        }}

        .stats {{
            text-align: right;
            margin-bottom: 1rem;
            font-size: 0.9rem;
            color: #666;
        }}
    </style>
</head>
<body>

<header>
    <h1>JAL & ANA Special Stores</h1>
    <p>どちらのカードがお得か一目でわかる比較ダッシュボード</p>
</header>

<div class="container">
    <div class="controls">
        <input type="text" id="searchInput" class="search-box" placeholder="店舗名、特徴、カテゴリーで検索...">
        
        <div class="filter-group">
            <span class="filter-label">カード会社:</span>
            <div class="filter-chips">
                <div class="chip program-all active" onclick="setProgram('all')">すべて</div>
                <div class="chip program-jal" onclick="setProgram('JAL')">JALカード (DOUBLE MILE)</div>
                <div class="chip program-ana" onclick="setProgram('ANA')">ANAカード (MILE PLUS)</div>
            </div>
        </div>

        <div class="filter-group">
            <span class="filter-label">カテゴリー:</span>
            <div class="filter-chips" id="categoryChips">
                <div class="chip cat-chip active" data-category="all" onclick="setCategory('all')">すべて</div>
                <!-- Categories injected here -->
            </div>
        </div>
    </div>

    <div class="stats" id="statsDisplay">
        読み込み中...
    </div>

    <div class="results-grid" id="resultsGrid">
        <!-- Cards injected here -->
    </div>
</div>

<script>
    const stores = {json_data};
    const categories = {json_categories};

    const searchInput = document.getElementById('searchInput');
    const categoryChipsContainer = document.getElementById('categoryChips');
    const resultsGrid = document.getElementById('resultsGrid');
    const statsDisplay = document.getElementById('statsDisplay');

    let currentCategory = 'all';
    let currentProgram = 'all';
    let currentSearch = '';

    // Initialize Category Chips
    // Limit to top categories or commonly used ones to avoid clutter if too many
    categories.forEach(cat => {{
        const chip = document.createElement('div');
        chip.className = 'chip cat-chip';
        chip.textContent = cat;
        chip.dataset.category = cat;
        chip.onclick = () => setCategory(cat);
        categoryChipsContainer.appendChild(chip);
    }});

    function setCategory(cat) {{
        currentCategory = cat;
        document.querySelectorAll('.cat-chip').forEach(c => {{
            c.classList.toggle('active', c.dataset.category === cat);
        }});
        render();
    }}

    function setProgram(prog) {{
        currentProgram = prog;
        const allChip = document.querySelector('.program-all');
        const jalChip = document.querySelector('.program-jal');
        const anaChip = document.querySelector('.program-ana');

        allChip.classList.remove('active');
        jalChip.classList.remove('active');
        anaChip.classList.remove('active');

        if (prog === 'all') allChip.classList.add('active');
        if (prog === 'JAL') jalChip.classList.add('active');
        if (prog === 'ANA') anaChip.classList.add('active');
        
        render();
    }}

    searchInput.addEventListener('input', (e) => {{
        currentSearch = e.target.value.toLowerCase();
        render();
    }});

    function render() {{
        resultsGrid.innerHTML = '';
        
        const filtered = stores.filter(store => {{
            const matchesCategory = currentCategory === 'all' || store.category === currentCategory;
            const matchesProgram = currentProgram === 'all' || store.program === currentProgram;
            const matchesSearch = store.name.toLowerCase().includes(currentSearch) || 
                                  store.category.toLowerCase().includes(currentSearch) ||
                                  (store.description && store.description.toLowerCase().includes(currentSearch));
            return matchesCategory && matchesProgram && matchesSearch;
        }});

        statsDisplay.textContent = `表示中: ${{filtered.length}}件 / 全 ${{stores.length}}件`;

        if (filtered.length === 0) {{
            resultsGrid.innerHTML = '<div class="no-results">条件に一致する店舗が見つかりませんでした</div>';
            return;
        }}

        const displayLimit = 200; // Increased limit
        const toShow = filtered.slice(0, displayLimit);

        toShow.forEach(store => {{
            const card = document.createElement('div');
            card.className = `store-card ${{store.program.toLowerCase()}}`;
            
            // Clean up description if missing
            const desc = store.description ? store.description : (store.program === 'JAL' ? '特約店: マイル2倍' : '-');

            card.innerHTML = `
                <div>
                    <span class="program-badge">${{store.program}}</span>
                    <div class="store-name">${{store.name}}</div>
                    <div class="store-meta">${{store.category}}</div>
                    <div class="store-desc">${{desc}}</div>
                </div>
                <div class="rate-info">
                    ${{store.rate}}
                </div>
            `;
            resultsGrid.appendChild(card);
        }});

        if (filtered.length > displayLimit) {{
            const more = document.createElement('div');
            more.className = 'no-results';
            more.style.padding = '1rem';
            more.textContent = `他 ${{filtered.length - displayLimit}}件... (さらに絞り込んでください)`;
            resultsGrid.appendChild(more);
        }}
    }}

    render();

</script>

</body>
</html>
"""

# Write to file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Created Combined Dashboard at: {output_path}")
