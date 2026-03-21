#!/usr/bin/env python3
"""
batch_processing.py - Process multiple PDFs efficiently

This script demonstrates how to batch process a directory of PDFs,
with progress tracking and error handling.

Usage: python batch_processing.py <input-directory> [output-directory]
"""

import sys
import subprocess
from pathlib import Path
from typing import List, Dict
import json
import time


def find_pdf_files(directory: str) -> List[Path]:
    """Find all PDF files in directory"""
    dir_path = Path(directory)

    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    pdf_files = list(dir_path.glob("*.pdf"))

    # Also check subdirectories
    pdf_files.extend(dir_path.glob("**/*.pdf"))

    # Remove duplicates
    pdf_files = list(set(pdf_files))

    return sorted(pdf_files)


def process_single_pdf(pdf_path: Path, output_dir: str) -> Dict:
    """Process a single PDF and return result"""
    print(f"\n{'='*60}")
    print(f"Processing: {pdf_path.name}")
    print(f"{'='*60}")

    start_time = time.time()

    try:
        result = subprocess.run(
            ["mineru", "-p", str(pdf_path), "-o", output_dir],
            check=True,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout per file
        )

        elapsed = time.time() - start_time

        # Check output
        pdf_name = pdf_path.stem
        output_path = Path(output_dir) / "auto" / pdf_name
        md_file = output_path / f"{pdf_name}.md"

        success = md_file.exists()

        if success:
            file_size = md_file.stat().st_size
            print(f"✅ Success in {elapsed:.1f}s ({file_size:,} bytes)")
        else:
            print(f"⚠️  Completed but output not found")

        return {
            'file': str(pdf_path),
            'name': pdf_path.name,
            'success': success,
            'time': elapsed,
            'size': file_size if success else 0,
            'error': None
        }

    except subprocess.TimeoutExpired:
        elapsed = time.time() - start_time
        print(f"❌ Timeout after {elapsed:.1f}s")
        return {
            'file': str(pdf_path),
            'name': pdf_path.name,
            'success': False,
            'time': elapsed,
            'error': 'Timeout (> 5 minutes)'
        }

    except subprocess.CalledProcessError as e:
        elapsed = time.time() - start_time
        print(f"❌ Failed in {elapsed:.1f}s")
        print(f"   Error: {e}")
        return {
            'file': str(pdf_path),
            'name': pdf_path.name,
            'success': False,
            'time': elapsed,
            'error': str(e)
        }


def batch_process(input_dir: str, output_dir: str = "./batch_output") -> List[Dict]:
    """Process all PDFs in directory"""
    print("="*60)
    print("BATCH PDF PROCESSING")
    print("="*60)
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")

    # Find all PDFs
    pdf_files = find_pdf_files(input_dir)
    total = len(pdf_files)

    if total == 0:
        print("\n❌ No PDF files found!")
        return []

    print(f"\nFound {total} PDF files")

    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Process each PDF
    results = []
    start_time = time.time()

    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{total}] ", end='')
        result = process_single_pdf(pdf_path, output_dir)
        results.append(result)

    total_time = time.time() - start_time

    # Print summary
    print_summary(results, total_time)

    # Save results
    save_results(results, output_dir)

    return results


def print_summary(results: List[Dict], total_time: float):
    """Print processing summary"""
    print("\n" + "="*60)
    print("BATCH PROCESSING SUMMARY")
    print("="*60)

    total = len(results)
    successful = sum(1 for r in results if r['success'])
    failed = total - successful

    print(f"\nTotal files: {total}")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"⏱️  Total time: {total_time:.1f}s ({total_time/60:.1f} min)")

    if successful > 0:
        avg_time = sum(r['time'] for r in results if r['success']) / successful
        print(f"📊 Average time per file: {avg_time:.1f}s")

        total_size = sum(r.get('size', 0) for r in results if r['success'])
        print(f"📄 Total output size: {total_size:,} bytes ({total_size/1024/1024:.1f} MB)")

    # List failed files
    if failed > 0:
        print("\n❌ Failed files:")
        for result in results:
            if not result['success']:
                print(f"   • {result['name']}: {result.get('error', 'Unknown error')}")


def save_results(results: List[Dict], output_dir: str):
    """Save processing results to JSON"""
    results_file = Path(output_dir) / "batch_results.json"

    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print(f"\n💾 Results saved to: {results_file}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python batch_processing.py <input-directory> [output-directory]")
        print("Example: python batch_processing.py ./pdfs ./output")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./batch_output"

    try:
        results = batch_process(input_dir, output_dir)

        # Exit with error code if any failed
        failed_count = sum(1 for r in results if not r['success'])
        sys.exit(1 if failed_count > 0 else 0)

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
