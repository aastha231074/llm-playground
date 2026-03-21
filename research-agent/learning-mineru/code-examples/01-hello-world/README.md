# Hello World Examples

Basic examples to get started with MinerU.

## Files

- `basic_conversion.sh` - Bash script for simple PDF conversion
- `basic_conversion.py` - Python script for simple PDF conversion
- `verify_installation.sh` - Check if MinerU is installed correctly

## Quick Start

### Bash Version

```bash
chmod +x basic_conversion.sh
./basic_conversion.sh /path/to/your/document.pdf
```

### Python Version

```bash
python basic_conversion.py /path/to/your/document.pdf
```

## Expected Output

After running either script, you should see:

```
Processing: /path/to/your/document.pdf
Output directory: ./output

[MinerU processing output...]

✅ Processing complete!

Output files are in: ./output/auto/document/
Files created:
  - document.md (Markdown)
  - content_list.json (Structured JSON)
  - images/ (Extracted images)
```

## What's Created

```
output/
└── auto/
    └── your_document/
        ├── your_document.md          # Main Markdown output
        ├── content_list.json         # Structured content (JSON)
        ├── middle.json               # Hierarchical structure
        ├── model.json                # Raw model output
        ├── layout.pdf                # Layout visualization
        ├── span.pdf                  # Content annotation
        └── images/                   # Extracted images
            ├── image_001.png
            └── image_002.png
```

## Next Steps

1. Open `your_document.md` to see the converted content
2. Explore `content_list.json` to understand the structured output
3. Check out the `02-core-concepts/` examples for more advanced usage
