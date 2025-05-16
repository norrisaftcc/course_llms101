# 90-Minute LLM Crash Course: From Zero to AI App

## Title: "Build Your First AI-Powered Application in 90 Minutes"

### Pre-Session Setup (Email to participants)
- Install Python 3.8+
- Create accounts: OpenAI, Supabase, GitHub
- Install: `pip install streamlit supabase openai`
- Download starter template from GitHub

### Session Flow

#### 0:00-0:10 - Opening Hook & Introductions
**"The 10x Developer Isn't Faster - They Use Better Tools"**

- Live demo: Build a blog post in 5 seconds with AI
- Show the finished app we'll build today
- Quick round of introductions (name, background, goal)
- Set expectations: "You'll leave with a working AI app"

#### 0:10-0:20 - LLMs in 10 Minutes
**Just Enough Theory to Be Dangerous**

1. **What's an LLM?** (2 min)
   - Advanced autocomplete on steroids
   - Trained on the internet's text
   - Doesn't "know" things - predicts likely responses

2. **Why Should You Care?** (3 min)
   - Automate repetitive writing tasks
   - Build intelligent interfaces
   - Enhance existing applications
   - Create new product categories

3. **Key Concepts** (5 min)
   - Tokens: How LLMs process text
   - Temperature: Creativity vs consistency
   - Prompts: Your instructions to the AI
   - Context window: Memory limitations

#### 0:20-0:30 - Hands-On: Your First LLM Interaction
**Let's Talk to AI**

```python
import openai

# Simple example
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write a haiku about coding"}
    ]
)
print(response.choices[0].message.content)
```

**Exercises**:
1. Generate a product description
2. Summarize a paragraph
3. Transform formal text to casual

#### 0:30-0:75 - Build Your AI Blog App
**From Empty Folder to Deployed App**

##### Part 1: Set Up Supabase (10 min)
```python
# Initialize Supabase
from supabase import create_client

supabase = create_client(
    "your-project-url",
    "your-anon-key"
)

# Create posts table
# Show UI method in Supabase dashboard
```

##### Part 2: Create Streamlit UI (15 min)
```python
import streamlit as st

st.title("AI-Powered Blog")

# Sidebar for create post
with st.sidebar:
    st.header("Create New Post")
    title = st.text_input("Title")
    topic = st.text_input("Topic")
    
    if st.button("Generate Post"):
        # AI generation here
        pass

# Main area for posts
posts = supabase.table("posts").select("*").execute()
for post in posts.data:
    st.subheader(post["title"])
    st.write(post["content"])
```

##### Part 3: Add AI Generation (10 min)
```python
def generate_blog_post(topic):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful blog writer"},
            {"role": "user", "content": f"Write a 200-word blog post about {topic}"}
        ]
    )
    return response.choices[0].message.content

# Connect to button
if st.button("Generate Post"):
    content = generate_blog_post(topic)
    supabase.table("posts").insert({
        "title": title,
        "content": content
    }).execute()
    st.success("Post created!")
```

##### Part 4: Add AI Features (10 min)
- Comment moderation
- SEO meta description generation
- Related posts suggestions
- Content tone adjustment

#### 0:75-0:85 - Identify Your Use Cases
**Where Can You Apply This?**

**Brainstorming Exercise**:
1. What repetitive writing tasks do you do?
2. Where do you need content generation?
3. What could be automated in your workflow?

**Common Patterns**:
- Customer service responses
- Documentation generation
- Data extraction from text
- Content personalization
- Report summarization

#### 0:85-0:90 - Wrap Up & Next Steps
**Your AI Journey Starts Now**

1. **Resources to Continue**:
   - GitHub repo with extended examples
   - Discord community for questions
   - Weekly office hours
   - Full course information

2. **Homework Challenge**:
   - Extend the blog with one new AI feature
   - Apply to your own use case
   - Share in the community

3. **Special Offer**:
   - 50% off full course for session attendees
   - Free 1-on-1 consultation
   - Access to advanced examples

### Post-Session Materials

#### GitHub Repository Structure:
```
llm-course-starter/
├── README.md
├── requirements.txt
├── 01-basics/
│   ├── first_api_call.py
│   ├── prompt_examples.py
│   └── error_handling.py
├── 02-blog-app/
│   ├── simple_blog.py
│   ├── ai_blog.py
│   └── advanced_features.py
├── 03-templates/
│   ├── customer_service.py
│   ├── content_generator.py
│   └── data_extractor.py
└── 04-resources/
    ├── prompt_library.md
    ├── best_practices.md
    └── troubleshooting.md
```

#### One-Page Reference Guide:
- API setup checklist
- Common prompt patterns
- Error handling basics
- Cost optimization tips
- Security best practices

### Success Metrics

**During Session**:
- 90% complete the basic app
- 70% add at least one AI feature
- 100% can explain what an LLM is

**Post Session**:
- 50% join the Discord community
- 30% complete homework challenge
- 10% sign up for full course

### Instructor Notes

**Timing Critical Points**:
- Don't let setup exceed 10 minutes
- Keep theory portion engaging with demos
- Have backup for slow typers (copy/paste ready)
- Leave buffer for debugging common issues

**Common Issues & Solutions**:
1. API key errors → Have test keys ready
2. Package conflicts → Provide Docker option
3. Supabase setup → Pre-created projects
4. Network issues → Local fallback demos

**Energy Management**:
- High energy opening
- Hands-on keeps engagement
- Quick wins build confidence
- End with inspiration

### Marketing Tagline:
"Most courses teach theory. We build apps. In 90 minutes."