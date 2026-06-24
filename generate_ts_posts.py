#!/usr/bin/env python3
"""Generate TypeScript blog post entries for bloomiox/bixie-ba."""

import os, re, glob

POSTS_DIR = "/root/bloomiox-bixie/src/blog"
MARKS_DIR = "/root/bixie-blog-posts/posts"
OUTPUT_FILE = os.path.join(POSTS_DIR, "posts_new.ts")
EXISTING_FILE = os.path.join(POSTS_DIR, "posts.ts")

# Read existing file up to the closing };
with open(EXISTING_FILE, 'r') as f:
    existing = f.read()

# Parse markdown frontmatter
def parse_md(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    fm = {}
    body = content
    
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            for line in content[3:end].strip().split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
            body = content[end+3:].strip()
    
    # Remove CTA line at the end
    if '---' in body:
        body = body.split('---')[0].strip()
    
    return fm, body

def md_body_to_html(body):
    """Convert markdown body to inline HTML"""
    lines = body.split('\n')
    html_parts = []
    in_list = None
    
    for line in lines:
        s = line.strip()
        if not s:
            if in_list:
                html_parts.append(f'</{in_list}>')
                in_list = None
            continue
        
        # Strip bold markers for processing
        # Headings
        if s.startswith('## '):
            text = s[3:]
            html_parts.append(f'<h2>{text}</h2>')
            continue
        if s.startswith('### '):
            text = s[4:]
            html_parts.append(f'<h3>{text}</h3>')
            continue
        
        # Unordered list
        if s.startswith('- '):
            if in_list != 'ul':
                if in_list: html_parts.append(f'</{in_list}>')
                in_list = 'ul'
                html_parts.append('<ul>')
            item = s[2:]
            item = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item)
            html_parts.append(f'<li>{item}</li>')
            continue
        
        # Ordered list
        if re.match(r'^\d+\.\s', s):
            if in_list != 'ol':
                if in_list: html_parts.append(f'</{in_list}>')
                in_list = 'ol'
                html_parts.append('<ol>')
            item = re.sub(r'^\d+\.\s+', '', s)
            item = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item)
            html_parts.append(f'<li>{item}</li>')
            continue
        
        # Regular paragraph
        text = s
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        html_parts.append(f'<p>{text}</p>')
    
    if in_list:
        html_parts.append(f'</{in_list}>')
    
    return '\n'.join(html_parts)

def estimate_read_time(body):
    words = len(body.split())
    return max(3, round(words / 200))

# Build new entries
new_entries = []

for fname in sorted(os.listdir(MARKS_DIR)):
    if not fname.endswith('.md'):
        continue
    
    slug = fname.replace('.md', '')
    filepath = os.path.join(MARKS_DIR, fname)
    fm, body = parse_md(filepath)
    
    title = fm.get('title', slug.replace('-', ' ').title())
    desc = fm.get('description', '')
    desc_short = desc[:120] if len(desc) > 120 else desc
    cat = fm.get('category', 'BIXIE')
    date = fm.get('date', '2026-07-01')
    rt = estimate_read_time(body)
    
    # Convert body to HTML
    html = md_body_to_html(body)
    # Escape backticks and backslashes for TS template literal
    html = html.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    
    entry = f"""  '{slug}': {{
    slug: '{slug}',
    title: '{title}',
    excerpt: '{desc_short}',
    category: '{cat}',
    date: '{date}',
    readTime: '{rt} min',
    content: `
{html}`,
  }},"""
    new_entries.append(entry)

# Insert before closing };
insert_point = existing.rfind('};')
new_content = existing[:insert_point] + '\n' + '\n'.join(new_entries) + '\n' + existing[insert_point:]

with open(OUTPUT_FILE, 'w') as f:
    f.write(new_content)

print(f"✅ Generated {len(new_entries)} new entries")
print(f"File: {OUTPUT_FILE}")
print(f"Size: {os.path.getsize(OUTPUT_FILE):,} bytes")
