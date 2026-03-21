#!/bin/bash
# basic_conversion.sh - Your first MinerU conversion

# This script demonstrates the simplest possible MinerU usage:
# Converting a single PDF to Markdown

# Prerequisites:
# - MinerU installed (pip install -U "mineru[all]")
# - A PDF file to process

# Usage: ./basic_conversion.sh /path/to/your/document.pdf

if [ $# -eq 0 ]; then
    echo "Usage: $0 <path-to-pdf>"
    echo "Example: $0 ./research_paper.pdf"
    exit 1
fi

INPUT_PDF="$1"
OUTPUT_DIR="./output"

# Check if input file exists
if [ ! -f "$INPUT_PDF" ]; then
    echo "Error: File not found: $INPUT_PDF"
    exit 1
fi

echo "Processing: $INPUT_PDF"
echo "Output directory: $OUTPUT_DIR"
echo ""

# Run MinerU with default settings
# -p: path to input PDF
# -o: output directory
mineru -p "$INPUT_PDF" -o "$OUTPUT_DIR"

# Check if processing succeeded
if [ $# -eq 0 ]; then
    echo ""
    echo "✅ Processing complete!"
    echo ""
    echo "Output files are in: $OUTPUT_DIR/auto/"
    echo ""
    echo "To view the Markdown output:"
    PDF_NAME=$(basename "$INPUT_PDF" .pdf)
    echo "  cat $OUTPUT_DIR/auto/$PDF_NAME/$PDF_NAME.md"
else
    echo "❌ Processing failed"
    exit 1
fi
