# LLM 90-Minute Session Cheat Sheet

## Quick Reference

### Essential Commands
```bash
# Check Python version
python --version

# Install packages
pip install streamlit openai supabase

# Run Streamlit app
streamlit run ai_blog.py

# Test your setup
python verify_setup.py
```

### Environment Variables
```bash
export OPENAI_API_KEY="sk-..."
export SUPABASE_URL="https://xxx.supabase.co"
export SUPABASE_KEY="eyJ..."
```

## Code Snippets

### 1. Basic OpenAI Call
```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.choices[0].message.content)
```

### 2. Simple Streamlit App
```python
import streamlit as st

st.title("My App")
user_input = st.text_input("Enter text:")
if st.button("Submit"):
    st.write(f"You entered: {user_input}")
```

### 3. Supabase Connection
```python
from supabase import create_client

supabase = create_client(url, key)
data = supabase.table("posts").select("*").execute()
```

### 4. Generate Blog Post
```python
def generate_blog_post(topic, tone="professional", length=250):
    prompt = f"""
    Write a {length}-word blog post about: {topic}
    Tone: {tone}
    Include introduction, main points, and conclusion.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a blog writer"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
```

### 5. Streamlit Form
```python
with st.form("post_form"):
    title = st.text_input("Title")
    topic = st.text_area("Topic")
    tone = st.select_slider("Tone", 
        ["Formal", "Professional", "Casual"])
    
    if st.form_submit_button("Generate"):
        content = generate_blog_post(topic, tone)
        st.write(content)
```

## Common Patterns

### Error Handling
```python
try:
    response = openai.ChatCompletion.create(...)
except Exception as e:
    st.error(f"Error: {str(e)}")
```

### Loading State
```python
with st.spinner("Generating..."):
    content = generate_blog_post(topic)
```

### Sidebar
```python
with st.sidebar:
    st.header("Settings")
    temperature = st.slider("Creativity", 0.0, 1.0, 0.7)
```

## Prompt Engineering Tips

### Structure
```
Role: You are a [specific role]
Context: [Background information]
Task: [What to do]
Format: [How to format output]
Constraints: [Any limitations]
```

### Examples
```python
# Professional blog post
"Write a professional blog post about {topic}. 
Use clear headings and include practical examples."

# SEO metadata
"Generate SEO metadata for this blog post:
Title: {title}
Content: {content[:200]}
Format: JSON with 'description' and 'keywords'"

# Content moderation
"Analyze this comment for inappropriate content.
Comment: {text}
Response: 'appropriate' or 'inappropriate'"
```

## Debugging Checklist

- [ ] API keys set correctly?
- [ ] Internet connection stable?
- [ ] All packages installed?
- [ ] Using correct Python version?
- [ ] Streamlit port available?
- [ ] Database tables created?

## Useful Links

- **OpenAI Docs**: https://platform.openai.com/docs
- **Streamlit Docs**: https://docs.streamlit.io
- **Supabase Docs**: https://supabase.com/docs
- **Course Discord**: [Discord Link]
- **GitHub Repo**: [Repository Link]

## Session Shortcuts

### Quick Debug
```python
st.write(st.session_state)  # Check state
st.write(data)              # Inspect data
print(response)             # Console output
```

### Quick Deploy
```bash
# Local testing
streamlit run app.py

# Share via localtunnel
npm install -g localtunnel
lt --port 8501
```

## After the Session

1. **Practice**: Modify the app with new features
2. **Explore**: Try different models and parameters
3. **Share**: Post your creation in Discord
4. **Learn**: Check out the full course materials

---

Remember: Focus on getting it working first, optimize later!