# Launch Instructions for Slide Viewer

## Quick Launch Steps

1. **Open Terminal**
   ```bash
   cd /Users/norrisa/Documents/dev/github/course_llms101/lunch-and-learn/slides
   ```

2. **Install Requirements** (if not already done)
   ```bash
   pip install streamlit
   ```

3. **Launch the App**
   ```bash
   streamlit run slide_viewer.py
   ```

   OR use the launch script:
   ```bash
   ./run_presentation.sh
   ```

## What Will Happen

1. Streamlit will start the server
2. Your default browser will open automatically
3. The slide viewer will load with:
   - Dark mode enabled
   - First slide displayed
   - Navigation controls ready

## Navigation Tips

- Use ← → arrow keys to navigate
- Click on slide titles in sidebar
- Use dropdown to jump to any slide
- Adjust font size in sidebar
- Toggle speaker notes with expander

## Troubleshooting

If the browser doesn't open automatically:
- Look for the URL in terminal (usually http://localhost:8501)
- Copy and paste it into your browser

If you get an error:
- Make sure you're in the correct directory
- Check that all markdown slide files are present
- Ensure Streamlit is installed: `pip install streamlit`

## Ready to Launch?

Just run this command:
```bash
cd /Users/norrisa/Documents/dev/github/course_llms101/lunch-and-learn/slides && streamlit run slide_viewer.py
```

The app should open in your browser within seconds!