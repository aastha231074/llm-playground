#!/usr/bin/env python3
"""
rag_pipeline.py - Complete RAG pipeline with MinerU

This script demonstrates a complete pipeline for preparing documents
for Retrieval-Augmented Generation (RAG):
1. Extract content with MinerU
2. Chunk content intelligently
3. Prepare for vector embedding

Usage: python rag_pipeline.py <pdf-path> [--chunk-size 512]
"""

import sys
import json
import subprocess
import argparse
from pathlib import Path
from typing import List, Dict, Optional


def extract_with_mineru(pdf_path: str, output_dir: str = "./rag_temp") -> Path:
    """Extract content from PDF using MinerU"""
    print(f"📄 Extracting content from: {pdf_path}")

    subprocess.run(
        ["mineru", "-p", pdf_path, "-o", output_dir],
        check=True,
        capture_output=True
    )

    # Return path to content_list.json
    pdf_name = Path(pdf_path).stem
    content_json = Path(output_dir) / "auto" / pdf_name / "content_list.json"

    if not content_json.exists():
        raise FileNotFoundError(f"Output not found: {content_json}")

    print(f"✅ Extraction complete")
    return content_json


def load_content(content_json: Path) -> List[Dict]:
    """Load structured content from MinerU output"""
    with open(content_json, 'r', encoding='utf-8') as f:
        return json.load(f)


def intelligent_chunk(content: List[Dict], chunk_size: int = 512, overlap: int = 50) -> List[Dict]:
    """
    Chunk content intelligently for RAG

    Strategy:
    - Keep tables as separate chunks
    - Combine text blocks until chunk_size is reached
    - Include formulas inline with text
    - Add metadata for each chunk
    """
    chunks = []
    current_chunk = {
        'text': '',
        'metadata': {
            'sources': [],
            'types': [],
            'has_table': False,
            'has_formula': False,
            'has_image': False
        }
    }

    def save_current_chunk():
        """Save current chunk if it has content"""
        if current_chunk['text'].strip():
            chunks.append({
                'text': current_chunk['text'].strip(),
                'metadata': current_chunk['metadata'].copy(),
                'char_count': len(current_chunk['text']),
                'chunk_id': len(chunks)
            })

    for idx, item in enumerate(content):
        item_type = item.get('type', 'text')

        if item_type == 'text':
            text = item.get('text', '').strip()
            if not text:
                continue

            # Check if adding this would exceed chunk size
            if len(current_chunk['text']) + len(text) > chunk_size and current_chunk['text']:
                # Save current chunk
                save_current_chunk()

                # Start new chunk with overlap
                if overlap > 0 and len(text) > overlap:
                    # Include last 'overlap' characters from previous chunk
                    overlap_text = current_chunk['text'][-overlap:] if current_chunk['text'] else ''
                    current_chunk = {
                        'text': overlap_text + '\n\n' + text,
                        'metadata': {
                            'sources': [idx],
                            'types': ['text'],
                            'has_table': False,
                            'has_formula': False,
                            'has_image': False
                        }
                    }
                else:
                    current_chunk = {
                        'text': text,
                        'metadata': {
                            'sources': [idx],
                            'types': ['text'],
                            'has_table': False,
                            'has_formula': False,
                            'has_image': False
                        }
                    }
            else:
                # Add to current chunk
                if current_chunk['text']:
                    current_chunk['text'] += '\n\n'
                current_chunk['text'] += text
                current_chunk['metadata']['sources'].append(idx)
                current_chunk['metadata']['types'].append('text')

        elif item_type == 'table':
            # Tables get their own chunk
            save_current_chunk()

            # Create table chunk
            table_text = f"[TABLE]\n{item.get('html', '')}"
            chunks.append({
                'text': table_text,
                'metadata': {
                    'sources': [idx],
                    'types': ['table'],
                    'has_table': True,
                    'has_formula': False,
                    'has_image': False
                },
                'char_count': len(table_text),
                'chunk_id': len(chunks),
                'special_type': 'table'
            })

            # Reset current chunk
            current_chunk = {
                'text': '',
                'metadata': {
                    'sources': [],
                    'types': [],
                    'has_table': False,
                    'has_formula': False,
                    'has_image': False
                }
            }

        elif item_type == 'formula':
            # Include formulas inline
            latex = item.get('latex', '')
            formula_text = f"$${latex}$$"

            if current_chunk['text']:
                current_chunk['text'] += '\n\n'
            current_chunk['text'] += formula_text
            current_chunk['metadata']['sources'].append(idx)
            current_chunk['metadata']['types'].append('formula')
            current_chunk['metadata']['has_formula'] = True

        elif item_type == 'image':
            # Add image reference
            image_path = item.get('image_path', '')
            caption = item.get('caption', 'Image')

            image_text = f"[IMAGE: {caption}]\nPath: {image_path}"

            if current_chunk['text']:
                current_chunk['text'] += '\n\n'
            current_chunk['text'] += image_text
            current_chunk['metadata']['sources'].append(idx)
            current_chunk['metadata']['types'].append('image')
            current_chunk['metadata']['has_image'] = True

    # Don't forget last chunk
    save_current_chunk()

    return chunks


def prepare_for_embedding(chunks: List[Dict], pdf_path: str) -> List[Dict]:
    """
    Prepare chunks for vector embedding

    Adds document-level metadata and formats for embedding
    """
    pdf_name = Path(pdf_path).stem
    prepared_chunks = []

    for chunk in chunks:
        prepared_chunks.append({
            'id': f"{pdf_name}_chunk_{chunk['chunk_id']}",
            'text': chunk['text'],
            'document': pdf_name,
            'document_path': pdf_path,
            'chunk_index': chunk['chunk_id'],
            'char_count': chunk['char_count'],
            'metadata': chunk['metadata'],
            'special_type': chunk.get('special_type', 'text')
        })

    return prepared_chunks


def save_chunks(chunks: List[Dict], output_file: str):
    """Save chunks to JSON file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved {len(chunks)} chunks to: {output_file}")


def print_statistics(chunks: List[Dict]):
    """Print chunk statistics"""
    print(f"\n{'='*60}")
    print("CHUNKING STATISTICS")
    print(f"{'='*60}\n")

    print(f"Total chunks: {len(chunks)}")

    # Count special types
    table_chunks = sum(1 for c in chunks if c['metadata'].get('has_table', False))
    formula_chunks = sum(1 for c in chunks if c['metadata'].get('has_formula', False))
    image_chunks = sum(1 for c in chunks if c['metadata'].get('has_image', False))

    print(f"Text chunks: {len(chunks) - table_chunks}")
    print(f"Table chunks: {table_chunks}")
    print(f"Chunks with formulas: {formula_chunks}")
    print(f"Chunks with images: {image_chunks}")

    # Size statistics
    char_counts = [c['char_count'] for c in chunks]
    avg_size = sum(char_counts) / len(char_counts) if char_counts else 0
    min_size = min(char_counts) if char_counts else 0
    max_size = max(char_counts) if char_counts else 0

    print(f"\nChunk sizes (characters):")
    print(f"  Average: {avg_size:.0f}")
    print(f"  Min: {min_size}")
    print(f"  Max: {max_size}")

    # Show first chunk as example
    if chunks:
        print(f"\n{'='*60}")
        print("FIRST CHUNK EXAMPLE")
        print(f"{'='*60}\n")
        print(f"ID: {chunks[0]['id']}")
        print(f"Text preview: {chunks[0]['text'][:200]}...")
        print(f"Metadata: {json.dumps(chunks[0]['metadata'], indent=2)}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="RAG pipeline with MinerU")
    parser.add_argument('pdf_path', help="Path to PDF file")
    parser.add_argument('--chunk-size', type=int, default=512, help="Target chunk size (default: 512)")
    parser.add_argument('--overlap', type=int, default=50, help="Chunk overlap (default: 50)")
    parser.add_argument('--output', default='./rag_chunks.json', help="Output file (default: ./rag_chunks.json)")

    args = parser.parse_args()

    if not Path(args.pdf_path).exists():
        print(f"❌ Error: File not found: {args.pdf_path}")
        sys.exit(1)

    print("="*60)
    print("RAG PIPELINE WITH MINERU")
    print("="*60)
    print(f"Input: {args.pdf_path}")
    print(f"Chunk size: {args.chunk_size}")
    print(f"Overlap: {args.overlap}")
    print(f"Output: {args.output}")
    print()

    # Step 1: Extract content
    content_json = extract_with_mineru(args.pdf_path)

    # Step 2: Load content
    print("📖 Loading content...")
    content = load_content(content_json)
    print(f"✅ Loaded {len(content)} content items")

    # Step 3: Chunk intelligently
    print(f"✂️  Chunking with size={args.chunk_size}, overlap={args.overlap}...")
    chunks = intelligent_chunk(content, args.chunk_size, args.overlap)
    print(f"✅ Created {len(chunks)} chunks")

    # Step 4: Prepare for embedding
    print("🔧 Preparing for embedding...")
    prepared_chunks = prepare_for_embedding(chunks, args.pdf_path)
    print(f"✅ Prepared {len(prepared_chunks)} chunks")

    # Step 5: Save
    save_chunks(prepared_chunks, args.output)

    # Print statistics
    print_statistics(prepared_chunks)

    print(f"\n{'='*60}")
    print("✅ RAG pipeline complete!")
    print()
    print("Next steps:")
    print("  1. Load chunks from JSON file")
    print("  2. Generate embeddings (OpenAI, HuggingFace, etc.)")
    print("  3. Store in vector database (Pinecone, Weaviate, FAISS, etc.)")
    print("  4. Build retrieval interface")


if __name__ == "__main__":
    main()
