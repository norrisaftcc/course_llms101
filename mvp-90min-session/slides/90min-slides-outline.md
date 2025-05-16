# 90-Minute Session Slide Deck Outline

## Slide 1: Title Slide
**From Zero to AI App in 90 Minutes**
- Subtitle: Build Your First AI-Powered Application Today
- Instructor name and credentials
- Date and location
- Course logo/branding

## Slide 2: Your Instructor
- Photo
- Brief background (3 bullets)
- Why I'm passionate about teaching AI
- Contact information

## Slide 3: Today's Journey
**What We'll Accomplish**
- ✅ Understand LLMs in 10 minutes
- ✅ Make your first AI API call
- ✅ Build a complete AI blog application
- ✅ Deploy and customize
- ✅ Plan your next AI project

## Slide 4: Pre-flight Check
**Quick Setup Verification**
```bash
python verify_setup.py
```
- All green? Let's go!
- Issues? Raise your hand
- Helpers are available

## Slide 5: The AI Revolution Timeline
**How We Got Here**
- 1950s: Turing Test
- 1960s-2000s: Rule-based systems
- 2017: Transformer architecture
- 2022: ChatGPT changes everything
- 2024: You join the revolution!

## Slide 6: What's an LLM?
**Large Language Model Explained**
[Visual: Input → Model → Output]
- Trained on massive text data
- Predicts next most likely word
- No true understanding, but...
- Incredibly useful patterns!

## Slide 7: The Business Impact
**Real Companies, Real Results**
| Company | Use Case | Impact |
|---------|----------|--------|
| GitHub | Copilot | 55% faster coding |
| JPMorgan | Contracts | 360,000 hours saved |
| Duolingo | Lessons | 4x content creation |

## Slide 8: Your First AI Call
**Let's Talk to GPT-3.5**
```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", 
               "content": "Hello AI!"}]
)
```
Live demo time! 🚀

## Slide 9: Tokens & Costs
**Understanding AI Economics**
[Visual: Text → Tokens → $ Cost]
- 1 token ≈ 4 characters
- Input + Output = Total cost
- GPT-3.5: $0.002 per 1K tokens
- Our app today: ~$0.01 per blog post

## Slide 10: The App We're Building
**AI-Powered Blog Platform**
[Screenshot of finished app]
Features:
- Auto-generate posts
- Adjustable tone
- SEO optimization
- Database storage
- Beautiful UI

## Slide 11: Architecture Overview
**How It All Connects**
[Diagram: User → Streamlit → OpenAI API → Supabase]
- Frontend: Streamlit (Python)
- AI Brain: OpenAI API
- Storage: Supabase (PostgreSQL)
- Deployment: Your choice!

## Slide 12: Let's Build! (Part 1)
**Setting Up Streamlit**
```python
import streamlit as st

st.title("AI Blog Generator")
topic = st.text_input("Blog topic:")
if st.button("Generate"):
    # Magic happens here
```

## Slide 13: Let's Build! (Part 2)
**Connecting to OpenAI**
```python
def generate_post(topic):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", 
                   "content": f"Write about {topic}"}]
    )
    return response.choices[0].message.content
```

## Slide 14: Let's Build! (Part 3)
**Adding Database Storage**
```python
supabase.table("posts").insert({
    "title": title,
    "content": content,
    "created_at": datetime.now()
}).execute()
```

## Slide 15: Prompt Engineering
**The Secret Sauce**
Good prompt:
```
Write a 200-word professional blog post about {topic}.
Include introduction, main points, and conclusion.
```
Better prompt:
```
Role: Expert blog writer
Task: Create engaging 200-word post about {topic}
Style: Professional yet conversational
Structure: Hook, 3 key points, call-to-action
```

## Slide 16: Live Customization
**Make It Yours**
Let's add:
- Tone selector
- Word count control
- SEO metadata
- Multiple languages
- Image generation?

## Slide 17: Common Pitfalls
**What to Avoid**
❌ No API key validation
❌ No error handling
❌ Unlimited requests
❌ Storing sensitive data
❌ Trusting AI blindly

✅ We'll fix all these!

## Slide 18: Your Use Cases
**Brainstorm Time!**
Think about your work:
- What tasks are repetitive?
- Where do you need content?
- What could be automated?
- What would save time?

Share with your neighbor!

## Slide 19: AI Application Patterns
**Common Success Patterns**
1. **Content Generation**
   - Marketing copy, emails, docs
2. **Data Extraction**
   - Invoices, contracts, forms
3. **Customer Service**
   - FAQ, chat, email responses
4. **Code Assistant**
   - Boilerplate, documentation
5. **Analysis & Insights**
   - Sentiment, summaries, trends

## Slide 20: Next Steps
**Your AI Journey Continues**
1. Complete today's app
2. Join our Discord community
3. Try the homework challenge
4. Explore prompt engineering
5. Consider the full course

## Slide 21: Resources
**Everything You Need**
- GitHub repo: [link]
- Discord: [link]
- Documentation: [link]
- My email: [email]
- Office hours: Thursdays 3-4 PM

## Slide 22: Special Offer
**For Today's Attendees Only**
- 50% off full 8-week course
- Regular price: $497
- Your price: $247
- Code: BUILDER50
- Valid 7 days

[QR code for enrollment]

## Slide 23: Let's Deploy!
**Bonus: Ship It!**
Quick deployment options:
- Streamlit Cloud (free)
- Heroku
- Railway
- Replit

Live demo if time permits!

## Slide 24: Q&A
**Your Questions**
[Large question mark graphic]

Common questions:
- Cost concerns?
- Security?
- Scaling?
- Other use cases?

## Slide 25: Thank You!
**You Built an AI App! 🎉**
- Certificate of completion
- Join our community
- Keep building
- Share your success

[Contact info and social links]

---

## Slide Design Notes

### Visual Style
- Clean, modern design
- Tech-forward color scheme
- Code syntax highlighting
- Minimal text per slide
- Large, readable fonts

### Animations
- Subtle transitions
- Code appears line by line
- Diagrams build progressively
- No distracting effects

### Interactive Elements
- Live coding sections
- Audience participation
- Real-time demos
- Progress indicators

### Backup Slides
- Troubleshooting guide
- Additional examples
- Advanced topics
- Corporate training info

### Speaker Notes
Include for each slide:
- Key talking points
- Timing (seconds)
- Demo instructions
- Common questions
- Transition phrases