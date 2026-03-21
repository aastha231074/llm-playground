# MinerU Resources

A curated collection of links organized by source type.

## Official Documentation

### Core Documentation
- [Official MinerU Documentation](https://opendatalab.github.io/MinerU/) - Main documentation site
- [Quick Start Guide](https://opendatalab.github.io/MinerU/quick_start/) - Installation and setup
- [Quick Usage](https://opendatalab.github.io/MinerU/usage/quick_usage/) - Basic command usage
- [CLI Tools Documentation](https://opendatalab.github.io/MinerU/usage/cli_tools/) - Command-line reference
- [Advanced CLI Parameters](https://opendatalab.github.io/MinerU/usage/advanced_cli_parameters/) - GPU optimization and multi-processing
- [Model Source Configuration](https://opendatalab.github.io/MinerU/usage/model_source/) - Model management
- [Output File Format Reference](https://opendatalab.github.io/MinerU/reference/output_files/) - JSON structure and formats

### Repository & Code
- [GitHub Repository](https://github.com/opendatalab/MinerU) - Source code and issues
- [GitHub Discussions](https://github.com/opendatalab/MinerU/discussions) - Community Q&A
- [PyPI Package](https://pypi.org/project/mineru/) - Python package index
- [GitHub Releases](https://github.com/opendatalab/MinerU/releases) - Version history and changelog

### Research & Papers
- [MinerU ArXiv Paper](https://ar5iv.labs.arxiv.org/html/2409.18839) - Academic paper with technical details
- [MinerU on HuggingFace Papers](https://huggingface.co/papers/2409.18839) - Paper discussion

### Try Online
- [MinerU.net](https://mineru.net/) - Zero-install web version
- [HuggingFace Space Demo](https://huggingface.co/spaces/opendatalab/MinerU) - Interactive demo (up to 20 pages)

---

## Community Tutorials

### Comprehensive Guides
- [MinerU Beginner's Guide - StableLearn](https://stable-learn.com/en/mineru-tutorial/)
  - Installation with conda/pip
  - GPU acceleration setup
  - Python API implementation with error handling

- [Extract Any PDF with MinerU 2.5 - Sonu Sahani](https://sonusahani.com/blogs/mineru)
  - Step-by-step setup for Linux/Windows/macOS
  - Performance benchmarks across languages
  - vLLM support configuration

### Architecture & Technical Deep Dives
- [From Big Picture to Details: MinerU 2.5 Redefines Document Parsing](https://aiexpjourney.substack.com/p/from-big-picture-to-details-mineru)
  - Two-stage approach explained
  - Global layout understanding vs fine-grained content recognition

- [Unlocking Data: The Power of MinerU in Document Processing](https://www.oreateai.com/blog/unlocking-data-the-power-of-mineru-in-document-processing/)
  - Real-world applications
  - Magic-PDF and Magic-Doc components

- [MinerU: Turns Any PDF Into LLM-ready Markdown](https://medevel.com/mineru/)
  - LLM integration focus

### Literature Reviews
- [MinerU Literature Review - The Moonlight](https://www.themoonlight.io/en/review/mineru-an-open-source-solution-for-precise-document-content-extraction)
  - Comprehensive academic review

- [MinerU Document Parsing Tool - Efficient Coder](https://www.xugj520.cn/en/archives/mineru-document-parsing-tool-pdf-markdown-conversion.html)
  - Scientific literature processing focus

---

## Comparison Articles

### Tool Comparisons
- [Best Open Source PDF to Markdown Tools (2026): Marker vs MinerU vs MarkItDown](https://jimmysong.io/blog/pdf-to-markdown-open-source-deep-dive/)
  - **Key Insight**: MinerU excels at complex tables, formulas, and academic papers but requires more resources

- [12 Open-Source PDF Parsing & OCR Tools Evaluated](https://liduos.com/en/ai-develope-tools-series-2-open-source-doucment-parsing.html)
  - **Result**: MinerU ranked #1 among 12 tools
  - Recommended as base for custom document parsing solutions

- [Which is the Best Model for Document Parsing? - 302.AI](https://medium.com/@302.AI/which-is-the-best-model-for-document-parsing-65405b7d7877)
  - Comparative analysis across approaches

- [MinerU Alternatives Directory](https://alternativeto.net/software/mineru/)
  - Community-curated alternatives

### Strengths vs Alternatives

| Tool | Best For | Tradeoffs |
|------|----------|-----------|
| **MinerU** | Academic papers, complex tables, formulas, multi-language OCR (109 languages) | Higher resource usage, GPU recommended |
| **Marker** | Image preservation, fast processing, multiple interfaces | GPL license (commercial requires authorization), weaker table/formula support |
| **MarkItDown** | Multi-format support (Word, PPT, Excel), easy installation | PDF handling is basic text-only, no structure preservation |

---

## Community Channels

### Official Support
- **GitHub Discussions**: [MinerU Discussions](https://github.com/opendatalab/MinerU/discussions) - Technical Q&A
- **GitHub Issues**: [Issue Tracker](https://github.com/opendatalab/MinerU/issues) - Bug reports and feature requests
- **Discord**: Active community support (check GitHub for invite link)
- **WeChat**: Chinese-language community support

### Broader Tech Community
- **Hacker News**: [Discussion Thread](https://news.ycombinator.com/item?id=41274578) - Community feedback and use cases
- **DeepWiki**: [Community Documentation](https://deepwiki.com/opendatalab/MinerU) - Collaborative knowledge base

---

## Common Issues & Solutions

### GitHub Discussion Highlights
- [MinerU Invocation Problem](https://github.com/opendatalab/MinerU/discussions/2961) - Deployment troubleshooting
- [Inquiries Regarding MinerU](https://github.com/opendatalab/MinerU/discussions/3977) - General Q&A
- [Language Confusion Issue](https://github.com/opendatalab/MinerU/discussions/3986) - Multilingual processing
- [Performance Issues](https://github.com/opendatalab/MinerU/discussions/1226) - Speed optimization
- [GPU Optimization](https://github.com/opendatalab/MinerU/discussions/3738) - Hardware acceleration

### Known Gotchas
1. **Python Version**: Windows requires Python 3.10-3.12 (Ray dependency limitation)
2. **macOS Requirement**: Version 14.0+ required
3. **Language Mixing**: VLM backend may hallucinate characters in non-Chinese/English documents
4. **Complex Tables**: May misidentify rows/columns in very complex layouts
5. **AGPL-3.0 License**: Contains AGPL-licensed YOLO models (team plans to replace)

**Pro Tip**: Always check the [Official FAQ](https://opendatalab.github.io/MinerU/) before troubleshooting!

---

## Real-World Use Cases

### By Industry
- **Academic Research**: Converting papers with charts and equations for analysis
- **Legal**: Streamlining contract review and document processing
- **Finance**: Extracting data from industry reports and financial documentation
- **Knowledge Management**: Building custom knowledge engines and RAG systems

### Community Testimonials
> "MinerU is hands-down the best PDF extraction tool" - Hacker News Community

> "MinerU 2.5 processed documents quickly and produced high-quality structure-preserving outputs. I rely on it for building custom datasets." - Sonu Sahani, Developer

> "Despite some limitations, the reviewer still highly recommends this project as first choice among open-source PDF parsers" - Meursault, Tool Evaluator

---

## Blog Posts & Articles

- [AI Innovations and Insights 29: EdgeRAG and MinerU](https://medium.com/ai-exploration-journey/ai-innovations-and-insights-29-edgerag-and-mineru-0981310ac30e)
- [RAG-Anything GitHub Repository](https://github.com/HKUDS/RAG-Anything) - Integration examples

---

## Version History

- **2.7.6** (Feb 2026) - Domestic computing platform support (Kunlunxin, Tecorigin)
- **2.7.5** - PDF rendering timeout detection fixes
- **2.7.0** - Hybrid backend as default, cross-page table merging
- **2.6.3** (Jan 2026) - vlm-mlx-engine backend for Apple Silicon (100-200% speed boost)
- **2.5.0** (Sept 2025) - Major release surpassing Gemini 2.5 Pro and GPT-4o on OmniDocBench

---

**Last Updated**: March 2026

For the most current information, always refer to the [Official Documentation](https://opendatalab.github.io/MinerU/).
