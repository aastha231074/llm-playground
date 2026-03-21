#!/usr/bin/env python3
"""
content_extraction.py - Extract and analyze different content types

This script demonstrates how MinerU extracts different content types:
- Text blocks
- Tables (as HTML)
- Images
- Mathematical formulas (as LaTeX)

Usage: python content_extraction.py <pdf-path>
"""

import sys
import json
import subprocess
from pathlib import Path
from collections import Counter


def process_pdf(pdf_path: str, output_dir: str = "./output") -> Path:
    """Process PDF with MinerU"""
    print(f"Processing: {pdf_path}")

    subprocess.run(
        ["mineru", "-p", pdf_path, "-o", output_dir],
        check=True,
        capture_output=True
    )

    # Find content_list.json
    pdf_name = Path(pdf_path).stem
    content_json = Path(output_dir) / "auto" / pdf_name / "content_list.json"

    return content_json


def analyze_content(content_json: Path):
    """Analyze and display content types"""
    with open(content_json, 'r', encoding='utf-8') as f:
        content = json.load(f)

    print(f"\n{'='*60}")
    print("CONTENT ANALYSIS")
    print(f"{'='*60}\n")

    # Count content types
    type_counts = Counter(item.get('type', 'unknown') for item in content)

    print("Content Type Distribution:")
    print("-" * 40)
    for content_type, count in type_counts.items():
        print(f"  {content_type:<15} {count:>5} items")

    # Show examples of each type
    print(f"\n{'='*60}")
    print("CONTENT EXAMPLES")
    print(f"{'='*60}\n")

    # Text example
    text_items = [item for item in content if item.get('type') == 'text']
    if text_items:
        print("1. TEXT BLOCK EXAMPLE:")
        print("-" * 40)
        first_text = text_items[0].get('text', '')[:200]
        print(first_text + "...\n" if len(text_items[0].get('text', '')) > 200 else first_text + "\n")

    # Table example
    table_items = [item for item in content if item.get('type') == 'table']
    if table_items:
        print("2. TABLE EXAMPLE (HTML):")
        print("-" * 40)
        first_table = table_items[0].get('html', '')[:300]
        print(first_table + "...\n" if len(table_items[0].get('html', '')) > 300 else first_table + "\n")

    # Image example
    image_items = [item for item in content if item.get('type') == 'image']
    if image_items:
        print("3. IMAGE EXAMPLE:")
        print("-" * 40)
        print(f"Image path: {image_items[0].get('image_path', 'N/A')}")
        print(f"Caption: {image_items[0].get('caption', 'No caption')}\n")

    # Formula example
    formula_items = [item for item in content if item.get('type') == 'formula']
    if formula_items:
        print("4. FORMULA EXAMPLE (LaTeX):")
        print("-" * 40)
        print(formula_items[0].get('latex', 'N/A'))
        print()

    return content, type_counts


def extract_by_type(content: list, content_type: str) -> list:
    """Extract all items of a specific type"""
    return [item for item in content if item.get('type') == content_type]


def save_extracted_content(content: list, type_counts: dict, output_base: str = "./extracted"):
    """Save extracted content by type to separate files"""
    output_path = Path(output_base)
    output_path.mkdir(exist_ok=True)

    # Save all text
    text_items = extract_by_type(content, 'text')
    if text_items:
        text_file = output_path / "all_text.txt"
        with open(text_file, 'w', encoding='utf-8') as f:
            for item in text_items:
                f.write(item.get('text', '') + "\n\n")
        print(f"✅ Saved {len(text_items)} text blocks to: {text_file}")

    # Save all tables
    table_items = extract_by_type(content, 'table')
    if table_items:
        tables_file = output_path / "all_tables.html"
        with open(tables_file, 'w', encoding='utf-8') as f:
            f.write("<html><body>\n")
            for i, item in enumerate(table_items, 1):
                f.write(f"<h2>Table {i}</h2>\n")
                f.write(item.get('html', '') + "\n\n")
            f.write("</body></html>")
        print(f"✅ Saved {len(table_items)} tables to: {tables_file}")

    # Save all formulas
    formula_items = extract_by_type(content, 'formula')
    if formula_items:
        formulas_file = output_path / "all_formulas.tex"
        with open(formulas_file, 'w', encoding='utf-8') as f:
            for i, item in enumerate(formula_items, 1):
                f.write(f"% Formula {i}\n")
                f.write(item.get('latex', '') + "\n\n")
        print(f"✅ Saved {len(formula_items)} formulas to: {formulas_file}")

    # List image paths
    image_items = extract_by_type(content, 'image')
    if image_items:
        images_file = output_path / "image_list.txt"
        with open(images_file, 'w', encoding='utf-8') as f:
            for item in image_items:
                f.write(f"{item.get('image_path', 'N/A')}\n")
        print(f"✅ Saved {len(image_items)} image paths to: {images_file}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python content_extraction.py <pdf-path>")
        print("Example: python content_extraction.py ./research_paper.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not Path(pdf_path).exists():
        print(f"Error: File not found: {pdf_path}")
        sys.exit(1)

    # Process PDF
    content_json = process_pdf(pdf_path)

    # Analyze content
    content, type_counts = analyze_content(content_json)

    # Save extracted content by type
    print(f"\n{'='*60}")
    save_extracted_content(content, type_counts)

    print(f"\n{'='*60}")
    print("Content extraction complete!")
    print()
    print("Tips:")
    print("  • Use content_list.json for programmatic access")
    print("  • Tables are always in HTML format (easier to parse)")
    print("  • Formulas are in LaTeX format (can render with MathJax)")
    print("  • Images are saved separately and referenced by path")


if __name__ == "__main__":
    main()
