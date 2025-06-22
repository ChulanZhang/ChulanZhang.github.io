#!/usr/bin/env python3
"""
Script to add authors field to publication markdown files.
This script extracts author information from citation field and adds it as a separate authors field.
"""

import os
import re
import yaml
import glob
from pathlib import Path

def extract_authors_from_citation(citation):
    """Extract authors from citation string."""
    # Try to extract from BibTeX format
    bibtex_match = re.search(r'author\s*=\s*\{([^}]+)\}', citation)
    if bibtex_match:
        return bibtex_match.group(1)
    
    # Try to extract from regular citation format
    # Look for pattern like "Author1, Author2, and Author3. (Year)"
    citation_match = re.search(r'^([^(]+)\.\s*\(', citation)
    if citation_match:
        return citation_match.group(1).strip()
    
    return None

def process_publication_file(file_path):
    """Process a single publication file to add authors field."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if authors field already exists
    if 'authors:' in content:
        print(f"Skipping {file_path}: authors field already exists")
        return False
    
    # Extract front matter
    front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
    if not front_matter_match:
        print(f"Skipping {file_path}: no front matter found")
        return False
    
    try:
        front_matter = yaml.safe_load(front_matter_match.group(1))
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {file_path}: {e}")
        return False
    
    # Check if citation exists
    if 'citation' not in front_matter:
        print(f"Skipping {file_path}: no citation field found")
        return False
    
    # Extract authors from citation
    authors = extract_authors_from_citation(front_matter['citation'])
    if not authors:
        print(f"Skipping {file_path}: could not extract authors from citation")
        return False
    
    # Add authors field to front matter
    front_matter['authors'] = authors
    
    # Reconstruct the file content
    new_front_matter = yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)
    
    # Replace the old front matter with new one
    new_content = content.replace(front_matter_match.group(0), f"---\n{new_front_matter}---")
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {file_path}: added authors '{authors}'")
    return True

def main():
    """Main function to process all publication files."""
    publications_dir = Path("_publications")
    
    if not publications_dir.exists():
        print("Error: _publications directory not found")
        return
    
    # Find all markdown files in publications directory
    md_files = list(publications_dir.glob("*.md"))
    
    if not md_files:
        print("No markdown files found in _publications directory")
        return
    
    print(f"Found {len(md_files)} publication files")
    
    updated_count = 0
    for file_path in md_files:
        if process_publication_file(file_path):
            updated_count += 1
    
    print(f"\nSummary: Updated {updated_count} out of {len(md_files)} files")

if __name__ == "__main__":
    main() 