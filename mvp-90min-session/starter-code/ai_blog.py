"""
AI-Powered Blog Application
Built with Streamlit, Supabase, and OpenAI
Course: LLMs in Enterprise Applications (90-min version)
"""

import streamlit as st
import openai
from supabase import create_client
import os
from datetime import datetime

# Initialize clients (in production, use environment variables)
openai.api_key = st.secrets.get("OPENAI_API_KEY", "your-api-key-here")
supabase = create_client(
    st.secrets.get("SUPABASE_URL", "your-supabase-url"),
    st.secrets.get("SUPABASE_KEY", "your-supabase-key")
)

# Page config
st.set_page_config(
    page_title="AI-Powered Blog",
    page_icon="✍️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .blog-post {
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .post-meta {
        color: #666;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("✍️ AI-Powered Blog Platform")
st.markdown("Build your blog content with the power of AI")

# Sidebar for creating posts
with st.sidebar:
    st.header("Create New Post")
    
    with st.form("create_post_form"):
        title = st.text_input("Post Title", placeholder="Enter a catchy title...")
        topic = st.text_area("Topic/Description", placeholder="What should the post be about?")
        
        # AI Settings
        st.subheader("AI Settings")
        tone = st.select_slider(
            "Content Tone",
            options=["Formal", "Professional", "Conversational", "Casual", "Creative"],
            value="Professional"
        )
        
        length = st.slider("Approximate Word Count", 100, 500, 250, 50)
        
        # SEO Options
        include_seo = st.checkbox("Generate SEO metadata", value=True)
        
        submitted = st.form_submit_button("Generate & Publish", type="primary")
        
        if submitted and title and topic:
            with st.spinner("AI is writing your post..."):
                try:
                    # Generate blog content
                    blog_content = generate_blog_post(topic, tone, length)
                    
                    # Generate SEO metadata if requested
                    seo_data = {}
                    if include_seo:
                        seo_data = generate_seo_metadata(title, blog_content)
                    
                    # Save to Supabase
                    post_data = {
                        "title": title,
                        "content": blog_content,
                        "topic": topic,
                        "tone": tone,
                        "meta_description": seo_data.get("description", ""),
                        "meta_keywords": seo_data.get("keywords", ""),
                        "created_at": datetime.now().isoformat()
                    }
                    
                    result = supabase.table("posts").insert(post_data).execute()
                    
                    st.success("✅ Post published successfully!")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# Main content area
col1, col2 = st.columns([3, 1])

with col1:
    st.header("Recent Posts")
    
    # Fetch and display posts
    try:
        response = supabase.table("posts").select("*").order("created_at", desc=True).execute()
        posts = response.data
        
        if posts:
            for post in posts:
                with st.container():
                    st.markdown(f"### {post['title']}")
                    st.markdown(f"<div class='post-meta'>Published: {post['created_at'][:10]} | Tone: {post['tone']}</div>", unsafe_allow_html=True)
                    st.markdown(post['content'])
                    
                    # Show SEO data if available
                    if post.get('meta_description'):
                        with st.expander("SEO Metadata"):
                            st.write(f"**Description:** {post['meta_description']}")
                            st.write(f"**Keywords:** {post['meta_keywords']}")
                    
                    st.divider()
        else:
            st.info("No posts yet. Create your first AI-powered post using the sidebar!")
            
    except Exception as e:
        st.error(f"Error loading posts: {str(e)}")

with col2:
    st.header("AI Features")
    st.markdown("""
    ### 🤖 What this app does:
    - Generates blog posts on any topic
    - Adjustable tone and length
    - SEO metadata generation
    - Automatic formatting
    
    ### 🎯 Try these features:
    - Different tone settings
    - Various content lengths
    - SEO optimization
    - Topic variations
    
    ### 📈 Coming soon:
    - Comment moderation
    - Content translation
    - Social media posts
    - Email newsletters
    """)

# AI Generation Functions
def generate_blog_post(topic, tone, length):
    """Generate blog post content using OpenAI"""
    
    tone_instructions = {
        "Formal": "Write in a formal, academic style",
        "Professional": "Write in a professional business style",
        "Conversational": "Write in a conversational, friendly style",
        "Casual": "Write in a casual, relaxed style",
        "Creative": "Write in a creative, engaging style with vivid descriptions"
    }
    
    prompt = f"""
    Write a {length}-word blog post about: {topic}
    
    Style: {tone_instructions.get(tone, 'Professional')}
    
    Requirements:
    - Engaging introduction
    - Clear main points
    - Practical examples where relevant
    - Strong conclusion
    - Natural paragraph breaks
    
    Do not include a title, as that's provided separately.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert blog writer who creates engaging, informative content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=length * 2  # Rough estimate for token count
    )
    
    return response.choices[0].message.content

def generate_seo_metadata(title, content):
    """Generate SEO metadata for the blog post"""
    
    prompt = f"""
    Generate SEO metadata for this blog post:
    
    Title: {title}
    Content: {content[:500]}...
    
    Provide:
    1. A compelling meta description (150-160 characters)
    2. 5-7 relevant keywords (comma-separated)
    
    Format as JSON with keys: "description" and "keywords"
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an SEO expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    # Parse the response (in production, use proper JSON parsing)
    content = response.choices[0].message.content
    try:
        import json
        return json.loads(content)
    except:
        # Fallback parsing
        return {
            "description": "AI-generated blog post",
            "keywords": "blog, AI, content"
        }

# Footer
st.markdown("---")
st.markdown("Built with ❤️ in the **LLMs in Enterprise Applications** course")
st.markdown("Questions? Join our [Discord Community](https://discord.gg/llm-course)")