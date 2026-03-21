#!/usr/bin/env python3
"""
backend_comparison.py - Compare different MinerU backends

This script demonstrates the three MinerU backends:
1. Pipeline - Traditional CV approach (CPU-friendly)
2. Hybrid - Balanced approach (default)
3. VLM - Vision Language Model (highest accuracy, GPU recommended)

Usage: python backend_comparison.py <pdf-path>
"""

import sys
import subprocess
import time
from pathlib import Path


def process_with_backend(pdf_path: str, backend: str, output_base: str) -> dict:
    """
    Process PDF with specific backend and measure performance

    Args:
        pdf_path: Path to PDF file
        backend: Backend to use ('pipeline', 'hybrid-auto-engine', 'vlm-auto-engine')
        output_base: Base directory for output

    Returns:
        Dictionary with processing results
    """
    output_dir = f"{output_base}_{backend.replace('-', '_')}"

    print(f"\n{'='*60}")
    print(f"Processing with backend: {backend}")
    print(f"{'='*60}")

    start_time = time.time()

    try:
        result = subprocess.run(
            ["mineru", "-p", pdf_path, "-o", output_dir, "-b", backend],
            check=True,
            capture_output=True,
            text=True
        )

        elapsed_time = time.time() - start_time

        # Get output file size
        pdf_name = Path(pdf_path).stem
        md_file = Path(output_dir) / "auto" / pdf_name / f"{pdf_name}.md"

        if md_file.exists():
            file_size = md_file.stat().st_size
        else:
            file_size = 0

        print(f"✅ Success!")
        print(f"   Time: {elapsed_time:.2f} seconds")
        print(f"   Output size: {file_size:,} bytes")

        return {
            'backend': backend,
            'success': True,
            'time': elapsed_time,
            'size': file_size,
            'output_dir': output_dir
        }

    except subprocess.CalledProcessError as e:
        elapsed_time = time.time() - start_time
        print(f"❌ Failed!")
        print(f"   Time: {elapsed_time:.2f} seconds")
        print(f"   Error: {e}")

        return {
            'backend': backend,
            'success': False,
            'time': elapsed_time,
            'error': str(e)
        }


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python backend_comparison.py <pdf-path>")
        print("Example: python backend_comparison.py ./research_paper.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not Path(pdf_path).exists():
        print(f"Error: File not found: {pdf_path}")
        sys.exit(1)

    print("MinerU Backend Comparison")
    print("="*60)
    print(f"Input: {pdf_path}")
    print()

    # Test all three backends
    backends = [
        'pipeline',           # CPU-friendly
        'hybrid-auto-engine', # Balanced (default)
        'vlm-auto-engine'     # Highest accuracy (GPU recommended)
    ]

    results = []
    output_base = "./output_comparison"

    for backend in backends:
        result = process_with_backend(pdf_path, backend, output_base)
        results.append(result)

    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    print(f"\n{'Backend':<25} {'Status':<10} {'Time (s)':<12} {'Size (bytes)':<15}")
    print("-"*60)

    for result in results:
        status = "✅ Success" if result['success'] else "❌ Failed"
        time_str = f"{result['time']:.2f}"
        size_str = f"{result.get('size', 0):,}" if result['success'] else "N/A"

        print(f"{result['backend']:<25} {status:<10} {time_str:<12} {size_str:<15}")

    # Find fastest
    successful_results = [r for r in results if r['success']]
    if successful_results:
        fastest = min(successful_results, key=lambda r: r['time'])
        print(f"\n⚡ Fastest: {fastest['backend']} ({fastest['time']:.2f}s)")

        # Find largest output (usually indicates most content extracted)
        largest = max(successful_results, key=lambda r: r['size'])
        print(f"📄 Most content: {largest['backend']} ({largest['size']:,} bytes)")

    print("\n" + "="*60)
    print("\nRecommendations:")
    print("  • Pipeline: Best for CPU-only or resource-constrained environments")
    print("  • Hybrid: Best for general use (default)")
    print("  • VLM: Best for highest accuracy, requires GPU with 20-25GB VRAM")


if __name__ == "__main__":
    main()
