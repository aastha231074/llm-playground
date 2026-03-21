#!/usr/bin/env python3
"""
basic_conversion.py - Your first MinerU conversion in Python

This script demonstrates the simplest possible MinerU usage:
Converting a single PDF to Markdown using subprocess

Prerequisites:
- MinerU installed (pip install -U "mineru[all]")
- A PDF file to process

Usage: python basic_conversion.py /path/to/your/document.pdf
"""

import sys
import subprocess
from pathlib import Path


def convert_pdf_to_markdown(pdf_path: str, output_dir: str = "./output") -> bool:
    """
    Convert a PDF to Markdown using MinerU

    Args:
        pdf_path: Path to input PDF file
        output_dir: Directory for output files

    Returns:
        True if successful, False otherwise
    """
    # Check if input file exists
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        print(f"❌ Error: File not found: {pdf_path}")
        return False

    print(f"Processing: {pdf_path}")
    print(f"Output directory: {output_dir}")
    print()

    try:
        # Run MinerU command
        result = subprocess.run(
            ["mineru", "-p", pdf_path, "-o", output_dir],
            check=True,
            capture_output=True,
            text=True
        )

        # Print MinerU output
        if result.stdout:
            print(result.stdout)

        print()
        print("✅ Processing complete!")
        print()

        # Show output location
        pdf_name = pdf_file.stem
        output_path = Path(output_dir) / "auto" / pdf_name
        print(f"Output files are in: {output_path}")
        print()
        print("Files created:")
        print(f"  - {pdf_name}.md (Markdown)")
        print(f"  - content_list.json (Structured JSON)")
        print(f"  - images/ (Extracted images)")

        return True

    except subprocess.CalledProcessError as e:
        print("❌ Processing failed")
        print(f"Error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python basic_conversion.py <path-to-pdf>")
        print("Example: python basic_conversion.py ./research_paper.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    success = convert_pdf_to_markdown(pdf_path)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
