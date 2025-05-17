"""
Streamlit Slide Viewer v2 - Cleaner UI with Retro Styling
Inspired by MazeBuilder presentation style
"""

import streamlit as st
import os
from pathlib import Path
import re

# Page config
st.set_page_config(
    page_title="AI For Busy Professionals",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for retro look with fixed fonts
st.markdown("""
<style>
    /* Dark retro theme */
    .stApp {
        background-color: #0a0a0a;
        color: #00ff00;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Main slide container */
    .slide-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        min-height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* Fixed font for ASCII art - CRITICAL */
    pre, code, .monospace {
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 14px;
        line-height: 1.2;
        background-color: #1a1a1a;
        color: #00ff00;
        padding: 20px;
        border: 2px solid #00ff00;
        border-radius: 0;
        overflow-x: auto;
        white-space: pre;
    }
    
    /* Headers retro styling */
    h1 {
        color: #00ff00;
        font-family: 'Courier New', monospace;
        text-align: center;
        font-size: 2.5em;
        border: 3px double #00ff00;
        padding: 20px;
        margin: 30px 0;
        text-transform: uppercase;
        background-color: #0a0a0a;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.3);
    }
    
    h2 {
        color: #ffff00;
        font-family: 'Courier New', monospace;
        font-size: 1.8em;
        border-bottom: 2px solid #ffff00;
        padding-bottom: 10px;
        margin: 20px 0;
    }
    
    h3 {
        color: #00ffff;
        font-family: 'Courier New', monospace;
        font-size: 1.4em;
        margin: 15px 0;
    }
    
    /* Tables retro style */
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        font-family: 'Courier New', monospace;
    }
    
    th {
        background-color: #00ff00;
        color: #000000;
        padding: 10px;
        text-align: left;
        font-weight: bold;
        border: 2px solid #00ff00;
    }
    
    td {
        padding: 8px;
        border: 1px solid #00ff00;
        background-color: #0a0a0a;
        color: #00ff00;
    }
    
    /* Lists */
    ul, ol {
        margin-left: 30px;
        color: #00ff00;
    }
    
    li {
        margin: 10px 0;
        font-family: 'Courier New', monospace;
    }
    
    /* Navigation bar */
    .nav-container {
        background-color: #1a1a1a;
        border: 2px solid #00ff00;
        padding: 10px;
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        align-items: center;
        gap: 20px;
        z-index: 100;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
    }
    
    .nav-button {
        background-color: #0a0a0a;
        color: #00ff00;
        border: 2px solid #00ff00;
        padding: 10px 20px;
        cursor: pointer;
        font-family: 'Courier New', monospace;
        font-size: 16px;
        transition: all 0.3s;
    }
    
    .nav-button:hover {
        background-color: #00ff00;
        color: #0a0a0a;
        box-shadow: 0 0 10px #00ff00;
    }
    
    .nav-button:disabled {
        opacity: 0.5;
        cursor: not-allowed;
    }
    
    .slide-counter {
        color: #ffff00;
        font-family: 'Courier New', monospace;
        font-size: 18px;
        font-weight: bold;
    }
    
    /* Strong emphasis */
    strong {
        color: #ffff00;
        text-shadow: 0 0 5px #ffff00;
    }
    
    /* Links */
    a {
        color: #00ffff;
        text-decoration: underline;
    }
    
    a:hover {
        color: #ffffff;
        text-shadow: 0 0 10px #00ffff;
    }
    
    /* Blockquotes */
    blockquote {
        border-left: 4px solid #00ff00;
        padding-left: 20px;
        margin: 20px 0;
        color: #00ffff;
        font-style: italic;
        background-color: #0a0a0a;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
        border: 1px solid #00ff00;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #00ff00;
        border: 1px solid #0a0a0a;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #00ff00;
        box-shadow: 0 0 10px #00ff00;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .nav-container {
            width: 90%;
            left: 5%;
            transform: none;
        }
        
        h1 {
            font-size: 1.8em;
        }
        
        pre, code {
            font-size: 12px;
        }
    }
    
    /* Special ASCII box styling */
    .ascii-box {
        font-family: 'Courier New', Courier, monospace !important;
        background-color: #0a0a0a;
        border: 1px solid #00ff00;
        padding: 15px;
        white-space: pre;
        overflow-x: auto;
        font-size: 14px;
        line-height: 1.1;
    }
    
    /* Speaker notes styling */
    .speaker-notes {
        background-color: #1a1a1a;
        border: 2px dashed #666;
        padding: 15px;
        margin-top: 30px;
        color: #999;
        font-family: 'Courier New', monospace;
        font-style: italic;
    }
    
    /* Slide content wrapper */
    .slide-content {
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)

# Load slides
def load_slides():
    slides_dir = Path(__file__).parent
    slide_files = sorted([f for f in slides_dir.glob("*.md") 
                         if f.name != "00-deck-overview.md" 
                         and f.name != "README.md"
                         and f.name != "LAUNCH_INSTRUCTIONS.md"])
    
    slides = []
    for file in slide_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract title
            title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file.stem
            
            # Remove the title from content since we'll display it separately
            if title_match:
                content = content.replace(title_match.group(0), '', 1)
            
            slides.append({
                'file': file.name,
                'title': title,
                'content': content
            })
    
    return slides

# Process markdown to handle ASCII art properly
def process_markdown(content):
    # Find code blocks and wrap them properly
    lines = content.split('\n')
    processed_lines = []
    in_code_block = False
    code_block_content = []
    
    for line in lines:
        if line.strip().startswith('```'):
            if in_code_block:
                # End of code block
                processed_lines.append('<pre class="ascii-box">' + '\n'.join(code_block_content) + '</pre>')
                code_block_content = []
                in_code_block = False
            else:
                # Start of code block
                in_code_block = True
        elif in_code_block:
            code_block_content.append(line)
        else:
            # Check if line looks like ASCII art (contains box drawing characters)
            if any(char in line for char in ['╔', '╗', '╚', '╝', '═', '║', '├', '┤', '─', '│', '┌', '┐', '└', '┘']):
                processed_lines.append(f'<pre class="ascii-box">{line}</pre>')
            else:
                processed_lines.append(line)
    
    return '\n'.join(processed_lines)

# Initialize session state
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

slides = load_slides()
current_slide = slides[st.session_state.slide_index]

# Main container
st.markdown('<div class="slide-container">', unsafe_allow_html=True)

# Slide title
st.markdown(f"# {current_slide['title']}", unsafe_allow_html=True)

# Process and display content
content = current_slide['content']

# Split speaker notes
parts = content.split("**Speaker Notes:**")
main_content = parts[0]
speaker_notes = parts[1] if len(parts) > 1 else None

# Process main content for ASCII art
processed_content = process_markdown(main_content)

# Display main content
st.markdown(f'<div class="slide-content">{processed_content}</div>', unsafe_allow_html=True)

# Display speaker notes if toggled
if st.checkbox("Show Speaker Notes", key=f"notes_{st.session_state.slide_index}"):
    if speaker_notes:
        st.markdown(f'<div class="speaker-notes">{speaker_notes}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Navigation bar (fixed at bottom)
nav_html = f"""
<div class="nav-container">
    <button class="nav-button" onclick="window.location.href='?prev=true'" {'disabled' if st.session_state.slide_index == 0 else ''}>
        ← Previous
    </button>
    <span class="slide-counter">
        {st.session_state.slide_index + 1} / {len(slides)}
    </span>
    <button class="nav-button" onclick="window.location.href='?next=true'" {'disabled' if st.session_state.slide_index == len(slides) - 1 else ''}>
        Next →
    </button>
</div>
"""

st.markdown(nav_html, unsafe_allow_html=True)

# Handle navigation through URL parameters
params = st.experimental_get_query_params()
if 'prev' in params and st.session_state.slide_index > 0:
    st.session_state.slide_index -= 1
    st.experimental_set_query_params()
    st.rerun()
elif 'next' in params and st.session_state.slide_index < len(slides) - 1:
    st.session_state.slide_index += 1
    st.experimental_set_query_params()
    st.rerun()

# Keyboard navigation script
st.markdown("""
<script>
document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowLeft' && window.location.search !== '?prev=true') {
        window.location.href = '?prev=true';
    } else if (event.key === 'ArrowRight' && window.location.search !== '?next=true') {
        window.location.href = '?next=true';
    }
});
</script>
""", unsafe_allow_html=True)

# Add slide overview in sidebar
with st.sidebar:
    st.markdown("### 📑 Slide Overview")
    for i, slide in enumerate(slides):
        if st.button(f"{i+1}. {slide['title']}", key=f"nav_{i}"):
            st.session_state.slide_index = i
            st.rerun()