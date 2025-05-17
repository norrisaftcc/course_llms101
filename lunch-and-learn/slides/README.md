# AI For Busy Professionals - Interactive Slide Viewer

A beautiful, dark-mode Streamlit application for viewing the lunch & learn presentation slides.

## Features

✨ **Dark Mode by Default** - Easy on the eyes during presentations
🎨 **Syntax Highlighting** - Beautiful code formatting
⌨️ **Keyboard Navigation** - Use arrow keys to navigate
📱 **Responsive Design** - Works on all screen sizes
📑 **Slide Overview** - Jump to any slide instantly
📝 **Speaker Notes** - Toggle visibility of presenter notes
🎯 **Customizable** - Adjust font size and themes

## Quick Start

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the presentation:
```bash
streamlit run slide_viewer.py
```

Or use the launch script:
```bash
chmod +x run_presentation.sh
./run_presentation.sh
```

## Usage

### Navigation
- Use **←** and **→** arrow keys to navigate
- Click "Previous" and "Next" buttons
- Use the dropdown to jump to any slide
- Click slide titles in the sidebar

### Features
- **Speaker Notes**: Click the expander to show/hide
- **Font Size**: Adjust in the sidebar
- **Theme**: Switch between Dark, Light, and High Contrast

### Presentation Mode
1. Press `F11` for fullscreen
2. Hide the sidebar by clicking the `×`
3. Use arrow keys to navigate
4. Press `Esc` to exit fullscreen

## Customization

### Styling
Edit the CSS in `slide_viewer.py` to customize:
- Colors
- Fonts
- Spacing
- Animations

### Content
Slides are loaded from markdown files in the same directory:
- `01-title-slide.md`
- `02-hook-slide.md`
- etc.

## Tips for Presenters

1. **Test First**: Run through all slides before presenting
2. **Check Links**: Ensure all demo links work
3. **Prepare Backups**: Have static slides ready
4. **Practice Timing**: Use speaker notes for pacing
5. **Engage Audience**: Use interactive elements

## Troubleshooting

**Slides not loading?**
- Check that markdown files are in the same directory
- Ensure file names follow the pattern: `XX-name.md`

**Styling issues?**
- Clear browser cache
- Try a different browser
- Check for CSS conflicts

**Performance issues?**
- Reduce number of images
- Optimize markdown content
- Use a modern browser

## Development

To modify the viewer:

1. Edit `slide_viewer.py`
2. Test changes locally
3. Commit to repository

## License

MIT License - See repository root for details