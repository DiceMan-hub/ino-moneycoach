#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML to Markdown Converter for JRE POINT Strategy Guide
Converts HTML content to Markdown format with frontmatter
"""

import re
from html.parser import HTMLParser
from html import unescape
from datetime import datetime

class HTMLToMarkdownConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.markdown = []
        self.current_tag = None
        self.current_text = []
        self.in_code = False
        self.in_pre = False
        self.list_stack = []
        self.table_data = []
        self.table_headers = []
        self.in_table = False
        self.in_thead = False
        self.in_tbody = False
        self.table_row = []
        self.in_details = False
        self.in_summary = False
        self.details_content = []
        self.details_title = ""
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'h2':
            self._flush_text()
            self.markdown.append('\n## ')
        elif tag == 'h3':
            self._flush_text()
            self.markdown.append('\n### ')
        elif tag == 'h4':
            self._flush_text()
            self.markdown.append('\n#### ')
        elif tag == 'p':
            self._flush_text()
        elif tag == 'strong':
            self._flush_text()
            self.markdown.append('**')
        elif tag == 'em':
            self._flush_text()
            self.markdown.append('*')
        elif tag == 'a':
            self._flush_text()
            href = attrs_dict.get('href', '')
            self.markdown.append('[')
            self.current_tag = 'a'
        elif tag == 'ul':
            self._flush_text()
            self.list_stack.append('ul')
        elif tag == 'ol':
            self._flush_text()
            self.list_stack.append('ol')
        elif tag == 'li':
            self._flush_text()
            if self.list_stack and self.list_stack[-1] == 'ol':
                self.markdown.append('\n1. ')
            else:
                self.markdown.append('\n- ')
        elif tag == 'br':
            self._flush_text()
            self.markdown.append('\n')
        elif tag == 'code':
            self._flush_text()
            self.markdown.append('`')
            self.in_code = True
        elif tag == 'pre':
            self._flush_text()
            self.in_pre = True
            self.markdown.append('\n```\n')
        elif tag == 'table':
            self._flush_text()
            self.in_table = True
            self.table_headers = []
            self.table_data = []
        elif tag == 'thead':
            self.in_thead = True
        elif tag == 'tbody':
            self.in_tbody = True
        elif tag == 'tr':
            self.table_row = []
        elif tag == 'th':
            self.current_tag = 'th'
        elif tag == 'td':
            self.current_tag = 'td'
        elif tag == 'details':
            self._flush_text()
            self.in_details = True
            self.details_content = []
            self.details_title = ""
        elif tag == 'summary':
            self.in_summary = True
        elif tag in ['div', 'section', 'article', 'main', 'body', 'html', 'head', 'meta', 'title', 'style', 'script', 'nav', 'header', 'footer']:
            # Skip these tags but continue processing
            pass
        elif tag == 'span':
            # Just continue, don't add anything
            pass
        
        self.current_tag = tag
        
    def handle_endtag(self, tag):
        if tag == 'h2' or tag == 'h3' or tag == 'h4':
            self._flush_text()
            self.markdown.append('\n')
        elif tag == 'p':
            self._flush_text()
            self.markdown.append('\n\n')
        elif tag == 'strong':
            self._flush_text()
            self.markdown.append('**')
        elif tag == 'em':
            self._flush_text()
            self.markdown.append('*')
        elif tag == 'a':
            self._flush_text()
            self.markdown.append(']')
            self.current_tag = None
        elif tag == 'ul' or tag == 'ol':
            self._flush_text()
            if self.list_stack:
                self.list_stack.pop()
            self.markdown.append('\n')
        elif tag == 'code':
            self._flush_text()
            self.markdown.append('`')
            self.in_code = False
        elif tag == 'pre':
            self._flush_text()
            self.markdown.append('\n```\n')
            self.in_pre = False
        elif tag == 'table':
            self._flush_text()
            self._write_table()
            self.in_table = False
            self.in_thead = False
            self.in_tbody = False
        elif tag == 'thead':
            self.in_thead = False
        elif tag == 'tbody':
            self.in_tbody = False
        elif tag == 'tr':
            if self.table_row:
                self.table_data.append(self.table_row)
                self.table_row = []
        elif tag == 'th' or tag == 'td':
            self.current_tag = None
        elif tag == 'details':
            self._flush_text()
            # Convert details to regular section
            if self.details_title:
                self.markdown.append(f'\n#### {self.details_title}\n\n')
            self.markdown.extend(self.details_content)
            self.in_details = False
            self.details_content = []
            self.details_title = ""
        elif tag == 'summary':
            self._flush_text()
            self.in_summary = False
        
        self.current_tag = None
        
    def handle_data(self, data):
        data = data.strip()
        if not data:
            return
            
        if self.in_summary:
            # Extract title from summary
            self.details_title = data
            return
            
        if self.in_details and not self.in_summary:
            # Collect content inside details
            self.details_content.append(data + '\n\n')
            return
            
        if self.current_tag == 'th' or self.current_tag == 'td':
            # Clean table cell data
            cell_data = re.sub(r'\s+', ' ', data).strip()
            self.table_row.append(cell_data)
            return
            
        if self.in_code or self.in_pre:
            self.markdown.append(data)
        else:
            self.current_text.append(data)
            
    def _flush_text(self):
        if self.current_text:
            text = ' '.join(self.current_text)
            text = re.sub(r'\s+', ' ', text).strip()
            if text:
                self.markdown.append(text)
            self.current_text = []
            
    def _write_table(self):
        if not self.table_headers and not self.table_data:
            return
            
        # Find headers (first row if no thead)
        if self.table_headers:
            headers = self.table_headers
        elif self.table_data:
            headers = self.table_data[0]
            self.table_data = self.table_data[1:]
        else:
            return
            
        # Write table
        self.markdown.append('\n')
        # Header row
        self.markdown.append('| ' + ' | '.join(headers) + ' |\n')
        # Separator
        self.markdown.append('| ' + ' | '.join(['---'] * len(headers)) + ' |\n')
        # Data rows
        for row in self.table_data:
            if len(row) == len(headers):
                self.markdown.append('| ' + ' | '.join(row) + ' |\n')
        self.markdown.append('\n')
        
    def get_markdown(self):
        self._flush_text()
        return ''.join(self.markdown)


def extract_meta_from_html(html_content):
    """Extract metadata from HTML"""
    meta = {}
    
    # Title
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
    if title_match:
        meta['title'] = title_match.group(1).strip()
    
    # Description
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', html_content)
    if desc_match:
        meta['description'] = desc_match.group(1).strip()
    
    # Keywords
    keywords_match = re.search(r'<meta\s+name="keywords"\s+content="(.*?)"', html_content)
    if keywords_match:
        meta['keywords'] = keywords_match.group(1).strip()
    
    # Date
    date_match = re.search(r'"datePublished":\s*"(.*?)"', html_content)
    if date_match:
        meta['date'] = date_match.group(1) + 'T10:00:00+09:00'
    else:
        meta['date'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00')
    
    return meta


def convert_html_to_markdown(html_file_path, output_file_path):
    """Convert HTML file to Markdown with frontmatter"""
    
    # Read HTML file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract metadata
    meta = extract_meta_from_html(html_content)
    
    # Extract main content (between <main> tags or <body>)
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
    if main_match:
        main_content = main_match.group(1)
    else:
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
        if body_match:
            main_content = body_match.group(1)
        else:
            main_content = html_content
    
    # Remove script and style tags
    main_content = re.sub(r'<script[^>]*>.*?</script>', '', main_content, flags=re.DOTALL)
    main_content = re.sub(r'<style[^>]*>.*?</style>', '', main_content, flags=re.DOTALL)
    
    # Convert special elements
    # Convert formula divs to code blocks
    main_content = re.sub(
        r'<div\s+class="formula"[^>]*>(.*?)</div>',
        r'\n```\n\1\n```\n',
        main_content,
        flags=re.DOTALL
    )
    
    # Convert formula-note to blockquote
    main_content = re.sub(
        r'<p[^>]*class="formula-note"[^>]*>(.*?)</p>',
        r'\n> \1\n',
        main_content,
        flags=re.DOTALL
    )
    
    # Convert card divs to regular content (remove wrapper)
    main_content = re.sub(r'<div[^>]*class="card[^"]*"[^>]*>', '', main_content)
    main_content = re.sub(r'</div>', '', main_content)
    
    # Convert CTA buttons to markdown links
    main_content = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*class="cta-button"[^>]*>(.*?)</a>',
        r'\n\n[**\2**](\1)\n\n',
        main_content,
        flags=re.DOTALL
    )
    
    # Parse HTML to Markdown
    parser = HTMLToMarkdownConverter()
    parser.feed(main_content)
    markdown_content = parser.get_markdown()
    
    # Clean up markdown
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    markdown_content = re.sub(r' +', ' ', markdown_content)
    
    # Create frontmatter
    frontmatter = f"""---
id: "jre-point-strategy-guide"
title: "{meta.get('title', 'JRE POINT活用戦略：価値最大化とビューカード徹底比較ガイド')}"
date: "{meta.get('date', datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00'))}"
type: "guide"
tags: {meta.get('keywords', 'JRE POINT,ビューカード,還元率,ポイント戦略,Suica,VIEWプラス,ゴールドカード,JRE CARD').split(',')}
platforms: ["blog", "github_pages"]
slug: "jre-point-strategy"
summary: "{meta.get('description', 'JRE POINTの価値最大化とビューカード徹底比較ガイド。1ポイントの価値を最大5.83円まで引き出す戦略を解説。')}"
author: "ino"
---

"""
    
    # Combine frontmatter and content
    full_markdown = frontmatter + markdown_content
    
    # Write to file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(full_markdown)
    
    print(f"✅ Converted {html_file_path} to {output_file_path}")
    print(f"   Frontmatter created with {len(meta)} metadata fields")
    print(f"   Markdown content: {len(markdown_content)} characters")


if __name__ == '__main__':
    html_file = '/Users/mba2024/Documents/Obsidian/Dai DB/docs/jre-point-strategy/index.html'
    output_file = '/Users/mba2024/Documents/Obsidian/Dai DB/content/guides/jre-point-strategy.md'
    convert_html_to_markdown(html_file, output_file)

