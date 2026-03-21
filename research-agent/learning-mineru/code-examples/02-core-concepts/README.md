# Core Concepts Examples

Examples demonstrating MinerU's fundamental concepts.

## Files

1. **`backend_comparison.py`** - Compare the three processing backends
2. **`processing_modes.sh`** - Demonstrate auto/text/OCR modes
3. **`content_extraction.py`** - Extract and analyze different content types
4. **`environment_config.sh`** - Environment variable configuration examples

## Running Examples

### 1. Backend Comparison

Compare performance and output quality across backends:

```bash
python backend_comparison.py /path/to/document.pdf
```

**Expected Output:**
```
Backend                   Status     Time (s)     Size (bytes)
------------------------------------------------------------
pipeline                  ✅ Success  3.45         45,231
hybrid-auto-engine        ✅ Success  5.12         47,856
vlm-auto-engine          ✅ Success  8.34         48,102

⚡ Fastest: pipeline (3.45s)
📄 Most content: vlm-auto-engine (48,102 bytes)
```

### 2. Processing Modes

Learn the difference between auto, text, and OCR modes:

```bash
chmod +x processing_modes.sh
./processing_modes.sh /path/to/document.pdf
```

### 3. Content Extraction

Extract and analyze different content types:

```bash
python content_extraction.py /path/to/research_paper.pdf
```

**Expected Output:**
```
Content Type Distribution:
----------------------------------------
  text               23 items
  table               3 items
  image               5 items
  formula            12 items

CONTENT EXAMPLES
========================================

1. TEXT BLOCK EXAMPLE:
----------------------------------------
# Introduction
This paper presents MinerU, a comprehensive solution...

2. TABLE EXAMPLE (HTML):
----------------------------------------
<table><tr><td>Model</td><td>Accuracy</td></tr>...

3. IMAGE EXAMPLE:
----------------------------------------
Image path: ./output/auto/paper/images/image_001.png
Caption: Figure 1: System architecture

4. FORMULA EXAMPLE (LaTeX):
----------------------------------------
E = mc^2
```

## Key Takeaways

### Backend Selection

| Backend | Best For | Hardware |
|---------|----------|----------|
| **Pipeline** | Simple documents, CPU-only | 3GB+ VRAM |
| **Hybrid** | General use (default) | GPU recommended |
| **VLM** | Highest accuracy | 20-25GB VRAM |

### Processing Modes

- **Auto**: Automatically detect (safest choice)
- **Text**: Digital PDFs (fastest)
- **OCR**: Scanned documents (most robust)

### Content Types

MinerU extracts:
- **Text**: Headings, paragraphs, lists
- **Tables**: HTML format (preserves structure)
- **Images**: Separate files with captions
- **Formulas**: LaTeX format

## Next Steps

Move on to `03-patterns/` for real-world application examples.
