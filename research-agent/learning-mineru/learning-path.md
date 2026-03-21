# MinerU Learning Path

A progressive guide to mastering MinerU, from first principles to production use.

---

## Level 1: Overview & Motivation

### What Problem Does MinerU Solve?

**The Challenge**: PDFs are designed for humans, not machines. When you need to:
- Extract content from scientific papers with complex formulas
- Convert multi-column layouts into linear text for AI processing
- Parse tables while preserving their structure
- Handle scanned documents with OCR
- Prepare documents for LLM training or RAG systems

...traditional PDF parsers fail. They lose structure, mangle tables, ignore formulas, and produce poor quality output for AI workflows.

**MinerU's Solution**: High-fidelity PDF-to-Markdown conversion that:
- Preserves document structure (headings, paragraphs, lists)
- Converts mathematical formulas to LaTeX
- Extracts tables as HTML with proper structure
- Supports 109 languages with advanced OCR
- Removes noise (headers, footers, page numbers)
- Outputs AI-ready formats (Markdown, JSON)

### What Existed Before? Why Is MinerU Better?

**Traditional Approaches**:

| Tool | Approach | Limitations |
|------|----------|-------------|
| **pypdf/pdfminer** | Text extraction | No layout understanding, loses structure |
| **OCR-only tools** | Image → text | Slow, no semantic understanding |
| **Commercial APIs** | Cloud-based | Cost per page, privacy concerns, vendor lock-in |
| **Nougat** | Neural OCR | Academic focus, slow, limited document types |

**MinerU's Innovation**:

1. **Multi-Backend Architecture**: Choose between speed (Pipeline backend), accuracy (VLM backend), or balanced (Hybrid backend)

2. **Two-Stage Processing** (MinerU 2.5):
   - **Stage 1**: Global layout understanding (identify document structure)
   - **Stage 2**: Fine-grained content recognition (extract detailed text/visuals)

   This avoids the trade-off between context (full-page processing) and detail (cropped regions).

3. **Multimodal Content Extraction**: Handles text, images, tables, and formulas in a unified workflow

4. **Production-Ready**: Used in InternLM's pre-training pipeline, battle-tested at scale

### Who Uses It? For What?

**Primary Users**:

1. **AI/ML Engineers**
   - Building RAG (Retrieval-Augmented Generation) systems
   - Preparing training data for LLMs
   - Creating document understanding pipelines

2. **Researchers**
   - Processing academic papers for literature review
   - Extracting data from scientific publications
   - Converting papers for terminal-based reading

3. **Enterprise**
   - Knowledge management systems
   - Legal document processing
   - Financial report analysis
   - Archive digitization

4. **Data Scientists**
   - Creating structured datasets from PDFs
   - Document classification preprocessing
   - Information extraction workflows

**Common Use Cases**:
- **Scientific Literature Processing**: Extract formulas, citations, and complex layouts from research papers
- **LLM Training**: Prepare high-quality document data for pre-training
- **RAG Pipelines**: Convert documents for vector database ingestion
- **Document Digitization**: Transform legacy PDFs into searchable, structured data
- **Multimodal AI**: Extract text, images, and tables for multimodal model training

### When Should You NOT Use MinerU?

**MinerU is NOT ideal for**:

1. **Comic Books & Art Albums**: Not designed for art-heavy, non-traditional layouts
2. **Vertical Text Documents**: Limited support for vertical writing systems
3. **Simple Text Extraction**: If you just need raw text without structure, simpler tools (pypdf) are faster
4. **Real-time Processing**: Requires significant compute; not suitable for instant processing on edge devices
5. **Code-Heavy Documents**: Code blocks in PDFs aren't well-supported by layout models
6. **Resource-Constrained Environments**: Minimum 16GB RAM; if you have less, use simpler tools

**When Alternatives Are Better**:
- **Marker**: Better image preservation, faster processing, multiple interfaces (but GPL license)
- **MarkItDown**: Multi-format support (Word, PPT, Excel) with easy installation (but basic PDF handling)
- **Commercial APIs** (Adobe, Google Document AI): If cost isn't a concern and you need guaranteed SLAs

**Red Flags**:
- Documents with extremely complex, uncertain reading order
- Need for sub-second processing times
- Cannot provision GPU resources (though CPU-only mode exists)
- AGPL-3.0 license is incompatible with your use case

---

## Level 2: Installation & Hello World

### Prerequisites

**Hardware Requirements**:
- **RAM**: Minimum 16GB (32GB+ recommended for large documents)
- **Storage**: 20GB+ free disk space (SSD preferred for model loading)
- **Processor**: Any modern CPU (multi-core beneficial)
- **GPU** (Optional but recommended):
  - NVIDIA GPU with Volta architecture or newer (RTX 2000 series+)
  - OR Apple Silicon (M1/M2/M3) with macOS 14.0+
  - 20-25GB VRAM recommended for VLM backend

**Software Requirements**:
- **Python**: 3.10, 3.11, 3.12, or 3.13
  - **Windows limitation**: 3.10-3.12 only (Ray dependency doesn't support 3.13)
- **Operating System**:
  - Linux (2019+ distributions)
  - macOS 14.0+
  - Windows 10/11

**Knowledge Prerequisites**:
- Basic command-line usage (cd, ls, running commands)
- Understanding of file paths
- (Optional) Basic Python knowledge for API usage

### Installation Steps

**Step 1: Verify Python Version**

```bash
python --version
# or
python3 --version
```

Expected output: `Python 3.10.x`, `3.11.x`, `3.12.x`, or `3.13.x` (3.10-3.12 on Windows)

**Step 2: Create Virtual Environment (Recommended)**

```bash
# Create virtual environment
python -m venv mineru-env

# Activate it
# On macOS/Linux:
source mineru-env/bin/activate

# On Windows:
mineru-env\Scripts\activate
```

**Step 3: Install MinerU**

```bash
# Upgrade pip first
pip install --upgrade pip

# Install uv (fast Python package installer)
pip install uv

# Install MinerU with all dependencies
uv pip install -U "mineru[all]"
```

**Alternative: Install from Source**

```bash
git clone https://github.com/opendatalab/MinerU.git
cd MinerU
uv pip install -e .[all]
```

**Step 4: Verify Installation**

```bash
mineru --help
```

Expected output: Help text showing available commands and options.

### Minimal Working Example

**Create a test PDF** (or use your own):

Save this as `test.txt`:
```
# Test Document

This is a simple test for MinerU.

## Features
- Text extraction
- Structure preservation
- Markdown output
```

Convert to PDF (or just use any PDF you have handy).

**Run MinerU**:

```bash
mineru -p /path/to/your/document.pdf -o ./output
```

Replace `/path/to/your/document.pdf` with the actual path to your PDF.

### Understanding the Output

After running, check the `./output` directory:

```bash
ls -la ./output/
```

You should see:
- **`auto/`** directory containing results
- Inside: `{filename}/` folder with multiple files

```bash
ls -la ./output/auto/your_document/
```

**Output Files**:

1. **`your_document.md`** - Main Markdown output (human-readable)
2. **`content_list.json`** - Flat structure with content in reading order
3. **`middle.json`** - Hierarchical document structure
4. **`model.json`** - Raw model inference results
5. **`layout.pdf`** - Visual layout analysis with reading order
6. **`span.pdf`** - Content annotation with colored bounding boxes
7. **`images/`** - Extracted images folder

### Verify It Works

**Open the Markdown file**:

```bash
cat ./output/auto/your_document/your_document.md
# or use a text editor
```

**Check if**:
- ✅ Text is extracted correctly
- ✅ Headings are marked with `#` symbols
- ✅ Structure is preserved
- ✅ No excessive noise (headers/footers/page numbers removed)

**Compare with original PDF**: Open `layout.pdf` to see how MinerU analyzed the document structure.

### Common Installation Issues

**Issue 1: Python version incompatible**
```
Solution: Install Python 3.10-3.13 (3.10-3.12 on Windows)
```

**Issue 2: Out of memory during model loading**
```
Solution: Ensure you have 16GB+ RAM, close other applications
```

**Issue 3: GPU not detected (NVIDIA)**
```
Solution: Install PyTorch with CUDA support:
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

**Issue 4: Command not found: mineru**
```
Solution: Ensure virtual environment is activated and installation completed successfully
```

---

## Level 3: Core Concepts

### Concept 1: Multi-Backend Processing Architecture

**What It Is**: MinerU offers three different processing engines (backends) optimized for different scenarios.

**The Three Backends**:

1. **Pipeline Backend** - Traditional computer vision approach
   - Uses YOLO for layout detection + OCR models
   - Runs on CPU (minimum 3GB VRAM)
   - Fast and resource-efficient
   - Best for: Simple documents, resource-constrained environments

2. **VLM Backend** - Vision Language Model approach
   - Uses modern transformer models (Qwen2-VL)
   - Requires GPU with significant VRAM (20-25GB)
   - Highest accuracy
   - Best for: Complex documents, academic papers, when quality matters most

3. **Hybrid Backend** (Default since v2.7.0) - Combined approach
   - Extracts text directly from text PDFs (lower hallucination)
   - Uses VLM for scanned/image regions
   - Balances accuracy and resource usage
   - Best for: General-purpose usage, mixed document types

**How They Relate**: Think of them as different tools in a toolbox. You choose based on:
- Document complexity
- Available hardware
- Speed vs accuracy requirements

**Example - Choosing a Backend**:

```bash
# Use CPU-only pipeline backend (fastest, lowest resource)
mineru -p document.pdf -o ./output -b pipeline

# Use VLM backend (highest accuracy, needs GPU)
mineru -p document.pdf -o ./output -b vlm-auto-engine

# Use hybrid backend (default, balanced)
mineru -p document.pdf -o ./output -b hybrid-auto-engine
# or simply:
mineru -p document.pdf -o ./output
```

**Common Mistake**: Using VLM backend on CPU without enough RAM
```bash
# ❌ Wrong: VLM on CPU with 8GB RAM
mineru -p complex_paper.pdf -o ./output -b vlm-auto-engine

# ✅ Right: Use pipeline backend for CPU
mineru -p complex_paper.pdf -o ./output -b pipeline
```

### Concept 2: Processing Modes (Auto, Text, OCR)

**What It Is**: MinerU can automatically detect or be told how to process a PDF.

**The Three Modes**:

1. **Auto Mode** (Default) - Automatically detects document type
   - Analyzes PDF to determine if it's text-based or scanned
   - Switches between text extraction and OCR as needed
   - Best for: Mixed documents, when unsure

2. **Text Mode** - Direct text extraction
   - Extracts embedded text from PDF
   - Faster than OCR
   - Best for: Digital PDFs with selectable text

3. **OCR Mode** - Optical character recognition
   - Treats entire document as images
   - Slower but handles scanned documents
   - Supports 109 languages
   - Best for: Scanned documents, corrupted PDFs

**How They Relate**:
```
Auto Mode
    ├─> Detects text-based → Text Mode
    └─> Detects scanned → OCR Mode
```

**Example - Specifying Processing Mode**:

```bash
# Auto-detect (default)
mineru -p document.pdf -o ./output --method auto

# Force text extraction
mineru -p digital_document.pdf -o ./output --method txt

# Force OCR (with language specification for accuracy)
mineru -p scanned_paper.pdf -o ./output --method ocr --lang en
```

**Example - Multi-language OCR**:

```bash
# Chinese document
mineru -p chinese_paper.pdf -o ./output --method ocr --lang ch

# Korean document
mineru -p korean_report.pdf -o ./output --method ocr --lang korean

# Japanese document
mineru -p japanese_manual.pdf -o ./output --method ocr --lang japan
```

**Common Mistake**: Not specifying language for non-English OCR
```bash
# ❌ Wrong: No language specified for Chinese scanned PDF
mineru -p chinese_scanned.pdf -o ./output --method ocr

# ✅ Right: Specify language for better accuracy
mineru -p chinese_scanned.pdf -o ./output --method ocr --lang ch
```

### Concept 3: Hierarchical Document Understanding

**What It Is**: MinerU processes documents in multiple stages, generating different JSON representations at each level.

**The Three JSON Outputs**:

1. **`model.json`** - Raw inference results
   - Bounding boxes for detected objects
   - Classification labels (text, table, image, formula)
   - Lowest level, directly from AI models

2. **`middle.json`** - Hierarchical structure
   - Organized into blocks, lines, and spans
   - Maintains spatial relationships
   - Intermediate representation

3. **`content_list.json`** - Reading-order content
   - Flattened structure in correct reading order
   - Content typed (text, table, image, formula)
   - Easiest to consume programmatically

**How They Relate**:
```
model.json (raw detection)
    ↓ (structure analysis)
middle.json (hierarchical blocks)
    ↓ (reading order + formatting)
content_list.json (linear content)
    ↓ (markdown formatting)
output.md (human-readable)
```

**Example - Using content_list.json**:

```python
import json

# Load the structured output
with open('./output/auto/document/content_list.json', 'r') as f:
    content = json.load(f)

# Iterate through content in reading order
for item in content:
    content_type = item['type']  # 'text', 'table', 'image', 'formula'

    if content_type == 'text':
        print(f"Text: {item['text']}")
    elif content_type == 'table':
        print(f"Table (HTML): {item['html']}")
    elif content_type == 'image':
        print(f"Image path: {item['image_path']}")
    elif content_type == 'formula':
        print(f"Formula (LaTeX): {item['latex']}")
```

**Common Mistake**: Trying to parse Markdown instead of using JSON
```python
# ❌ Wrong: Parsing Markdown with regex
with open('output.md', 'r') as f:
    text = f.read()
    tables = re.findall(r'\|.*\|', text)  # Fragile!

# ✅ Right: Use structured JSON
with open('content_list.json', 'r') as f:
    content = json.load(f)
    tables = [item for item in content if item['type'] == 'table']
```

### Concept 4: Multimodal Content Extraction

**What It Is**: MinerU treats documents as heterogeneous collections of different content types, each extracted optimally.

**Content Types Handled**:

1. **Text Blocks**
   - Headings (with hierarchy detection)
   - Paragraphs
   - Lists (bullet and numbered)
   - Captions

2. **Tables**
   - Extracted as HTML (preserves structure)
   - Supports cross-page table merging
   - Can be disabled if not needed

3. **Images**
   - Extracted to separate files
   - Linked in Markdown output
   - Captions preserved

4. **Mathematical Formulas**
   - Converted to LaTeX format
   - Inline: `$formula$`
   - Display: `$$formula$$`
   - Can be disabled if not needed

5. **Metadata Removal**
   - Headers, footers, page numbers automatically removed
   - Footnotes handled separately

**Example - Selective Content Extraction**:

```bash
# Extract only text and images (disable formulas and tables)
MINERU_FORMULA_ENABLE=false MINERU_TABLE_ENABLE=false \
  mineru -p document.pdf -o ./output

# Extract everything (default)
mineru -p document.pdf -o ./output

# Extract with formula processing enabled
mineru -p scientific_paper.pdf -o ./output --formula-enable
```

**Example - Accessing Different Content Types**:

```python
import json

with open('./output/auto/paper/content_list.json', 'r') as f:
    content = json.load(f)

# Separate content by type
texts = [item for item in content if item['type'] == 'text']
tables = [item for item in content if item['type'] == 'table']
images = [item for item in content if item['type'] == 'image']
formulas = [item for item in content if item['type'] == 'formula']

print(f"Found: {len(texts)} text blocks, {len(tables)} tables, "
      f"{len(images)} images, {len(formulas)} formulas")

# Extract all LaTeX formulas
all_formulas = [item['latex'] for item in formulas]
print("Formulas:", all_formulas)
```

**Common Mistake**: Expecting tables in Markdown format
```python
# ❌ Wrong: Tables in Markdown are still embedded HTML
md_content = open('output.md').read()
# Markdown tables look like: | col1 | col2 |
# But MinerU tables are: <table><tr><td>...</td></tr></table>

# ✅ Right: Tables are always HTML, use HTML parser
from bs4 import BeautifulSoup
soup = BeautifulSoup(item['html'], 'html.parser')
rows = soup.find_all('tr')
```

### Concept 5: Environment-Based Configuration

**What It Is**: MinerU uses environment variables for high-priority configuration that overrides defaults.

**Key Environment Variables**:

1. **`MINERU_DEVICE_MODE`** - Hardware selection
   - Values: `cpu`, `cuda`, `mps`, `cann` (NPU)
   - Example: `MINERU_DEVICE_MODE=cuda`

2. **`MINERU_MODEL_SOURCE`** - Model repository
   - Values: `huggingface`, `modelscope`, `local`
   - Example: `MINERU_MODEL_SOURCE=modelscope`

3. **`MINERU_FORMULA_ENABLE`** - Toggle formula parsing
   - Values: `true`, `false`
   - Example: `MINERU_FORMULA_ENABLE=true`

4. **`MINERU_TABLE_ENABLE`** - Toggle table extraction
   - Values: `true`, `false`
   - Example: `MINERU_TABLE_ENABLE=false`

5. **`MINERU_VL_MODEL_NAME`** - Specific VLM model
   - Example: `MINERU_VL_MODEL_NAME=Qwen2-VL-7B-Instruct`

6. **`CUDA_VISIBLE_DEVICES`** - GPU selection
   - Example: `CUDA_VISIBLE_DEVICES=0,1`

**How They Relate**: Environment variables > config file > command-line defaults

**Example - Using Environment Variables**:

```bash
# Use specific GPU
CUDA_VISIBLE_DEVICES=0 mineru -p document.pdf -o ./output

# Use CPU only
MINERU_DEVICE_MODE=cpu mineru -p document.pdf -o ./output

# Download models from ModelScope (if HuggingFace is blocked)
MINERU_MODEL_SOURCE=modelscope mineru -p document.pdf -o ./output

# Disable formula extraction for speed
MINERU_FORMULA_ENABLE=false mineru -p document.pdf -o ./output

# Combine multiple settings
CUDA_VISIBLE_DEVICES=0 MINERU_FORMULA_ENABLE=true MINERU_TABLE_ENABLE=true \
  mineru -p scientific_paper.pdf -o ./output
```

**Example - Configuration File** (`~/.mineru/mineru.json`):

```json
{
  "latex_delimiters": {
    "inline": ["$", "$"],
    "display": ["$$", "$$"]
  },
  "model_config": {
    "device": "cuda",
    "model_source": "huggingface"
  },
  "parsing_config": {
    "formula_enable": true,
    "table_enable": true
  }
}
```

**Common Mistake**: Forgetting environment variables override config
```bash
# ❌ Wrong: Config file says cuda, but env var says cpu
# Config: {"device": "cuda"}
MINERU_DEVICE_MODE=cpu mineru -p document.pdf -o ./output
# Result: Uses CPU (env var wins)

# ✅ Right: Be consistent or remove conflicting settings
unset MINERU_DEVICE_MODE  # Remove env var to use config
mineru -p document.pdf -o ./output
```

---

## Level 4: Practical Patterns

### Pattern 1: Basic Single-File Processing

**Use Case**: Convert one PDF to Markdown for reading or analysis.

**Code Example**:

```bash
#!/bin/bash
# basic_processing.sh

# Input and output paths
INPUT_PDF="./documents/research_paper.pdf"
OUTPUT_DIR="./output"

# Basic processing with default settings
mineru -p "$INPUT_PDF" -o "$OUTPUT_DIR"

echo "Processing complete!"
echo "Check output at: $OUTPUT_DIR/auto/research_paper/"
```

**Expected Output**:
```
Processing complete!
Check output at: ./output/auto/research_paper/
```

**Output files**:
- `research_paper.md` - Markdown file
- `content_list.json` - Structured JSON
- `images/` - Extracted images

### Pattern 2: Batch Processing Multiple PDFs

**Use Case**: Process an entire directory of PDFs for dataset creation.

**Code Example**:

```bash
#!/bin/bash
# batch_processing.sh

INPUT_DIR="./pdfs"
OUTPUT_DIR="./processed"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Process all PDFs in directory
for pdf in "$INPUT_DIR"/*.pdf; do
    echo "Processing: $pdf"
    mineru -p "$pdf" -o "$OUTPUT_DIR"
done

echo "Batch processing complete!"
echo "Processed files in: $OUTPUT_DIR"
```

**Python Version**:

```python
#!/usr/bin/env python3
# batch_processing.py

import os
import subprocess
from pathlib import Path

def process_pdfs(input_dir, output_dir):
    """Process all PDFs in input_dir"""
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)

    # Find all PDFs
    pdf_files = list(input_path.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")

    # Process each PDF
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")

        subprocess.run([
            "mineru",
            "-p", str(pdf_file),
            "-o", str(output_path)
        ], check=True)

    print(f"Batch processing complete! Output: {output_path}")

if __name__ == "__main__":
    process_pdfs("./pdfs", "./processed")
```

### Pattern 3: Optimized Processing for Large Documents

**Use Case**: Process large academic papers or reports efficiently with GPU acceleration and page ranges.

**Code Example**:

```bash
#!/bin/bash
# large_document_processing.sh

INPUT_PDF="./large_textbook.pdf"
OUTPUT_DIR="./output"

# Process with optimizations:
# - Use GPU (CUDA device 0)
# - Use hybrid backend (balanced)
# - Process pages 10-50 only (for testing)
# - Specify language for better OCR

CUDA_VISIBLE_DEVICES=0 \
  mineru \
  -p "$INPUT_PDF" \
  -o "$OUTPUT_DIR" \
  -b hybrid-auto-engine \
  --start-page 10 \
  --end-page 50 \
  --lang en

echo "Large document processing complete!"
```

**Python Version with Multi-GPU**:

```python
#!/usr/bin/env python3
# multi_gpu_processing.py

import subprocess
import os

def process_with_multi_gpu(pdf_path, output_dir, num_gpus=2):
    """Process PDF using multiple GPUs"""

    # Set visible GPUs
    os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(str(i) for i in range(num_gpus))

    # Run with data parallelism
    subprocess.run([
        "mineru",
        "--data-parallel-size", str(num_gpus),
        "-p", pdf_path,
        "-o", output_dir,
        "-b", "hybrid-auto-engine"
    ], check=True)

    print(f"Multi-GPU processing complete using {num_gpus} GPUs")

if __name__ == "__main__":
    process_with_multi_gpu("./huge_document.pdf", "./output", num_gpus=2)
```

### Pattern 4: Building a RAG Pipeline

**Use Case**: Convert documents for ingestion into a vector database for Retrieval-Augmented Generation.

**Code Example**:

```python
#!/usr/bin/env python3
# rag_pipeline.py

import json
import subprocess
from pathlib import Path
from typing import List, Dict

def extract_document(pdf_path: str, output_dir: str) -> Path:
    """Extract content from PDF using MinerU"""
    print(f"Extracting: {pdf_path}")

    subprocess.run([
        "mineru",
        "-p", pdf_path,
        "-o", output_dir
    ], check=True)

    # Determine output path
    pdf_name = Path(pdf_path).stem
    content_json = Path(output_dir) / "auto" / pdf_name / "content_list.json"

    return content_json

def load_structured_content(content_json: Path) -> List[Dict]:
    """Load structured content from MinerU output"""
    with open(content_json, 'r', encoding='utf-8') as f:
        return json.load(f)

def chunk_content_for_rag(content: List[Dict], chunk_size: int = 512) -> List[Dict]:
    """Split content into chunks suitable for vector embedding"""
    chunks = []
    current_chunk = ""
    current_metadata = []

    for item in content:
        item_type = item.get('type', 'text')

        if item_type == 'text':
            text = item.get('text', '')

            # Add to current chunk
            if len(current_chunk) + len(text) < chunk_size:
                current_chunk += text + "\n\n"
                current_metadata.append(item)
            else:
                # Save current chunk and start new one
                if current_chunk:
                    chunks.append({
                        'text': current_chunk.strip(),
                        'metadata': current_metadata.copy()
                    })
                current_chunk = text + "\n\n"
                current_metadata = [item]

        elif item_type == 'table':
            # Tables get their own chunk
            if current_chunk:
                chunks.append({
                    'text': current_chunk.strip(),
                    'metadata': current_metadata.copy()
                })
                current_chunk = ""
                current_metadata = []

            # Add table as separate chunk
            chunks.append({
                'text': f"[TABLE]\n{item.get('html', '')}",
                'metadata': [item],
                'type': 'table'
            })

        elif item_type == 'formula':
            # Include formulas inline
            latex = item.get('latex', '')
            current_chunk += f"${latex}$\n\n"

    # Don't forget last chunk
    if current_chunk:
        chunks.append({
            'text': current_chunk.strip(),
            'metadata': current_metadata.copy()
        })

    return chunks

def prepare_for_rag(pdf_path: str, output_dir: str = "./rag_output") -> List[Dict]:
    """Complete RAG preparation pipeline"""

    # Step 1: Extract content with MinerU
    content_json = extract_document(pdf_path, output_dir)

    # Step 2: Load structured content
    content = load_structured_content(content_json)

    # Step 3: Chunk for vector embedding
    chunks = chunk_content_for_rag(content, chunk_size=512)

    print(f"Created {len(chunks)} chunks from {pdf_path}")

    return chunks

# Example usage
if __name__ == "__main__":
    # Process a research paper for RAG
    chunks = prepare_for_rag("./research_paper.pdf")

    # Print first chunk as example
    print("\nFirst chunk:")
    print(chunks[0]['text'][:200] + "...")

    # Save chunks for vector database ingestion
    with open("./rag_chunks.json", 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"\nChunks saved to rag_chunks.json")
```

**Expected Output**:
```
Extracting: ./research_paper.pdf
Created 47 chunks from ./research_paper.pdf

First chunk:
# MinerU: An Open-Source Solution for Precise Document Content Extraction

## Abstract

We present MinerU, a comprehensive solution for document content extraction...

Chunks saved to rag_chunks.json
```

### Pattern 5: REST API Server for Web Applications

**Use Case**: Deploy MinerU as a web service for integration into web applications.

**Step 1: Start API Server**

```bash
#!/bin/bash
# start_api_server.sh

# Start FastAPI server
mineru-api --host 0.0.0.0 --port 8000

# API documentation available at: http://127.0.0.1:8000/docs
```

**Step 2: Client Code (Python)**

```python
#!/usr/bin/env python3
# api_client.py

import requests
from pathlib import Path

def upload_and_process(pdf_path: str, api_url: str = "http://127.0.0.1:8000") -> dict:
    """Upload PDF to MinerU API and get processed result"""

    # Prepare file for upload
    with open(pdf_path, 'rb') as f:
        files = {'file': (Path(pdf_path).name, f, 'application/pdf')}

        # Send request
        response = requests.post(
            f"{api_url}/file_parse",
            files=files,
            data={
                'backend': 'hybrid-auto-engine',
                'method': 'auto',
                'formula_enable': 'true',
                'table_enable': 'true'
            }
        )

    # Check response
    response.raise_for_status()
    return response.json()

# Example usage
if __name__ == "__main__":
    result = upload_and_process("./document.pdf")

    # Access results
    markdown_content = result['markdown']
    content_list = result['content_list']

    print("Markdown output:")
    print(markdown_content[:500] + "...")

    print(f"\nFound {len(content_list)} content items")
```

**Step 3: Client Code (JavaScript/Node.js)**

```javascript
// api_client.js

const FormData = require('form-data');
const fs = require('fs');
const axios = require('axios');

async function uploadAndProcess(pdfPath, apiUrl = 'http://127.0.0.1:8000') {
    const form = new FormData();
    form.append('file', fs.createReadStream(pdfPath));
    form.append('backend', 'hybrid-auto-engine');
    form.append('method', 'auto');
    form.append('formula_enable', 'true');
    form.append('table_enable', 'true');

    try {
        const response = await axios.post(`${apiUrl}/file_parse`, form, {
            headers: form.getHeaders()
        });

        return response.data;
    } catch (error) {
        console.error('Error processing PDF:', error.message);
        throw error;
    }
}

// Example usage
uploadAndProcess('./document.pdf')
    .then(result => {
        console.log('Markdown output:', result.markdown.substring(0, 500) + '...');
        console.log(`\nFound ${result.content_list.length} content items`);
    })
    .catch(console.error);
```

### Pattern 6: Web UI with Gradio

**Use Case**: Provide a user-friendly web interface for non-technical users.

**Start Gradio Interface**:

```bash
#!/bin/bash
# start_webui.sh

# Start Gradio web interface
mineru-gradio --server-name 0.0.0.0 --server-port 7860

# Access at: http://127.0.0.1:7860
```

**Custom Gradio App**:

```python
#!/usr/bin/env python3
# custom_gradio_app.py

import gradio as gr
import subprocess
import json
from pathlib import Path
import tempfile

def process_pdf(pdf_file, backend="hybrid-auto-engine", enable_formulas=True):
    """Process PDF and return results"""

    if pdf_file is None:
        return "Please upload a PDF file", "", ""

    # Create temp output directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Process PDF
        try:
            subprocess.run([
                "mineru",
                "-p", pdf_file.name,
                "-o", temp_dir,
                "-b", backend
            ], check=True, capture_output=True, text=True)

            # Find output files
            pdf_name = Path(pdf_file.name).stem
            output_path = Path(temp_dir) / "auto" / pdf_name

            # Read markdown
            md_file = output_path / f"{pdf_name}.md"
            markdown_content = md_file.read_text(encoding='utf-8')

            # Read content_list.json
            json_file = output_path / "content_list.json"
            with open(json_file, 'r', encoding='utf-8') as f:
                content_list = json.load(f)

            # Generate summary
            summary = f"""
            📄 Processing complete!

            - Total content items: {len(content_list)}
            - Text blocks: {sum(1 for item in content_list if item.get('type') == 'text')}
            - Tables: {sum(1 for item in content_list if item.get('type') == 'table')}
            - Images: {sum(1 for item in content_list if item.get('type') == 'image')}
            - Formulas: {sum(1 for item in content_list if item.get('type') == 'formula')}
            """

            return summary, markdown_content, json.dumps(content_list, indent=2)

        except subprocess.CalledProcessError as e:
            return f"Error processing PDF: {e}", "", ""

# Create Gradio interface
with gr.Blocks(title="MinerU PDF Processor") as app:
    gr.Markdown("# MinerU PDF to Markdown Converter")
    gr.Markdown("Upload a PDF to extract structured content")

    with gr.Row():
        with gr.Column():
            pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
            backend_choice = gr.Dropdown(
                choices=["hybrid-auto-engine", "pipeline", "vlm-auto-engine"],
                value="hybrid-auto-engine",
                label="Backend"
            )
            formula_toggle = gr.Checkbox(label="Enable Formula Extraction", value=True)
            process_btn = gr.Button("Process PDF", variant="primary")

        with gr.Column():
            summary_output = gr.Textbox(label="Summary", lines=8)

    with gr.Row():
        markdown_output = gr.Textbox(label="Markdown Output", lines=15)
        json_output = gr.Textbox(label="JSON Output", lines=15)

    # Connect button to processing function
    process_btn.click(
        fn=process_pdf,
        inputs=[pdf_input, backend_choice, formula_toggle],
        outputs=[summary_output, markdown_output, json_output]
    )

# Launch app
if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860)
```

**Access**: Open browser to `http://127.0.0.1:7860`

---

## Level 5: Next Steps

### Advanced Topics to Explore

Now that you understand the fundamentals, here are advanced topics to deepen your expertise:

#### 1. Fine-Tuning and Model Customization
**What**: Adapt MinerU's models for domain-specific documents (legal, medical, scientific)

**Resources**:
- GitHub Issue #4060 discusses fine-tuning approaches
- MinerU uses YOLO for layout detection (can be retrained)
- VLM backend models can be fine-tuned on HuggingFace

**Learning Path**:
1. Understand the model architecture (read `mineru/model/` directory)
2. Prepare domain-specific labeled dataset
3. Fine-tune layout detection models
4. Evaluate on your document types

#### 2. Performance Optimization
**What**: Maximize throughput and minimize latency for production workloads

**Key Topics**:
- Multi-GPU processing with `--data-parallel-size`
- Model quantization for faster inference
- Batch processing optimization
- Caching strategies for repeated processing

**Resources**:
- [Advanced CLI Parameters](https://opendatalab.github.io/MinerU/usage/advanced_cli_parameters/)
- GitHub Discussion #3738: GPU optimization techniques
- vLLM documentation for inference optimization

**Experiment**:
```bash
# Benchmark different configurations
time mineru -p large_doc.pdf -o ./output -b pipeline
time mineru -p large_doc.pdf -o ./output -b hybrid-auto-engine
time CUDA_VISIBLE_DEVICES=0,1 mineru --data-parallel-size 2 -p large_doc.pdf -o ./output
```

#### 3. Custom Output Formats
**What**: Generate outputs beyond Markdown (DocBook, reStructuredText, custom JSON schemas)

**Approach**:
- Parse `content_list.json` with custom formatters
- Build templates for your target format
- Integrate with document generation tools (Pandoc, Sphinx)

**Mini-Project**: Build a converter from MinerU JSON to LaTeX Beamer slides

#### 4. Integration with LLM Frameworks
**What**: Connect MinerU with LangChain, LlamaIndex, or custom RAG systems

**Resources**:
- LangChain document loaders
- LlamaIndex ingestion pipelines
- RAG-Anything repository: [GitHub](https://github.com/HKUDS/RAG-Anything)

**Example Integration**:
```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# After processing with MinerU, load Markdown files
loader = DirectoryLoader('./output/auto/', glob="**/*.md")
documents = loader.load()

# Split for vector storage
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Now embed and store in vector DB
```

#### 5. Handling Edge Cases
**What**: Deal with complex documents that challenge standard processing

**Topics**:
- Cross-page table merging
- Handling vertical text and non-Latin scripts
- Processing documents with complex nested structures
- Dealing with corrupted or low-quality scans

**Resources**:
- GitHub Issues: Search for specific document types
- Community discussions on handling edge cases

### Community Resources

#### Official Channels
- **GitHub Discussions**: [opendatalab/MinerU/discussions](https://github.com/opendatalab/MinerU/discussions) - Ask questions, share use cases
- **Discord**: Active community for real-time help (check GitHub for invite)
- **GitHub Issues**: Report bugs and request features

#### Learning Resources
- [StableLearn MinerU Tutorial](https://stable-learn.com/en/mineru-tutorial/) - Comprehensive beginner's guide
- [Sonu Sahani's Blog](https://sonusahani.com/blogs/mineru) - Practical setup and usage
- [AI Innovations Blog](https://aiexpjourney.substack.com/p/from-big-picture-to-details-mineru) - Deep dive into architecture

#### Comparison Resources
- [Jimmy Song's Tool Comparison](https://jimmysong.io/blog/pdf-to-markdown-open-source-deep-dive/) - MinerU vs Marker vs MarkItDown
- [12 PDF Parsing Tools Evaluated](https://liduos.com/en/ai-develope-tools-series-2-open-source-doucment-parsing.html) - Comprehensive comparison

#### Research Papers
- [MinerU ArXiv Paper](https://ar5iv.labs.arxiv.org/html/2409.18839) - Original research paper
- OmniDocBench: Benchmark used to evaluate MinerU 2.5

### How to Get Help

**Before Asking**:
1. Check the [Official FAQ](https://opendatalab.github.io/MinerU/)
2. Search [GitHub Issues](https://github.com/opendatalab/MinerU/issues) for similar problems
3. Review [GitHub Discussions](https://github.com/opendatalab/MinerU/discussions)

**When Asking**:
1. Include MinerU version: `mineru --version`
2. Describe your environment (OS, Python version, GPU/CPU)
3. Provide a minimal reproducible example
4. Share error messages and logs
5. Mention what you've already tried

**Where to Ask**:
- **General Questions**: GitHub Discussions
- **Bugs**: GitHub Issues (with reproducible example)
- **Quick Help**: Discord community
- **Complex Issues**: Open detailed GitHub Discussion

### Hands-On Mini-Project

**Project**: Build a Research Paper Analysis Tool

**Objectives**:
1. Process a directory of academic papers
2. Extract all papers' titles, abstracts, and references
3. Identify all mathematical formulas
4. Generate a summary report with statistics
5. Create a searchable index

**Suggested Approach**:

```python
# Step 1: Batch process papers
# Use Pattern 2 from Level 4

# Step 2: Extract structured content
# Parse content_list.json for each paper

# Step 3: Identify sections
# Use heuristics or regex to find "Abstract", "References" sections

# Step 4: Extract formulas
# Filter content items where type == 'formula'

# Step 5: Generate report
# Use Pandas to create statistics DataFrame
# Generate visualizations with matplotlib

# Step 6: Build search index
# Use Whoosh or ElasticSearch for full-text search
```

**Bonus Challenges**:
- Add citation network visualization
- Implement semantic search with embeddings
- Build a web interface to explore papers
- Export results to CSV/Excel

**Expected Time**: 4-6 hours

### Continuous Learning

**Stay Updated**:
- Watch the GitHub repository for releases
- Follow MinerU on HuggingFace for model updates
- Join the Discord community for announcements

**Contribute Back**:
- Report issues you encounter
- Share your use cases in GitHub Discussions
- Contribute code improvements or documentation
- Write blog posts about your experience

**Next-Level Goals**:
1. **Week 1**: Process 100+ documents in your domain
2. **Week 2**: Build a complete RAG pipeline with MinerU
3. **Week 3**: Optimize processing speed by 50%
4. **Month 1**: Contribute a bug fix or documentation improvement
5. **Month 3**: Share a case study of your MinerU integration

---

## Congratulations! 🎉

You've completed the MinerU learning path! You now understand:

✅ What MinerU solves and when to use it
✅ How to install and run basic conversions
✅ Core concepts: backends, processing modes, content types
✅ Practical patterns for real-world applications
✅ Where to go next for advanced topics

**What's Next?**

1. **Practice**: Process documents from your domain
2. **Build**: Create a small project using MinerU
3. **Share**: Post your experience in GitHub Discussions
4. **Explore**: Dive into advanced topics that interest you

Keep learning, keep building, and welcome to the MinerU community! 🚀
