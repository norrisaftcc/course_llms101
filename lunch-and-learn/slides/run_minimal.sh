#!/bin/bash

# Launch the minimal retro slide viewer
echo "🖥️  Launching Retro Terminal Slide Viewer..."
echo "🎯 Arrow keys to navigate"
echo "⚡ Press Ctrl+C to exit"

# Run Streamlit with minimal UI
streamlit run slide_viewer_minimal.py \
    --theme.base dark \
    --theme.primaryColor "#00ff00" \
    --theme.backgroundColor "#000000" \
    --theme.secondaryBackgroundColor "#0a0a0a" \
    --theme.textColor "#00ff00" \
    --theme.font "monospace" \
    --client.showErrorDetails false \
    --client.toolbarMode minimal