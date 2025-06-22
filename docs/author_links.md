# Author Links Feature

This document explains how to add clickable links to author names in publication pages.

## Overview

The author links feature allows you to automatically convert author names into clickable links that point to their personal websites, Google Scholar profiles, or other relevant pages.

## How It Works

1. **Author Database**: Author information is stored in `_data/authors.yml`
2. **Automatic Linking**: A Liquid filter automatically converts author names to links
3. **Fallback**: If no link is found, the author name is displayed as plain text

## Setup

### Step 1: Configure Author Information

Edit `_data/authors.yml` to add author information:

```yaml
authors:
  pengcheng_wang:
    name: "Pengcheng Wang"
    url: "https://pengchengwang.github.io/"
    institution: "Purdue University"
    
  jane_doe:
    name: "Jane Doe"
    url: "https://janedoe.com"
    institution: "Stanford University"
```

### Step 2: Use Author Names in Publications

In your publication markdown files, simply list the author names:

```yaml
---
title: "Your Paper Title"
collection: publications
date: 2024-01-01
venue: 'Journal Name'
authors: 'Pengcheng Wang, Jane Doe, John Smith'
---
```

The system will automatically:
- Look up each author name in the database
- Convert matching names to clickable links
- Leave unmatched names as plain text

## Author Database Format

Each author entry should have:

- `name`: The exact name as it appears in publications
- `url`: The author's personal website or profile page
- `institution`: (Optional) Author's institution

## Examples

### Input (in publication file)
```yaml
authors: 'Pengcheng Wang, Jane Doe, Unknown Author'
```

### Output (on website)
- **Pengcheng Wang** → [Pengcheng Wang](https://pengchengwang.github.io/)
- **Jane Doe** → [Jane Doe](https://janedoe.com)
- **Unknown Author** → Unknown Author (no link, plain text)

## Manual Override

If you want to manually specify links for specific authors, you can still use Markdown syntax in the authors field:

```yaml
authors: '[Pengcheng Wang](https://custom-link.com), Jane Doe, [John Smith](https://johnsmith.com)'
```

## Benefits

1. **Centralized Management**: All author information in one place
2. **Automatic Updates**: Change an author's URL once, updates everywhere
3. **Consistency**: Ensures consistent linking across all publications
4. **Flexibility**: Supports both automatic and manual linking
5. **Privacy**: No email addresses exposed to prevent spam

## Tips

- Author names in the database must exactly match the names in publications
- URLs should be complete (including `https://`)
- You can add authors to the database as needed
- The system is case-sensitive for author names
- Email addresses are intentionally excluded to prevent spam and scraping 