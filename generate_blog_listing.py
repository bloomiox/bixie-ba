import os, re, json
from datetime import datetime

SITE_DIR = "/root/bixie-site"
POSTS_DIR = os.path.join(SITE_DIR, "blog/posts")

months_bs = {
    1: 'Januar', 2: 'Februar', 3: 'Mart', 4: 'April',
    5: 'Maj', 6: 'Juni', 7: 'Juli', 8: 'Avgust',
    9: 'Septembar', 10: 'Oktobar', 11: 'Novembar', 12: 'Decembar'
}

# Category/tag mapping for filter
CAT_TAG_MAP = {
    'CRM': 'CRM',
    'AI Agenti': 'AI',
    'AI Tehnologija': 'AI',
    'Automatizacija': 'RPA',
    'Marketing': 'AI',
    'Prodaja': 'AI',
    'Case Study': 'Case Studies',
    'Vodiči': 'AI',
    'Trendovi': 'AI',
    'Customer Support': 'AI',
}

def slug_to_tag_display(cat):
    m = {
        'CRM': 'CRM',
        'AI Agenti': 'AI Agenti',
        'AI Tehnologija': 'AI Tehnologija',
        'Automatizacija': 'Automatizacija',
        'Marketing': 'Marketing',
        'Prodaja': 'Prodaja',
        'Case Study': 'Case Study',
        'Vodiči': 'Vodiči',
        'Trendovi': 'Trendovi',
        'Customer Support': 'Customer Support',
    }
    return m.get(cat, cat)

def parse_frontmatter(content):
    fm = {}
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            for line in content[3:end].strip().split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm

def format_date_bs(d):
    parts = d.split('-')
    if len(parts) == 3:
        return f"{int(parts[2])}. {months_bs.get(int(parts[1]), parts[1])} {parts[0]}"
    return d

posts = []
for slug in sorted(os.listdir(POSTS_DIR)):
    idx = os.path.join(POSTS_DIR, slug, 'index.html')
    md = os.path.join('/root/bixie-blog-posts/posts', f'{slug}.md')
    
    # Try reading from markdown source
    if os.path.exists(md):
        with open(md) as f:
            fm = parse_frontmatter(f.read())
        
        title = fm.get('title', slug.replace('-',' ').title())
        desc = fm.get('description', '')
        cat = fm.get('category', '')
        date = fm.get('date', '2026-01-01')
        date_display = format_date_bs(date)
        
        # Short description for blog card
        short_desc = desc[:100] + '...' if len(desc) > 100 else desc
        
        filter_tag = CAT_TAG_MAP.get(cat, 'AI')
        display_cat = slug_to_tag_display(cat)
        
        posts.append((date, slug, title, short_desc, date_display, filter_tag, display_cat))

# Sort by date descending (newest first)
posts.sort(key=lambda x: x[0], reverse=True)

# Generate blog cards HTML
cards_html = ''
for date, slug, title, short_desc, date_display, filter_tag, display_cat in posts:
    cards_html += f'''<a href="/blog/posts/{slug}" class="blog-card" data-tag="{filter_tag}"><span class="tag tag-teal" style="border-color:rgba(94,106,210,0.3);color:#00736a">{display_cat}</span><h2>{title}</h2><p>{short_desc}</p><div class="meta">{date_display}</div></a>
'''

print(f"Generated {len(posts)} blog cards")

# Read current blog/index.html
blog_index = os.path.join(SITE_DIR, 'blog', 'index.html')
with open(blog_index) as f:
    content = f.read()

# Find blog-grid section and replace
start = content.find('<div class="blog-grid">')
end = content.find('</div>', start)
end = content.find('</section>', end)

if start != -1:
    new_content = content[:start] + f'<div class="blog-grid">\n{cards_html}</div>\n' + content[end:]
    with open(blog_index, 'w') as f:
        f.write(new_content)
    print("✅ Blog listing page updated")
else:
    print("❌ Could not find blog-grid section")
