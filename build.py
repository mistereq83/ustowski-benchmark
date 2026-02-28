#!/usr/bin/env python3
"""
Ustowski Build Script
Replaces <!-- INCLUDE:_filename.html --> placeholders in src/ pages
with contents from _partials/ directory. Outputs to root (for deploy).

Usage: python3 build.py
"""
import os
import re
import glob

PARTIALS_DIR = '_partials'
SRC_DIR = 'src'
OUT_DIR = '.'  # root = deploy directory

def load_partial(name):
    path = os.path.join(PARTIALS_DIR, name)
    if not os.path.exists(path):
        print(f"  ⚠️  Partial not found: {path}")
        return f"<!-- MISSING PARTIAL: {name} -->"
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def build_page(src_path, out_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all <!-- INCLUDE:_filename.html --> placeholders
    pattern = r'<!-- INCLUDE:(\S+) -->'
    
    def replacer(match):
        partial_name = match.group(1)
        return load_partial(partial_name)
    
    result = re.sub(pattern, replacer, content)
    
    # Count replacements
    count = len(re.findall(pattern, content))
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    return count

def main():
    if not os.path.exists(SRC_DIR):
        print(f"❌ Source directory '{SRC_DIR}' not found!")
        return
    
    if not os.path.exists(PARTIALS_DIR):
        print(f"❌ Partials directory '{PARTIALS_DIR}' not found!")
        return
    
    # List available partials
    partials = os.listdir(PARTIALS_DIR)
    print(f"📦 Partials: {', '.join(partials)}")
    
    # Build all HTML files from src/
    src_files = glob.glob(os.path.join(SRC_DIR, '*.html'))
    
    if not src_files:
        print(f"❌ No HTML files found in {SRC_DIR}/")
        return
    
    print(f"\n🔨 Building {len(src_files)} pages...\n")
    
    for src_path in sorted(src_files):
        filename = os.path.basename(src_path)
        out_path = os.path.join(OUT_DIR, filename)
        count = build_page(src_path, out_path)
        print(f"  ✅ {filename} ({count} includes)")
    
    print(f"\n🎉 Build complete! {len(src_files)} pages generated.")

if __name__ == '__main__':
    main()
