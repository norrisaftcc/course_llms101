"""
Minimal Retro Slide Viewer - Clean presentation mode
ASCII art with proper fixed-width font display
"""

import streamlit as st
from pathlib import Path
import re

st.set_page_config(
    page_title="AI For Busy Professionals",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Retro terminal CSS with proper monospace fonts
st.markdown("""
<style>
    /* Hide Streamlit UI elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Terminal green theme */
    .stApp {
        background-color: #000000;
        color: #00ff00;
        padding: 0;
    }
    
    /* Container for centering */
    .main-container {
        max-width: 1000px;
        margin: 40px auto;
        padding: 20px;
    }
    
    /* All text monospace by default */
    * {
        font-family: 'Courier New', Courier, 'Lucida Console', monospace !important;
    }
    
    /* Slide title */
    h1 {
        color: #00ff00;
        text-align: center;
        font-size: 2.2em;
        margin-bottom: 40px;
        padding: 20px;
        border: 3px double #00ff00;
        background: #000000;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    h2 {
        color: #ffff00;
        font-size: 1.6em;
        margin: 30px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 2px solid #ffff00;
    }
    
    h3 {
        color: #00ffff;
        font-size: 1.3em;
        margin: 20px 0;
    }
    
    /* Paragraphs and lists */
    p, li {
        font-size: 1.1em;
        line-height: 1.6;
        margin: 15px 0;
    }
    
    ul, ol {
        margin-left: 30px;
    }
    
    /* Code blocks and ASCII art */
    pre, code {
        background: #000000 !important;
        color: #00ff00 !important;
        border: 1px solid #00ff00;
        padding: 15px !important;
        font-size: 14px !important;
        line-height: 1.2 !important;
        overflow-x: auto;
        white-space: pre !important;
        display: block;
        margin: 20px 0;
    }
    
    /* Tables */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }
    
    th {
        background: #00ff00;
        color: #000000;
        padding: 12px;
        text-align: left;
        font-weight: bold;
    }
    
    td {
        border: 1px solid #00ff00;
        padding: 10px;
        color: #00ff00;
    }
    
    /* Strong text */
    strong {
        color: #ffff00;
        font-weight: bold;
    }
    
    /* Links */
    a {
        color: #00ffff;
        text-decoration: underline;
    }
    
    /* Navigation */
    .bottom-nav {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        background: #000000;
        border: 2px solid #00ff00;
        padding: 15px 30px;
        display: flex;
        gap: 30px;
        align-items: center;
        z-index: 1000;
    }
    
    .nav-btn {
        background: #000000;
        color: #00ff00;
        border: 1px solid #00ff00;
        padding: 8px 20px;
        cursor: pointer;
        font-size: 16px;
        transition: all 0.2s;
    }
    
    .nav-btn:hover {
        background: #00ff00;
        color: #000000;
    }
    
    .nav-btn:disabled {
        opacity: 0.4;
        cursor: not-allowed;
    }
    
    .slide-num {
        color: #ffff00;
        font-size: 18px;
        font-weight: bold;
    }
    
    /* Hide Streamlit elements */
    .stButton button {
        visibility: hidden;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 2px solid #00ff00;
    }
    
    /* Keyboard hint */
    .kbd-hint {
        position: fixed;
        top: 20px;
        right: 20px;
        color: #666;
        font-size: 14px;
    }
    
    /* ASCII art special handling */
    .ascii-content {
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 13px !important;
        line-height: 1.1 !important;
        color: #00ff00;
        white-space: pre !important;
    }
</style>
""", unsafe_allow_html=True)

# Load slides
@st.cache_data
def load_slides():
    slides_dir = Path(__file__).parent
    slide_files = sorted([f for f in slides_dir.glob("*.md") 
                         if not f.name.startswith("00-") 
                         and f.name not in ["README.md", "LAUNCH_INSTRUCTIONS.md"]])
    
    slides = []
    for file in slide_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file.stem
            slides.append({
                'title': title,
                'content': content,
                'file': file.name
            })
    return slides

# Navigation state
if 'current' not in st.session_state:
    st.session_state.current = 0

slides = load_slides()
total_slides = len(slides)

# Navigation functions
def go_prev():
    if st.session_state.current > 0:
        st.session_state.current -= 1

def go_next():
    if st.session_state.current < total_slides - 1:
        st.session_state.current += 1

# Current slide
current = slides[st.session_state.current]

# Main content area
with st.container():
    st.markdown(f'<div class="main-container">', unsafe_allow_html=True)
    
    # Display slide content
    content = current['content']
    
    # Special handling for ASCII art boxes
    def format_ascii_boxes(text):
        # Pattern for ASCII boxes
        lines = text.split('\n')
        formatted_lines = []
        in_box = False
        
        for line in lines:
            # Detect ASCII art
            if any(c in line for c in ['╔', '╗', '╚', '╝', '═', '║', '┌', '┐', '└', '┘', '─', '│']):
                if not in_box:
                    formatted_lines.append('```')
                    in_box = True
                formatted_lines.append(line)
            else:
                if in_box and line.strip() == '':
                    formatted_lines.append(line)
                else:
                    if in_box:
                        formatted_lines.append('```')
                        in_box = False
                    formatted_lines.append(line)
        
        if in_box:
            formatted_lines.append('```')
        
        return '\n'.join(formatted_lines)
    
    # Format and display content
    formatted_content = format_ascii_boxes(content)
    st.markdown(formatted_content, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Bottom navigation bar
nav_html = f"""
<div class="bottom-nav">
    <button class="nav-btn" onclick="window.location.search='?p=prev'" 
            {'disabled' if st.session_state.current == 0 else ''}>
        ← Prev
    </button>
    <span class="slide-num">{st.session_state.current + 1} / {total_slides}</span>
    <button class="nav-btn" onclick="window.location.search='?p=next'"
            {'disabled' if st.session_state.current == total_slides - 1 else ''}>
        Next →
    </button>
</div>
<div class="kbd-hint">Use ← → arrow keys</div>
"""
st.markdown(nav_html, unsafe_allow_html=True)

# Handle URL navigation
params = st.experimental_get_query_params()
if params.get('p'):
    if params['p'][0] == 'prev':
        go_prev()
    elif params['p'][0] == 'next':
        go_next()
    st.experimental_set_query_params()
    st.rerun()

# Keyboard navigation
st.markdown("""
<script>
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        window.location.search = '?p=prev';
    } else if (e.key === 'ArrowRight') {
        window.location.search = '?p=next';
    }
});
</script>
""", unsafe_allow_html=True)

# Sidebar with slide list
with st.sidebar:
    st.markdown("### Slides")
    for i, slide in enumerate(slides):
        if st.button(f"{i+1}. {slide['title'][:30]}...", key=f"s{i}"):
            st.session_state.current = i
            st.rerun()