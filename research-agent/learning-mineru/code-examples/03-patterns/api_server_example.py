#!/usr/bin/env python3
"""
api_server_example.py - Example REST API client for MinerU

This script demonstrates how to:
1. Start MinerU API server
2. Upload and process PDFs via REST API
3. Retrieve results programmatically

Prerequisites:
- MinerU installed with API support
- Start server first: mineru-api --host 0.0.0.0 --port 8000

Usage: python api_server_example.py <pdf-path>
"""

import sys
import requests
from pathlib import Path
import json
import time


class MinerUAPIClient:
    """Client for MinerU REST API"""

    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url
        self.session = requests.Session()

    def health_check(self) -> bool:
        """Check if API server is running"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def parse_pdf(
        self,
        pdf_path: str,
        backend: str = "hybrid-auto-engine",
        method: str = "auto",
        formula_enable: bool = True,
        table_enable: bool = True
    ) -> dict:
        """
        Upload and parse PDF

        Args:
            pdf_path: Path to PDF file
            backend: Processing backend
            method: Processing method (auto/txt/ocr)
            formula_enable: Enable formula extraction
            table_enable: Enable table extraction

        Returns:
            Dictionary with parsing results
        """
        pdf_file = Path(pdf_path)

        if not pdf_file.exists():
            raise FileNotFoundError(f"File not found: {pdf_path}")

        print(f"📤 Uploading: {pdf_file.name}")
        print(f"   Backend: {backend}")
        print(f"   Method: {method}")
        print(f"   Formulas: {formula_enable}")
        print(f"   Tables: {table_enable}")

        # Prepare request
        with open(pdf_file, 'rb') as f:
            files = {
                'file': (pdf_file.name, f, 'application/pdf')
            }

            data = {
                'backend': backend,
                'method': method,
                'formula_enable': str(formula_enable).lower(),
                'table_enable': str(table_enable).lower()
            }

            # Send request
            start_time = time.time()
            response = self.session.post(
                f"{self.base_url}/file_parse",
                files=files,
                data=data,
                timeout=300  # 5 minute timeout
            )
            elapsed = time.time() - start_time

        # Check response
        response.raise_for_status()

        print(f"✅ Processing complete in {elapsed:.1f}s")

        return response.json()

    def parse_pdf_async(self, pdf_path: str, **kwargs) -> str:
        """
        Start async PDF processing (if supported)

        Returns job ID for checking status later
        """
        # Note: This endpoint may not be available in all versions
        # Check API documentation at http://127.0.0.1:8000/docs
        raise NotImplementedError("Async processing not yet implemented")


def format_result(result: dict):
    """Format and display parsing result"""
    print(f"\n{'='*60}")
    print("PARSING RESULTS")
    print(f"{'='*60}\n")

    # Check result structure
    if 'markdown' in result:
        markdown = result['markdown']
        print(f"Markdown output ({len(markdown)} characters):")
        print("-" * 40)
        print(markdown[:500] + "..." if len(markdown) > 500 else markdown)
        print()

    if 'content_list' in result:
        content_list = result['content_list']
        print(f"Content items: {len(content_list)}")

        # Count by type
        from collections import Counter
        types = Counter(item.get('type', 'unknown') for item in content_list)

        print("\nContent breakdown:")
        for content_type, count in types.items():
            print(f"  {content_type}: {count}")
        print()

    if 'metadata' in result:
        print("Metadata:")
        print(json.dumps(result['metadata'], indent=2))


def save_result(result: dict, output_file: str = "./api_result.json"):
    """Save API result to file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"💾 Full result saved to: {output_file}")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python api_server_example.py <pdf-path>")
        print()
        print("Prerequisites:")
        print("  1. Start API server: mineru-api --host 0.0.0.0 --port 8000")
        print("  2. Access API docs: http://127.0.0.1:8000/docs")
        print()
        print("Example:")
        print("  python api_server_example.py ./research_paper.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]

    print("="*60)
    print("MINERU API CLIENT EXAMPLE")
    print("="*60)
    print()

    # Create client
    client = MinerUAPIClient()

    # Check if server is running
    print("🔍 Checking API server...")
    if not client.health_check():
        print("❌ API server not responding at http://127.0.0.1:8000")
        print()
        print("Please start the server first:")
        print("  mineru-api --host 0.0.0.0 --port 8000")
        print()
        print("API documentation will be available at:")
        print("  http://127.0.0.1:8000/docs")
        sys.exit(1)

    print("✅ API server is running")
    print()

    # Parse PDF
    try:
        result = client.parse_pdf(
            pdf_path,
            backend="hybrid-auto-engine",
            method="auto",
            formula_enable=True,
            table_enable=True
        )

        # Display results
        format_result(result)

        # Save results
        save_result(result)

        print(f"\n{'='*60}")
        print("✅ Example complete!")
        print()
        print("Integration tips:")
        print("  • Use client.parse_pdf() in your application")
        print("  • Handle timeouts for large documents")
        print("  • Parse content_list for structured access")
        print("  • Check API docs for all available endpoints")

    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
        sys.exit(130)


if __name__ == "__main__":
    main()
