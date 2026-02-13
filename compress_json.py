"""
Compress gss_data.json to gss_data.json.gz

This makes the file much smaller for GitHub upload.
Run this in the same folder as your gss_data.json file.
"""

import gzip
import json

print("Compressing gss_data.json...")

try:
    # Read the JSON file
    with open('gss_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Write compressed version
    with gzip.open('gss_data.json.gz', 'wt', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'))  # Compact format
    
    import os
    original_size = os.path.getsize('gss_data.json') / (1024 * 1024)
    compressed_size = os.path.getsize('gss_data.json.gz') / (1024 * 1024)
    
    print(f"✓ Compression complete!")
    print(f"  Original:   {original_size:.2f} MB")
    print(f"  Compressed: {compressed_size:.2f} MB")
    print(f"  Saved:      {original_size - compressed_size:.2f} MB ({(1 - compressed_size/original_size)*100:.1f}% reduction)")
    print(f"\nUpload gss_data.json.gz to GitHub!")
    
except FileNotFoundError:
    print("ERROR: gss_data.json not found in this directory")
except Exception as e:
    print(f"ERROR: {e}")
