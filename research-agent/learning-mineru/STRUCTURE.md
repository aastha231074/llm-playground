# MinerU Learning Guide - Structure

## Directory Layout

```
learning-mineru/
├── README.md                  # Start here - guide overview
├── learning-path.md           # Main content (5 progressive levels)
├── resources.md               # Curated links and references
├── STRUCTURE.md              # This file
└── code-examples/            # Runnable code samples
    ├── 01-hello-world/       # Getting started
    │   ├── README.md
    │   ├── basic_conversion.sh
    │   ├── basic_conversion.py
    │   └── verify_installation.sh
    ├── 02-core-concepts/     # Understanding fundamentals
    │   ├── README.md
    │   ├── backend_comparison.py
    │   ├── processing_modes.sh
    │   └── content_extraction.py
    └── 03-patterns/          # Real-world applications
        ├── README.md
        ├── batch_processing.py
        ├── rag_pipeline.py
        └── api_server_example.py
```

## Learning Path Structure

### Level 1: Overview & Motivation (15 min)
- What MinerU solves
- Why it's better than alternatives
- Who uses it and when NOT to use it

### Level 2: Installation & Hello World (30 min)
- Prerequisites and installation
- First PDF conversion
- Verifying output

### Level 3: Core Concepts (60 min)
- Multi-backend architecture (Pipeline, Hybrid, VLM)
- Processing modes (Auto, Text, OCR)
- Hierarchical document understanding
- Multimodal content extraction
- Environment-based configuration

### Level 4: Practical Patterns (90 min)
- Single file processing
- Batch processing multiple PDFs
- Large document optimization
- RAG pipeline implementation
- REST API server
- Web UI with Gradio

### Level 5: Next Steps (30 min)
- Advanced topics to explore
- Community resources
- Getting help
- Hands-on mini-project

## Quick Start

1. **Read first**: `README.md`
2. **Main content**: `learning-path.md`
3. **Try examples**: `code-examples/01-hello-world/`
4. **Go deeper**: Follow levels 2-5 sequentially

## File Descriptions

### Root Files

- **README.md**: Overview, prerequisites, quick links
- **learning-path.md**: Complete 5-level learning guide (main content)
- **resources.md**: All links organized by source (official, community, comparisons)

### Code Examples

#### 01-hello-world/
- `basic_conversion.sh`: Simplest bash conversion
- `basic_conversion.py`: Simplest Python conversion
- `verify_installation.sh`: Check installation

#### 02-core-concepts/
- `backend_comparison.py`: Compare 3 backends (Pipeline/Hybrid/VLM)
- `processing_modes.sh`: Demo auto/text/OCR modes
- `content_extraction.py`: Extract text/tables/images/formulas

#### 03-patterns/
- `batch_processing.py`: Process multiple PDFs with tracking
- `rag_pipeline.py`: Complete RAG pipeline with chunking
- `api_server_example.py`: REST API client example

## Estimated Time Investment

- **Quick path** (basics only): 2-3 hours
- **Complete path** (all levels + practice): 6-8 hours
- **With mini-project**: +4-6 hours

## Key Features of This Guide

✅ Progressive learning (5 levels, easy to hard)
✅ Runnable code examples (not just snippets)
✅ Real-world patterns (batch, RAG, API)
✅ Complete resource collection (docs, tutorials, comparisons)
✅ Hands-on mini-project (research paper analyzer)

## What's Included

### Documentation
- Installation guide
- Core concepts explained
- API reference highlights
- Configuration examples

### Code Examples
- 8 complete, runnable scripts
- Bash and Python versions
- Error handling included
- Comments for clarity

### Resources
- Official documentation links
- Community tutorials (5+)
- Tool comparisons (3+)
- Research papers
- Try-online links

### Practical Patterns
- Batch processing
- RAG pipeline
- API integration
- Performance optimization

## Next Steps After Completion

1. ✅ Process 100+ documents in your domain
2. ✅ Build a complete RAG pipeline
3. ✅ Optimize processing speed by 50%
4. ✅ Contribute to MinerU community
5. ✅ Share your use case

---

**Current MinerU Version**: 2.7.6 (February 2026)

**Last Updated**: March 2026
