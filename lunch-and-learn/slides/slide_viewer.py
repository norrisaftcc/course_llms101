"""
Streamlit Slide Viewer for Lunch & Learn Presentation
Features: Dark mode, navigation, attractive styling
"""

import streamlit as st
import os
from pathlib import Path
import re

# Page config - MUST be first Streamlit command
st.set_page_config(
    page_title="AI For Busy Professionals - Slides",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark mode and styling
st.markdown("""
<style>
    /* Dark mode by default */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* Code blocks styling */
    .stMarkdown pre {
        background-color: #1e1e1e;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 15px;
        overflow-x: auto;
    }
    
    /* Headers styling */
    .stMarkdown h1 {
        color: #06FFA5;
        font-size: 3em;
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        border-bottom: 3px solid #06FFA5;
    }
    
    .stMarkdown h2 {
        color: #2E86AB;
        font-size: 2.2em;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    
    .stMarkdown h3 {
        color: #A7DAFF;
        font-size: 1.8em;
        margin-top: 20px;
    }
    
    /* Box styling for ASCII art */
    .stMarkdown pre code {
        color: #06FFA5;
        font-family: 'Courier New', monospace;
        font-size: 0.9em;
        line-height: 1.4;
    }
    
    /* Table styling */
    .stMarkdown table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
    }
    
    .stMarkdown th {
        background-color: #2E86AB;
        color: white;
        padding: 12px;
        text-align: left;
        border: 1px solid #444;
    }
    
    .stMarkdown td {
        padding: 10px;
        border: 1px solid #444;
        background-color: #1e1e1e;
    }
    
    /* Lists styling */
    .stMarkdown ul, .stMarkdown ol {
        margin-left: 30px;
        line-height: 1.8;
    }
    
    .stMarkdown li {
        margin-bottom: 10px;
    }
    
    /* Links */
    .stMarkdown a {
        color: #06FFA5;
        text-decoration: none;
    }
    
    .stMarkdown a:hover {
        text-decoration: underline;
    }
    
    /* Emphasis styling */
    .stMarkdown strong {
        color: #FFB000;
        font-weight: bold;
    }
    
    .stMarkdown em {
        color: #A7DAFF;
        font-style: italic;
    }
    
    /* Blockquote styling */
    .stMarkdown blockquote {
        border-left: 4px solid #06FFA5;
        padding-left: 20px;
        margin: 20px 0;
        color: #A7DAFF;
        font-style: italic;
    }
    
    /* Navigation buttons */
    .navigation-button {
        background-color: #2E86AB;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.1em;
        margin: 10px;
    }
    
    .navigation-button:hover {
        background-color: #06FFA5;
        color: #0e1117;
    }
    
    /* Speaker notes styling */
    .speaker-notes {
        background-color: #1e1e1e;
        border: 2px solid #444;
        border-radius: 10px;
        padding: 20px;
        margin-top: 30px;
        font-style: italic;
        color: #A7DAFF;
    }
    
    /* Slide number */
    .slide-number {
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #2E86AB;
        color: white;
        padding: 10px 15px;
        border-radius: 5px;
        font-weight: bold;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .stMarkdown h1 {
            font-size: 2em;
        }
        .stMarkdown h2 {
            font-size: 1.5em;
        }
    }
</style>
""", unsafe_allow_html=True)

# Load slides from markdown files
def load_slides():
    slides_dir = Path(__file__).parent
    slide_files = sorted([f for f in slides_dir.glob("*.md") if f.name != "00-deck-overview.md"])
    
    slides = []
    for file in slide_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract title from first H1
            title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file.stem
            slides.append({
                'file': file.name,
                'title': title,
                'content': content
            })
    
    return slides

# Navigation state
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

slides = load_slides()

# Header with navigation
col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    if st.button("⬅️ Previous", disabled=st.session_state.slide_index == 0):
        st.session_state.slide_index -= 1
        st.rerun()

with col2:
    st.markdown(f"<h2 style='text-align: center;'>Slide {st.session_state.slide_index + 1} of {len(slides)}</h2>", unsafe_allow_html=True)

with col3:
    if st.button("Next ➡️", disabled=st.session_state.slide_index == len(slides) - 1):
        st.session_state.slide_index += 1
        st.rerun()

# Slide selector
selected_slide = st.selectbox(
    "Jump to slide:",
    range(len(slides)),
    index=st.session_state.slide_index,
    format_func=lambda x: f"{x+1}. {slides[x]['title']}",
    key="slide_selector"
)

if selected_slide != st.session_state.slide_index:
    st.session_state.slide_index = selected_slide
    st.rerun()

# Display current slide
current_slide = slides[st.session_state.slide_index]

# Main content area
st.markdown("---")

# Process the markdown content for better display
content = current_slide['content']

# Split content into main slide and speaker notes
parts = content.split("**Speaker Notes:**")
main_content = parts[0]
speaker_notes = parts[1] if len(parts) > 1 else None

# Display main slide content
st.markdown(main_content)

# Display speaker notes if they exist
if speaker_notes:
    with st.expander("📝 Speaker Notes", expanded=False):
        st.markdown(f"<div class='speaker-notes'>{speaker_notes}</div>", unsafe_allow_html=True)

# Keyboard shortcuts
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    Navigation: Use arrow keys ← → or buttons above | Press 'f' for fullscreen
</div>
""", unsafe_allow_html=True)

# Add keyboard navigation
st.markdown("""
<script>
document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowLeft') {
        const prevButton = document.querySelector('button:contains("Previous")');
        if (prevButton && !prevButton.disabled) {
            prevButton.click();
        }
    } else if (event.key === 'ArrowRight') {
        const nextButton = document.querySelector('button:contains("Next")');
        if (nextButton && !nextButton.disabled) {
            nextButton.click();
        }
    }
});
</script>
""", unsafe_allow_html=True)

# Sidebar with all slides
with st.sidebar:
    st.markdown("### 📑 All Slides")
    for i, slide in enumerate(slides):
        if st.button(f"{i+1}. {slide['title']}", key=f"sidebar_{i}"):
            st.session_state.slide_index = i
            st.rerun()
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    
    # Font size selector
    font_size = st.slider("Font Size", 12, 24, 16)
    st.markdown(f"""
    <style>
        .stMarkdown p, .stMarkdown li {{
            font-size: {font_size}px;
        }}
    </style>
    """, unsafe_allow_html=True)
    
    # Theme selector (though we default to dark)
    theme = st.selectbox("Theme", ["Dark (Default)", "Light", "High Contrast"])
    
    if theme == "Light":
        st.markdown("""
        <style>
            .stApp {
                background-color: #ffffff;
                color: #000000;
            }
            .stMarkdown pre {
                background-color: #f5f5f5;
                border-color: #ddd;
            }
        </style>
        """, unsafe_allow_html=True)
    elif theme == "High Contrast":
        st.markdown("""
        <style>
            .stApp {
                background-color: #000000;
                color: #ffffff;
            }
            .stMarkdown h1, .stMarkdown h2 {
                color: #ffff00;
            }
        </style>
        """, unsafe_allow_html=True)