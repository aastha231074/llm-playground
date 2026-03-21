# Practical Patterns

Real-world examples for building production applications with MinerU.

## Files

1. **`batch_processing.py`** - Process multiple PDFs with progress tracking
2. **`rag_pipeline.py`** - Complete RAG pipeline implementation
3. **`api_server_example.py`** - REST API client example
4. **`optimization_examples.sh`** - Performance optimization techniques

## Examples

### 1. Batch Processing

Process entire directories of PDFs:

```bash
python batch_processing.py ./pdfs ./output
```

**Features:**
- Progress tracking
- Error handling
- Performance metrics
- Results summary
- JSON output with statistics

**Expected Output:**
```
BATCH PROCESSING SUMMARY
========================================
Total files: 25
✅ Successful: 23
❌ Failed: 2
⏱️  Total time: 245.3s (4.1 min)
📊 Average time per file: 10.7s
📄 Total output size: 2,456,789 bytes (2.3 MB)

💾 Results saved to: ./output/batch_results.json
```

### 2. RAG Pipeline

Prepare documents for vector databases:

```bash
python rag_pipeline.py ./research_paper.pdf --chunk-size 512 --overlap 50
```

**Features:**
- Intelligent chunking (preserves semantic boundaries)
- Table handling (separate chunks)
- Formula inclusion (inline with text)
- Metadata for each chunk
- Ready for embedding

**Output Structure:**
```json
{
  "id": "paper_chunk_0",
  "text": "# Introduction\n\nThis paper presents...",
  "document": "paper",
  "chunk_index": 0,
  "char_count": 487,
  "metadata": {
    "has_table": false,
    "has_formula": true,
    "has_image": false
  }
}
```

### 3. API Server

Use MinerU as a REST service:

**Step 1: Start server**
```bash
mineru-api --host 0.0.0.0 --port 8000
```

**Step 2: Use client**
```bash
python api_server_example.py ./document.pdf
```

**Features:**
- RESTful API integration
- Programmatic access
- Error handling
- Result formatting

**API Documentation:** http://127.0.0.1:8000/docs

### 4. Performance Optimization

GPU acceleration and multi-processing:

```bash
# Multi-GPU processing
CUDA_VISIBLE_DEVICES=0,1 mineru --data-parallel-size 2 -p large_doc.pdf -o ./output

# Page range (for testing)
mineru -p document.pdf -o ./output --start-page 0 --end-page 10

# CPU-only optimized
MINERU_DEVICE_MODE=cpu mineru -p document.pdf -o ./output -b pipeline
```

## Integration Patterns

### Pattern 1: Document Processing Service

```python
from pathlib import Path
import subprocess

class DocumentProcessor:
    def __init__(self, output_dir="./processed"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def process(self, pdf_path):
        subprocess.run([
            "mineru",
            "-p", pdf_path,
            "-o", str(self.output_dir)
        ], check=True)

        # Return structured output
        pdf_name = Path(pdf_path).stem
        return self.output_dir / "auto" / pdf_name

# Usage
processor = DocumentProcessor()
result_dir = processor.process("./document.pdf")
```

### Pattern 2: RAG System Integration

```python
# 1. Process with MinerU
from rag_pipeline import extract_with_mineru, load_content, intelligent_chunk

content_json = extract_with_mineru("paper.pdf")
content = load_content(content_json)
chunks = intelligent_chunk(content, chunk_size=512)

# 2. Generate embeddings (example with OpenAI)
from openai import OpenAI
client = OpenAI()

embeddings = []
for chunk in chunks:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk['text']
    )
    embeddings.append(response.data[0].embedding)

# 3. Store in vector database (example with FAISS)
import faiss
import numpy as np

dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# 4. Query
query_embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input="What is MinerU?"
).data[0].embedding

distances, indices = index.search(np.array([query_embedding]), k=5)
```

### Pattern 3: Microservice Architecture

```python
from fastapi import FastAPI, UploadFile
from api_server_example import MinerUAPIClient

app = FastAPI()
mineru_client = MinerUAPIClient()

@app.post("/process")
async def process_document(file: UploadFile):
    # Save uploaded file
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # Process with MinerU
    result = mineru_client.parse_pdf(temp_path)

    # Return structured result
    return {
        "filename": file.filename,
        "content": result['content_list'],
        "markdown": result['markdown']
    }
```

## Performance Tips

### For Speed
1. Use `pipeline` backend (CPU-friendly)
2. Process specific page ranges during testing
3. Disable formula/table extraction if not needed
4. Use multi-GPU with `--data-parallel-size`

### For Accuracy
1. Use `vlm-auto-engine` backend (requires GPU)
2. Specify language for OCR documents
3. Enable formula and table extraction
4. Use appropriate processing mode (auto/txt/ocr)

### For Scale
1. Implement batch processing with error handling
2. Use async/parallel processing for multiple files
3. Monitor memory usage (16GB+ recommended)
4. Consider API server for multi-user scenarios

## Common Use Cases

| Use Case | Recommended Pattern | Key Settings |
|----------|-------------------|--------------|
| **LLM Training** | Batch processing | `--method auto` |
| **RAG System** | RAG pipeline | `chunk_size=512` |
| **Web Service** | API server | FastAPI integration |
| **Large Scale** | Multi-GPU batch | `--data-parallel-size 2` |
| **Research** | Single file + analysis | `vlm-auto-engine` |

## Next Steps

1. **Customize**: Adapt patterns to your use case
2. **Integrate**: Connect with your stack (LangChain, LlamaIndex, etc.)
3. **Optimize**: Benchmark and tune for your workload
4. **Deploy**: Containerize with Docker for production

Check `learning-path.md` Level 5 for advanced topics!
