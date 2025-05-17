#!/bin/bash

# Launch the Streamlit slide viewer
echo "🚀 Launching AI For Busy Professionals Slide Viewer..."
echo "📍 Opening in your default browser..."
echo "⌨️  Use arrow keys to navigate between slides"
echo "🎯 Press Ctrl+C to exit"

# Run Streamlit
streamlit run slide_viewer.py --theme.base dark --theme.primaryColor "#06FFA5" --theme.backgroundColor "#0e1117" --theme.secondaryBackgroundColor "#1e1e1e" --theme.textColor "#ffffff"