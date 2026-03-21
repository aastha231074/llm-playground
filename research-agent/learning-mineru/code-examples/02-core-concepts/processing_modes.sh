#!/bin/bash
# processing_modes.sh - Demonstrate MinerU processing modes

# This script shows the three processing modes:
# 1. Auto - Automatically detect (default)
# 2. Text - Direct text extraction
# 3. OCR - Optical character recognition

# Usage: ./processing_modes.sh <pdf-path>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <pdf-path>"
    echo "Example: $0 ./document.pdf"
    exit 1
fi

INPUT_PDF="$1"

if [ ! -f "$INPUT_PDF" ]; then
    echo "Error: File not found: $INPUT_PDF"
    exit 1
fi

echo "MinerU Processing Modes Demo"
echo "=============================="
echo "Input: $INPUT_PDF"
echo ""

# Mode 1: Auto (default)
echo "1. AUTO MODE - Automatically detect document type"
echo "------------------------------------------------"
mineru -p "$INPUT_PDF" -o ./output_auto --method auto
echo "✅ Output: ./output_auto"
echo ""

# Mode 2: Text extraction
echo "2. TEXT MODE - Direct text extraction (faster)"
echo "------------------------------------------------"
mineru -p "$INPUT_PDF" -o ./output_text --method txt
echo "✅ Output: ./output_text"
echo ""

# Mode 3: OCR
echo "3. OCR MODE - Optical character recognition"
echo "------------------------------------------------"
echo "   (Specify language for better accuracy)"

# Ask for language
read -p "Enter language code (en/ch/korean/japan/etc) [en]: " LANG
LANG=${LANG:-en}

mineru -p "$INPUT_PDF" -o ./output_ocr --method ocr --lang "$LANG"
echo "✅ Output: ./output_ocr"
echo ""

echo "=============================="
echo "Processing complete!"
echo ""
echo "Compare outputs:"
echo "  diff ./output_auto/auto/*/content_list.json ./output_text/auto/*/content_list.json"
echo ""
echo "When to use each mode:"
echo "  • Auto: When unsure (safest choice)"
echo "  • Text: For digital PDFs with selectable text (fastest)"
echo "  • OCR: For scanned documents or corrupted PDFs (most robust)"
