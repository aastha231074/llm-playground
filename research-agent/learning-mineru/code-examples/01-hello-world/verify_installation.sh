#!/bin/bash
# verify_installation.sh - Check if MinerU is installed correctly

echo "🔍 Verifying MinerU Installation..."
echo ""

# Check Python version
echo "1. Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1)
echo "   $PYTHON_VERSION"

# Check if mineru command exists
echo ""
echo "2. Checking if mineru command is available..."
if command -v mineru &> /dev/null; then
    echo "   ✅ mineru command found"
    MINERU_VERSION=$(mineru --version 2>&1 || echo "Version check failed")
    echo "   $MINERU_VERSION"
else
    echo "   ❌ mineru command not found"
    echo "   Please install MinerU: pip install -U 'mineru[all]'"
    exit 1
fi

# Check if mineru-api is available
echo ""
echo "3. Checking if mineru-api is available..."
if command -v mineru-api &> /dev/null; then
    echo "   ✅ mineru-api command found"
else
    echo "   ❌ mineru-api command not found"
fi

# Check if mineru-gradio is available
echo ""
echo "4. Checking if mineru-gradio is available..."
if command -v mineru-gradio &> /dev/null; then
    echo "   ✅ mineru-gradio command found"
else
    echo "   ❌ mineru-gradio command not found"
fi

# Check GPU availability (optional)
echo ""
echo "5. Checking GPU availability (optional)..."
if command -v nvidia-smi &> /dev/null; then
    GPU_INFO=$(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>&1)
    echo "   ✅ NVIDIA GPU detected:"
    echo "   $GPU_INFO"
else
    echo "   ⚠️  No NVIDIA GPU detected (CPU-only mode available)"
fi

echo ""
echo "✅ Installation verification complete!"
echo ""
echo "Next steps:"
echo "  1. Try basic conversion: ./basic_conversion.sh <your-pdf-file>"
echo "  2. Check out examples in code-examples/ directory"
echo "  3. Read learning-path.md for comprehensive guide"
