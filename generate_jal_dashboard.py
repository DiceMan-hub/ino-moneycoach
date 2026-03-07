import csv
import json
import os

csv_path = '/Users/mba2024/Documents/Obsidian/Dai DB/00_Projects/JAL/JALカード/JAL_Card_Special_Stores_DoubleMiles_List.csv'
output_path = '/Users/mba2024/Documents/Obsidian/Dai DB/00_Projects/JAL/JALカード/JAL_Card_Dashboard.html'

data = []
categories = set()

if os.path.exists(csv_path):
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)

        for row in reader:
            store_name = row.get('Store Name', '').strip()
            orig_category = row.get('Category', '').strip()
            
            final_cat = orig_category
            
            # Smart categorization logic
            if not orig_category or 'レストラン' in orig_category or orig_category == '':
                final_cat = 'レストラン・その他'
                
                # Check keywords
                name_lower = store_name.lower()
                if any(x in store_name for x in ['鮨', '寿司', '割烹', '和食', 'そば', 'うどん', '天ぷら', '懐石', 'とんかつ', '海鮮', 'ふぐ', 'かに', '鰻', 'うなぎ']):
                    final_cat = '和食'
                elif any(x in store_name for x in ['焼肉', 'ステーキ', '鉄板', '肉', 'ジンギスカン', 'しゃぶしゃぶ', 'すき焼き', '牛たん']):
                    final_cat = '肉料理'
                elif any(x in store_name for x in ['イタリア', 'フレンチ', 'ビストロ', '洋食', 'カレー', 'ピザ', 'パスタ', 'スパゲッティ', 'オムライス']):
                    final_cat = '洋食'
                elif any(x in store_name for x in ['中華', '餃子', 'ラーメン', '担々麺', '四川', '広東']):
                    final_cat = '中華'
                elif any(x in store_name for x in ['居酒屋', '酒場', 'バル', 'ダイニング', 'バー', 'Bar', '焼き鳥', '焼鳥', '串焼き']):
                    final_cat = '居酒屋・Bar'
                elif any(x in store_name for x in ['カフェ', '喫茶', 'スイーツ', 'ケーキ', 'パン', '珈琲', 'Tea']):
                    final_cat = 'カフェ・スイーツ'
            
            if store_name:
                data.append({
                    'name': store_name,
                    'category': final_cat
                })
                if final_cat:
                    categories.add(final_cat)

categories = sorted(list(categories))
json_data = json.dumps(data, ensure_ascii=False)
json_categories = json.dumps(categories, ensure_ascii=False)

html_content = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>JAL Card Special Stores</title>
    <style>
        :root {{
            --primary-color: #000000;
            --accent-color: #D30000; /* JAL Red */
            --bg-color: #F2F2F7; /* Apple System Gray 6 */
            --card-bg: #FFFFFF;
            --text-primary: #1C1C1E;
            --text-secondary: #8E8E93;
            --divider: #E5E5EA;
            --search-bg: #E3E3E8;
            --shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
            --safe-area-top: env(safe-area-inset-top);
        }}

        * {{
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}

        header {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: calc(var(--safe-area-top) + 12px) 20px 12px;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 0.5px solid rgba(0,0,0,0.1);
        }}

        .header-content {{
            max-width: 700px;
            margin: 0 auto;
            position: relative;
        }}

        header h1 {{
            margin: 0;
            font-size: 22px;
            font-weight: 700;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        header .subtitle {{
            font-size: 13px;
            color: var(--text-secondary);
            font-weight: 400;
            margin-top: 2px;
        }}

        .container {{
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
        }}

        /* Search Bar (iOS Style) */
        .search-wrapper {{
            position: relative;
            margin-bottom: 20px;
        }}

        .search-box {{
            width: 100%;
            padding: 12px 16px 12px 40px;
            font-size: 17px;
            border: none;
            border-radius: 12px;
            background: var(--search-bg);
            color: var(--text-primary);
            outline: none;
            transition: background 0.2s;
        }}

        .search-box:focus {{
            background: #FFFFFF;
            box-shadow: 0 0 0 4px rgba(0,0,0,0.05);
        }}

        .search-icon {{
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: #8E8E93;
            width: 18px;
            height: 18px;
        }}

        /* Segmented Control (Tabs) */
        .segmented-control {{
            display: flex;
            background: #E3E3E8;
            border-radius: 9px;
            padding: 2px;
            margin-bottom: 24px;
        }}

        .segment-btn {{
            flex: 1;
            padding: 6px 12px;
            font-size: 13px;
            font-weight: 600;
            text-align: center;
            border-radius: 7px;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.1, 0.7, 1.0, 0.1);
            color: var(--text-primary);
            border: 0.5px solid transparent; /* Prevents layout shift */
        }}

        .segment-btn.active {{
            background: #FFFFFF;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 0 0 0.5px rgba(0,0,0,0.04);
        }}

        /* Filter Chips (Apple Tags) */
        .filter-scroll-area {{
            overflow-x: auto;
            white-space: nowrap;
            padding-bottom: 4px; /* Space for scrollbar hide */
            -webkit-overflow-scrolling: touch;
            margin: 0 -20px 20px -20px; /* Bleed out */
            padding-left: 20px;
            padding-right: 20px;
            display: flex;
            gap: 8px;
        }}

        .filter-scroll-area::-webkit-scrollbar {{
            display: none;
        }}

        .chip {{
            padding: 8px 16px;
            background: #FFFFFF;
            border-radius: 100px;
            font-size: 14px;
            font-weight: 500;
            color: var(--text-primary);
            border: 1px solid rgba(0,0,0,0.05);
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }}

        .chip.active {{
            background: var(--text-primary);
            color: #FFFFFF;
            border-color: transparent;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}

        /* Card List */
        .results-list {{
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .store-card {{
            background: var(--card-bg);
            border-radius: 18px; /* Smooth corners */
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.03); /* Very subtle shadow */
            position: relative;
            transform: translateZ(0); /* Hardware accel */
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .store-card:active {{
            transform: scale(0.98);
        }}

        @media (hover: hover) {{
            .store-card:hover {{
                transform: translateY(-2px);
                box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            }}
        }}

        .store-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 6px;
        }}

        .store-name {{
            font-size: 17px;
            font-weight: 600;
            color: var(--text-primary);
            padding-right: 32px;
            line-height: 1.3;
        }}

        .category-pill {{
            font-size: 11px;
            font-weight: 600;
            color: #8E8E93;
            background: #F2F2F7;
            padding: 4px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-bottom: 8px;
        }}

        .badge-miles {{
            display: inline-flex;
            align-items: center;
            font-size: 12px;
            font-weight: 700;
            color: var(--accent-color);
            background: rgba(211, 0, 0, 0.05);
            padding: 6px 12px;
            border-radius: 8px;
        }}
        
        .badge-miles::before {{
            content: '';
            display: inline-block;
            width: 6px;
            height: 6px;
            background-color: var(--accent-color);
            border-radius: 50%;
            margin-right: 6px;
        }}

        /* Favorite Button (Heart) */
        .fav-btn {{
            position: absolute;
            top: 20px;
            right: 20px;
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            background: #F2F2F7;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .fav-btn svg {{
            width: 16px;
            height: 16px;
            fill: #C7C7CC;
            transition: fill 0.2s;
        }}

        .fav-btn.active svg {{
            fill: #FF2D55; /* Apple Red/Pink for Favorites */
        }}
        
        .fav-btn.active {{
            background: #FFEDF0;
        }}

        /* Empty State */
        .no-results {{
            text-align: center;
            padding: 60px 20px;
            color: var(--text-secondary);
        }}

        .scroll-top-btn {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: rgba(255,255,255,0.9);
            backdrop-filter: blur(10px);
            border-radius: 50%;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 900;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s;
            border: 1px solid rgba(0,0,0,0.05);
        }}

        .scroll-top-btn.visible {{
            opacity: 1;
            transform: translateY(0);
        }}

        .scroll-top-btn svg {{
            width: 24px;
            height: 24px;
            fill: var(--text-primary);
        }}
        
        /* Stats */
        .stats-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            font-size: 13px;
            color: var(--text-secondary);
            font-weight: 500;
            padding: 0 4px;
        }}

        #sentinel {{
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            font-size: 13px;
        }}
        
    </style>
</head>
<body>

    <header>
        <div class="header-content">
            <h1>
                JAL Card
                <span id="favCountBadge" style="font-size: 14px; background:var(--accent-color); color:white; padding: 2px 10px; border-radius:12px; font-weight:600; display:none;">Fav</span>
            </h1>
            <div class="subtitle">プレミアム・パートナーズ (特約店)</div>
        </div>
    </header>

    <div class="container">
        
        <div class="search-wrapper">
            <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path fill-rule="evenodd" d="M10.5 3.75a6.75 6.75 0 100 13.5 6.75 6.75 0 000-13.5zM2.25 10.5a8.25 8.25 0 1114.59 5.28l4.69 4.69a.75.75 0 11-1.06 1.06l-4.69-4.69A8.25 8.25 0 012.25 10.5z" clip-rule="evenodd" />
            </svg>
            <input type="text" id="searchInput" class="search-box" placeholder="店舗名、カテゴリーで検索">
        </div>

        <div class="segmented-control">
            <div class="segment-btn active" id="tabAll" onclick="switchTab('all')">すべての店舗</div>
            <div class="segment-btn" id="tabFav" onclick="switchTab('fav')">お気に入り</div>
        </div>

        <div class="filter-scroll-area" id="categoryChips">
            <div class="chip active" data-category="all" onclick="setCategory('all')">すべて</div>
            <!-- Dynamic Chips -->
        </div>

        <div class="stats-bar">
            <span id="statsCount">Loading...</span>
        </div>

        <div class="results-list" id="resultsList">
            <!-- Cards -->
        </div>

        <div id="sentinel">読み込み中...</div>
    </div>

    <!-- Scroll Top Button -->
    <div class="scroll-top-btn" id="scrollTopBtn" onclick="scrollToTop()">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path fill-rule="evenodd" d="M11.47 2.47a.75.75 0 011.06 0l7.5 7.5a.75.75 0 11-1.06 1.06l-6.22-6.22V21a.75.75 0 01-1.5 0V4.81l-6.22 6.22a.75.75 0 11-1.06-1.06l7.5-7.5z" clip-rule="evenodd" />
        </svg>
    </div>

<script>
    const stores = {json_data};
    const categories = {json_categories};

    // State
    let currentCategory = 'all';
    let currentSearch = '';
    let filteredStores = [];
    let displayedCount = 0;
    let currentTab = 'all';
    let favorites = JSON.parse(localStorage.getItem('jal_favs') || '[]');
    const CHUNK_SIZE = 40; 

    // Elements
    const searchInput = document.getElementById('searchInput');
    const categoryChipsContainer = document.getElementById('categoryChips');
    const resultsList = document.getElementById('resultsList');
    const statsCount = document.getElementById('statsCount');
    const sentinel = document.getElementById('sentinel');
    const scrollTopBtn = document.getElementById('scrollTopBtn');

    // Update Fav Badge visibility
    function updateFavCount() {{
        // Simple logic: could be improved
    }}

    function toggleFavorite(name, event) {{
        event.stopPropagation();
        const index = favorites.indexOf(name);
        if (index === -1) {{
            favorites.push(name);
        }} else {{
            favorites.splice(index, 1);
        }}
        localStorage.setItem('jal_favs', JSON.stringify(favorites));
        
        // Update UI immediately for better feel
        const btn = event.currentTarget;
        btn.classList.toggle('active');
        
        // Refresh if in Fav mode (delayed slightly)
        if (currentTab === 'fav') {{
            setTimeout(applyFilters, 150);
        }}
    }}

    function switchTab(tab) {{
        currentTab = tab;
        document.getElementById('tabAll').classList.toggle('active', tab === 'all');
        document.getElementById('tabFav').classList.toggle('active', tab === 'fav');
        
        // Scroll to top when switching
        window.scrollTo({{top: 0, behavior: 'smooth'}});
        applyFilters();
    }}

    function scrollToTop() {{
        window.scrollTo({{top: 0, behavior: 'smooth'}});
    }}

    // Scroll Observer for Top Button
    window.addEventListener('scroll', () => {{
        if (window.scrollY > 300) {{
            scrollTopBtn.classList.add('visible');
        }} else {{
            scrollTopBtn.classList.remove('visible');
        }}
    }});

    // Initialize Categories
    categories.forEach(cat => {{
        const chip = document.createElement('div');
        chip.className = 'chip';
        chip.textContent = cat;
        chip.dataset.category = cat;
        chip.onclick = () => setCategory(cat);
        categoryChipsContainer.appendChild(chip);
    }});

    function setCategory(cat) {{
        currentCategory = cat;
        document.querySelectorAll('.chip').forEach(c => {{
            c.classList.toggle('active', c.dataset.category === cat);
        }});
        // Center the active chip in scroll view
        const activeChip = document.querySelector(`.chip[data-category="${{cat}}"]`);
        if(activeChip) {{
            activeChip.scrollIntoView({{ behavior: 'smooth', block: 'nearest', inline: 'center' }});
        }}
        applyFilters();
    }}

    searchInput.addEventListener('input', (e) => {{
        currentSearch = e.target.value.toLowerCase();
        applyFilters();
    }});

    function applyFilters() {{
        filteredStores = stores.filter(store => {{
            if (currentTab === 'fav' && !favorites.includes(store.name)) return false;

            const matchesCategory = currentCategory === 'all' || store.category === currentCategory;
            const matchesSearch = store.name.toLowerCase().includes(currentSearch) || 
                                  store.category.toLowerCase().includes(currentSearch);
            return matchesCategory && matchesSearch;
        }});

        statsCount.textContent = `${{filteredStores.length}} Stores`;

        resultsList.innerHTML = '';
        displayedCount = 0;
        
        if (filteredStores.length === 0) {{
            resultsList.innerHTML = `
                <div class="no-results">
                    <h3>No Stores Found</h3>
                    <p>検索条件を変更してください</p>
                </div>`;
            sentinel.style.display = 'none';
        }} else {{
            sentinel.style.display = 'flex';
            sentinel.textContent = '読み込み中...';
            loadMore();
        }}
    }}

    function loadMore() {{
        if (displayedCount >= filteredStores.length) {{
            sentinel.textContent = 'すべて表示しました';
            return;
        }}

        const nextBatch = filteredStores.slice(displayedCount, displayedCount + CHUNK_SIZE);
        const fragment = document.createDocumentFragment();

        nextBatch.forEach(store => {{
            const div = document.createElement('div');
            const isFav = favorites.includes(store.name) ? 'active' : '';
            
            div.className = 'store-card';
            div.innerHTML = `
                <div class="fav-btn ${{isFav}}" onclick="toggleFavorite('${{store.name}}', event)">
                    <svg viewBox="0 0 24 24">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                    </svg>
                </div>
                <div class="store-header">
                    <div class="store-name">${{store.name}}</div>
                </div>
                <div class="category-pill">${{store.category}}</div>
                <br>
                <div class="badge-miles">マイル2倍</div>
            `;
            fragment.appendChild(div);
        }});

        resultsList.appendChild(fragment);
        displayedCount += nextBatch.length;
        
        if (displayedCount >= filteredStores.length) {{
            sentinel.textContent = 'すべて表示しました';
        }}
    }}

    // Intersection Observer
    const observer = new IntersectionObserver(entries => {{
        if (entries[0].isIntersecting) {{
            loadMore();
        }}
    }}, {{ rootMargin: '400px' }});

    observer.observe(sentinel);

    // Initial load
    applyFilters();

</script>
</body>
</html>
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated JAL Dashboard (Apple Design) at: {output_path}")
