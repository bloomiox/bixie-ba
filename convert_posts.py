#!/usr/bin/env python3
"""Convert BIXIE markdown blog posts to HTML and push to GitHub repo."""

import os, re, json, subprocess, sys

MARKDOWN_DIR = "/root/bixie-blog-posts/posts"
SITE_DIR = "/root/bixie-site/blog/posts"

# HTML template parts extracted from existing blog post
HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="bs">
<head>
    <meta charset="UTF-8">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — BIXIE</title>
<meta property="og:title" content="{title} — BIXIE">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://bixie.ba/blog/posts/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BIXIE">
<meta property="og:image" content="https://bixie.ba/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — BIXIE">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="https://bixie.ba/og-image.png">
    <meta name="description" content="{description}" />
  <link rel="canonical" href="https://bixie.ba/blog/posts/{slug}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BIXIE",
  "url": "https://bixie.ba",
  "logo": "https://bixie.ba/og-image.png",
  "description": "CRM, AI Agenti i Digitalna Transformacija za firme u Bosni i Hercegovini.",
  "address": {{ "@type": "PostalAddress", "streetAddress": "Maglajska 1", "addressLocality": "Sarajevo", "addressCountry": "BA" }},
  "contactPoint": {{ "@type": "ContactPoint", "telephone": "+387-33-922-622", "email": "hello@bixie.ba", "contactType": "sales" }},
  "sameAs": ["https://www.linkedin.com/company/bixie"]
}}
</script>
<link rel="alternate" hreflang="en" href="https://bixie.ba/en/blog/posts/{slug}">
<link rel="alternate" hreflang="de" href="https://bixie.ba/de/blog/posts/{slug}">
<link rel="alternate" hreflang="bs" href="https://bixie.ba/blog/posts/{slug}">
<link rel="alternate" hreflang="x-default" href="https://bixie.ba/blog/posts/{slug}"><!-- Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
        c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "jhp3l0sl3y");
</script>
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-WRGFE5K9G4"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag("js", new Date());
  gtag("config", "G-WRGFE5K9G4");
</script>
<link rel="stylesheet" href="/style.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
.hamburger{{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px}}
.hamburger span{{display:block;width:22px;height:2px;background:#5b6f99;border-radius:1px;transition:all .2s}}
.mobile-menu{{display:none;border-top:1px solid rgba(30,41,59,0.4);padding:16px 24px 24px;background:var(--bg-root)}}
@media(max-width:768px){{.hamburger{{display:flex}}.nav-links{{display:none}}.mobile-menu.open{{display:block}}}}
</style>
</head>
<body><nav>
<div class="nav-inner">
<a href="/" class="logo"><img src="/images/logo/bixie-logo.png" alt="BIXIE" style="height:36px"></a>
<div class="nav-links">
<div class="dropdown"><a href="/services/crm">CRM</a><div class="dropdown-menu"><a href="/services/crm">Pregled CRM usluga</a><a href="/services/crm#bitrix24">Bitrix24</a><a href="/services/crm#zoho">Zoho CRM</a><a href="/services/crm#monday">Monday.com</a><a href="/services/crm#salesforce">Salesforce</a><a href="/services/crm#pipedrive">Pipedrive</a><a href="/services/crm#twenty">Twenty CRM</a><a href="/services/crm#hubspot">HubSpot</a></div></div>
<div class="dropdown"><a href="/services/ai-agents">AI</a><div class="dropdown-menu"><a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-agents#implementacija">AI Implementacija</a><a href="/services/ai-agents#licence">AI Licence</a></div></div>
<div class="dropdown"><a href="/services/digital-transformation">Digitalna Transformacija</a><div class="dropdown-menu"><a href="/services/digital-transformation">Pregled</a><a href="/services/rpa">RPA i Automatizacija</a></div></div>
<a href="/about">O nama</a>
<a href="/ai-providers">AI Licence</a>
<a href="/blog">Blog</a>
<a href="/contact" class="nav-cta">Zatražite ponudu</a>
</div>
<button class="hamburger" onclick="toggleMobile()"><span></span><span></span><span></span></button>
</div>
<div id="mobileMenu" class="mobile-menu">
<div class="mobile-label">CRM</div>
<a href="/services/crm">Pregled CRM usluga</a><a href="/services/crm#bitrix24">Bitrix24</a><a href="/services/crm#zoho">Zoho CRM</a><a href="/services/crm#monday">Monday.com</a><a href="/services/crm#salesforce">Salesforce</a><a href="/services/crm#pipedrive">Pipedrive</a><a href="/services/crm#twenty">Twenty CRM</a><a href="/services/crm#hubspot">HubSpot</a>
<div class="mobile-label">AI</div>
<a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-agents#implementacija">AI Implementacija</a><a href="/services/ai-agents#licence">AI Licence</a>
<a href="/services/digital-transformation">Digitalna Transformacija</a><a href="/services/rpa">RPA i Automatizacija</a>
<a href="/about">O nama</a>
<a href="/ai-providers">AI Licence</a><a href="/blog">Blog</a>
<a href="/contact" style="display:block;margin-top:10px;background:#00736a;color:#fff;padding:10px 16px;border-radius:6px;text-align:center;font-weight:450;font-size:0.9rem">Zatražite ponudu</a>
</div>
</nav>
<section class="max-w-3xl mx-auto px-4 py-12">
<a href="/blog" class="text-gray-500 hover:text-white text-sm mb-6 inline-block">← Nazad na blog</a>
<span class="badge bg-green-600/20 text-green-400 mb-4 inline-block">{category}</span>
<h1>{title}</h1>
<div class="text-sm text-gray-500 mb-8">{date} · BIXIE Team · {read_time} min čitanja</div>
{BODY}
</section>
<footer>
<div class="footer-inner">
<div><a href="/" style="display:flex;align-items:center;gap:10px;text-decoration:none;font-size:16px;font-weight:600;color:#f3f4f6;margin-bottom:14px"><img src="/images/logo/bixie-logo.png" alt="BIXIE" style="height:28px"></a><p style="font-size:14px;color:#6b7280;line-height:1.6">CRM, AI Agenti i Digitalna Transformacija za vasu firmu.</p></div>
<div><h4>Usluge</h4><a href="/services/crm">CRM Rjesenja</a><br><a href="/services/ai-agents">AI Agenti</a><br><a href="/services/digital-transformation">Digitalna Transformacija</a><br><a href="/services/rpa">RPA i Automatizacija</a><br><a href="/ai-providers">AI Provajderi i Licence</a></div>
<div><h4>Kompanija</h4><a href="/blog">Blog</a><br><a href="/about">O nama</a><br><a href="/contact">Kontakt</a><br><a href="/privacy">Privacy Policy</a></div>
<div><h4>Kontakt</h4><p>hello@bixie.ba</p><p>033 922 622</p><p>Maglajska 1, 71000 Sarajevo</p></div>
</div>
<div class="footer-bottom">2026 BIXIE. All rights reserved.</div>
</footer>
<script>
function toggleMobile() {{
  var m = document.getElementById("mobileMenu");
  m.classList.toggle("open");
}}
</script>
</body>
</html>'''

def md_to_html(md_text):
    """Convert markdown-style content to HTML matching BIXIE's format."""
    lines = md_text.split('\n')
    html_parts = []
    in_list = None
    in_table = False
    table_rows = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip empty lines unless in table
        if not stripped and not in_table:
            if in_list:
                if in_list == 'ul':
                    html_parts.append('</ul>')
                else:
                    html_parts.append('</ol>')
                in_list = None
            i += 1
            continue
        
        # HR
        if stripped == '---' and not in_table:
            i += 1
            continue
        
        # Code blocks
        if stripped.startswith('```'):
            lang = stripped[3:].strip()
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            code = '\n'.join(code_lines)
            html_parts.append(f'<pre><code>{code}</code></pre>')
            i += 1
            continue
        
        # Tables
        if '|' in stripped and '---' not in stripped and stripped.startswith('|'):
            in_table = True
            # Parse table row
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if not table_rows:  # header
                table_rows.append(('<thead><tr>', '</tr></thead>'))
                html_parts.append('<div class="card mb-6"><table class="w-full text-sm text-gray-300">')
                html_parts.append(f'<tr class="text-left text-white border-b border-gray-700">' + ''.join(f'<th class="pb-3 pr-4">{c}</th>' for c in cells) + '</tr>')
            else:
                html_parts.append(f'<tr class="border-b border-gray-800">' + ''.join(f'<td class="py-3 pr-4">{c}</td>' for c in cells) + '</tr>')
            i += 1
            # Check if next line is also a table row
            continue
        
        if in_table and (not stripped or '|' not in stripped):
            html_parts.append('</tbody></table></div>')
            in_table = False
            table_rows = []
        
        # Headings
        if stripped.startswith('# ') or stripped.startswith('## ') or stripped.startswith('### '):
            level = stripped.count('#')
            text = stripped.strip('# ')
            html_parts.append(f'<h{level+1} class="text-{"3xl" if level == 1 else "2xl"} font-bold text-white mt-10 mb-4">{text}</h{level+1}>')
            i += 1
            continue
        
        # Bold + paragraph (description line)
        if stripped.startswith('**') and stripped.endswith('**') and len(stripped) > 4:
            text = stripped.strip('*')
            html_parts.append(f'<p class="text-gray-300 mb-4"><strong>{text}</strong></p>')
            i += 1
            continue
        
        # Unordered list
        if stripped.startswith('- **') or stripped.startswith('- '):
            if in_list != 'ul':
                if in_list:
                    html_parts.append(f'</{in_list}>')
                html_parts.append('<ul class="list-disc list-inside text-gray-300 mb-6 space-y-2">')
                in_list = 'ul'
            item_text = stripped.lstrip('- ')
            if '**' in item_text:
                # Bold in list
                item_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item_text)
            html_parts.append(f'<li>{item_text}</li>')
            i += 1
            continue
        
        # Ordered list
        if re.match(r'^\d+\.\s', stripped):
            if in_list != 'ol':
                if in_list:
                    html_parts.append(f'</{in_list}>')
                html_parts.append('<ol class="list-decimal list-inside text-gray-300 mb-6 space-y-3">')
                in_list = 'ol'
            item_text = re.sub(r'^\d+\.\s+', '', stripped)
            if '**' in item_text:
                item_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item_text)
            html_parts.append(f'<li>{item_text}</li>')
            i += 1
            continue
        
        # Bold + paragraph
        if '**' in stripped:
            processed = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', stripped)
            html_parts.append(f'<p class="text-gray-300 mb-4">{processed}</p>')
            i += 1
            continue
        
        # Regular paragraph
        if stripped and not in_table:
            html_parts.append(f'<p class="text-gray-300 mb-4">{stripped}</p>')
            i += 1
            continue
        
        i += 1
    
    if in_list:
        html_parts.append(f'</{in_list}>')
    if in_table:
        html_parts.append('</tbody></table></div>')
    
    return '\n'.join(html_parts)


def parse_md_frontmatter(content):
    """Parse frontmatter from markdown file."""
    fm = {}
    body = content
    
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            fm_text = content[3:end].strip()
            body = content[end+3:].strip()
            for line in fm_text.split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    fm[key] = val
    
    return fm, body

def format_date_bs(date_str):
    """Convert YYYY-MM-DD to BS format like '15. Juni 2026'"""
    months_bs = {
        '01': 'Januar', '02': 'Februar', '03': 'Mart', '04': 'April',
        '05': 'Maj', '06': 'Juni', '07': 'Juli', '08': 'Avgust',
        '09': 'Septembar', '10': 'Oktobar', '11': 'Novembar', '12': 'Decembar'
    }
    parts = date_str.split('-')
    if len(parts) == 3:
        return f"{int(parts[2])}. {months_bs.get(parts[1], parts[1])} {parts[0]}"
    return date_str


def process_posts():
    md_files = sorted([f for f in os.listdir(MARKDOWN_DIR) if f.endswith('.md')])
    print(f"Found {len(md_files)} markdown files")
    
    for fname in md_files:
        slug = fname.replace('.md', '')
        filepath = os.path.join(MARKDOWN_DIR, fname)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        fm, body = parse_md_frontmatter(content)
        
        title = fm.get('title', slug.replace('-', ' ').title())
        description = fm.get('description', '')
        category = fm.get('category', 'BIXIE')
        date = fm.get('date', '2026-07-01')
        
        # Format date for display
        date_display = format_date_bs(date)
        
        # Estimate read time from body
        word_count = len(body.split())
        read_time = max(3, round(word_count / 150))
        
        # Convert body to HTML
        body_html = md_to_html(body)
        
        # Create directory
        post_dir = os.path.join(SITE_DIR, slug)
        os.makedirs(post_dir, exist_ok=True)
        dest_file = os.path.join(post_dir, 'index.html')
        
        # Write HTML
        full_html = HEADER_TEMPLATE.format(
            title=title,
            description=description.replace('"', "'"),
            slug=slug,
            category=category,
            date=date_display,
            read_time=read_time,
            BODY=body_html
        )
        
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"✓ {slug} ({read_time} min, {len(body_html)} chars)")
    
    print(f"\n✅ Total: {len(md_files)} posts converted")

if __name__ == '__main__':
    process_posts()
