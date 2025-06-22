# Publication Authors Feature

This document explains how to add author information to publication pages in your academic website.

## Overview

The publication pages now support displaying author information in both the publication list and individual publication pages. The author information is extracted from the citation field and displayed with a user icon.

## How to Add Authors to Publications

### Method 1: Manual Addition

Add an `authors` field to the front matter of your publication markdown files:

```yaml
---
title: "Your Paper Title"
collection: publications
date: 2024-01-01
venue: 'Journal Name'
authors: 'Author1, Author2, and Author3'  # Add this line
citation: 'Author1, Author2, and Author3. (2024). "Your Paper Title." Journal Name.'
---
```

### Method 2: Automatic Extraction (Recommended)

Use the provided Python script to automatically extract authors from existing citation fields:

```bash
cd scripts
python add_authors_to_publications.py
```

This script will:
1. Scan all files in the `_publications` directory
2. Extract author information from the citation field
3. Add an `authors` field to the front matter
4. Skip files that already have an authors field

## Supported Citation Formats

The script can extract authors from these citation formats:

### BibTeX Format
```bibtex
@article{key,
    author={Author1, Author2, and Author3},
    title={Title},
    journal={Journal},
    year={2024}
}
```

### Regular Citation Format
```
Author1, Author2, and Author3. (2024). "Title." Journal.
```

## Display Features

- **Publication List**: Authors are displayed with a users icon (👥) below the venue and date
- **Individual Publication Pages**: Authors are displayed in the page header with a users icon
- **Styling**: Authors are displayed in italic style with a distinct color

## CSS Customization

The author information uses the CSS class `.archive__item-authors`. You can customize the appearance by modifying the styles in `_sass/_custom.scss`:

```scss
.archive__item-authors {
  color: #495057;
  font-size: 0.9em;
  margin: 5px 0;
  font-style: italic;
}
```

## Example

Before:
```
Paper Title
📚 Journal Name • 2024
```

After:
```
Paper Title
📚 Journal Name • 2024
👥 Author1, Author2, and Author3
```

## Notes

- The authors field is optional. Publications without this field will display normally
- The script preserves the original citation field
- Author information is extracted from the citation field, so ensure your citations are properly formatted 