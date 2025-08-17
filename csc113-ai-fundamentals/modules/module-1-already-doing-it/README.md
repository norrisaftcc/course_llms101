# Module 1: AI - You're Already Doing It
## CSC-113 AI Fundamentals | Week 1

---

## Module Overview

Welcome to CSC-113! This week, you'll discover you're already an AI user, learn how professional developers actually work, and meet your first AI teammate: "Kevin from IT" (Gemini Flash). By Friday, you'll have your first GitHub repository with actual commits, proving you can collaborate with both humans and AI.

**Time Commitment**: 4-6 hours total (spread across 3 work days)
**Format**: Asynchronous with optional sync sessions
**Tracking**: Your GitHub contribution graph is your attendance

---

## Learning Objectives

By the end of Module 1, you will be able to:

1. **Identify** at least 10 ways AI already impacts your daily life
2. **Execute** the complete GitHub workflow (Issue → Branch → Commit → PR → Merge)
3. **Document** your work using professional Markdown formatting
4. **Collaborate** with AI (Gemini Flash) for various tasks
5. **Participate** in peer code review processes
6. **Reflect** on your learning through GitHub Discussions

---

## Required Accounts & Setup

### Before Day 1
1. **GitHub Account**: https://github.com/signup
   - Use a professional username (you'll keep this forever)
   - Add a profile photo and bio
   - Enable two-factor authentication

2. **Google AI Studio**: https://aistudio.google.com
   - Sign in with Google account
   - No credit card required
   - This gives you access to Gemini Flash (Kevin)

3. **GitHub Student Developer Pack**: https://education.github.com/pack
   - Free access to premium tools
   - Requires .edu email or student ID
   - Apply now, approval takes 1-3 days

---

## Day 1 (Monday): "Hello, Scholars!"

### Learning Goals
- Understand why GitHub is "how developers work"
- Create your first repository
- Make your first commit
- Open your first Issue

### Synchronous Session (Optional but Recommended)
**Time**: 1 hour
**Agenda**:
1. Welcome & course overview (10 min)
2. Live demo: "This is how Netflix ships code" (15 min)
3. Follow along: Create first repository together (20 min)
4. Q&A and troubleshooting (15 min)

### Asynchronous Activities

#### Activity 1.1: GitHub Exploration (30 minutes)
1. Accept invitation to course organization: `csc113-fall-2025`
2. Explore the organization page
3. Find the `module-1-discussions` repository
4. Post introduction in Discussions: "Hello from [Your Name]"

#### Activity 1.2: Create Your First Repository (45 minutes)

**Step-by-Step Instructions**:

1. **Create Repository**
   - Click green "New" button in GitHub
   - Name: `my-ai-journey`
   - Description: "Documenting my AI learning in CSC-113"
   - Public repository
   - Add README file: Yes
   - Add .gitignore: No
   - License: MIT

2. **Create Your First Issue**
   - Go to Issues tab
   - Click "New Issue"
   - Title: "Document my current AI usage"
   - Body:
   ```markdown
   ## Task
   Create a comprehensive list of ways I already use AI
   
   ## Acceptance Criteria
   - [ ] List at least 10 AI interactions
   - [ ] Organize by category
   - [ ] Add personal reflection
   
   ## Branch
   `1-ai-audit`
   ```
   - Assign to yourself
   - Submit Issue

3. **Create Branch from Issue**
   - In the Issue, look for "Create a branch" in the right sidebar
   - Accept default name: `1-ai-audit`
   - Create branch

4. **Make Your First Edit**
   - Navigate to README.md
   - Click pencil icon to edit
   - Replace contents with:
   ```markdown
   # My AI Journey
   
   ## About This Repository
   This repository documents my learning journey in CSC-113 AI Fundamentals.
   
   ## Current Module
   Module 1: Discovering AI in Daily Life
   
   ## My AI Audit
   
   ### AI I Use Daily (Without Realizing It)
   
   #### Communication
   1. **Autocorrect** - My phone fixes my typing constantly
   2. **Email filters** - Gmail sorts spam automatically
   
   #### Entertainment
   3. **Netflix recommendations** - "Because you watched..."
   4. **Spotify Discover Weekly** - New music every Monday
   
   #### Navigation
   5. **Google Maps** - Route optimization in real-time
   6. **Uber/Lyft** - Pricing and driver matching
   
   #### Shopping
   7. **Amazon recommendations** - "Customers also bought"
   8. **Credit card fraud detection** - Flags unusual purchases
   
   #### Social Media
   9. **Instagram feed** - Algorithm chooses what I see
   10. **Facebook face recognition** - Tags friends automatically
   
   ### Reflection
   I'm surprised by how much AI I already use. It's not just robots 
   and sci-fi - it's woven into everything I do online.
   
   ## Author
   [Your Name]
   
   ## Course
   CSC-113 AI Fundamentals
   ```

5. **Commit Your Changes**
   - Scroll to "Commit changes"
   - Message: "Add AI audit documenting 10+ daily AI interactions"
   - Description: "Completes Issue #1 requirements for Module 1"
   - Select: "Commit directly to the `1-ai-audit` branch"
   - Click "Commit changes"

#### Activity 1.3: Create Your First Pull Request (30 minutes)

1. **Navigate to Pull Requests tab**
2. Click "New pull request"
3. Ensure: `base: main` ← `compare: 1-ai-audit`
4. Click "Create pull request"
5. Title: "Add AI audit - Fixes #1"
6. Body:
   ```markdown
   ## Summary
   Added comprehensive AI audit documenting daily AI usage
   
   ## Changes
   - Listed 10+ AI interactions
   - Organized by category
   - Added personal reflection
   
   ## Related Issue
   Fixes #1 
   ```
7. Create pull request
8. Merge your own PR (for now)
9. Delete branch when prompted

### Daily Reflection
Post in `module-1-discussions`:
- What surprised you about GitHub?
- What AI usage surprised you most?
- What's still confusing?

### Success Metrics for Day 1
- [ ] GitHub account created and configured
- [ ] First repository created
- [ ] First Issue opened and closed
- [ ] First PR merged
- [ ] Posted in Discussions

---

## Day 2 (Wednesday): Meet Kevin from IT

### Learning Goals
- Set up Gemini Flash access
- Understand AI as a collaborative tool
- Document AI interactions professionally
- Practice atomic commits

### Asynchronous Activities

#### Activity 2.1: Meet Kevin (30 minutes)

1. **Access Google AI Studio**
   - Go to https://aistudio.google.com
   - Sign in with Google account
   - Click "Create new prompt"

2. **Your First Kevin Interaction**
   ```
   Hi! I'm going to call you Kevin from IT. You're my helpful AI assistant 
   for a college course on AI Fundamentals. Please introduce yourself as 
   Kevin and tell me what kinds of things you can help with.
   ```

3. **Document Kevin's Response**
   - Create new Issue: "Test Kevin's capabilities"
   - Create branch: `2-kevin-introduction`
   - Add new file: `kevin-tests.md`

#### Activity 2.2: Kevin Capability Testing (1 hour)

Test Kevin with these 5 different task types:

1. **Writing Assistance**
   ```
   Kevin, help me write a professional email to my professor explaining 
   that I'll miss class due to a job interview.
   ```

2. **Code Generation**
   ```
   Kevin, write a Python function that calculates the average of a list 
   of numbers, with error handling for empty lists.
   ```

3. **Learning Support**
   ```
   Kevin, explain what a GitHub Pull Request is using a restaurant 
   kitchen analogy.
   ```

4. **Creative Tasks**
   ```
   Kevin, write a haiku about debugging code.
   ```

5. **Analysis Tasks**
   ```
   Kevin, analyze this commit message and suggest improvements:
   "fixed stuff"
   ```

**Document each test in `kevin-tests.md`**:
```markdown
# Kevin Capability Tests

## Test 1: Writing Assistance
**Prompt**: [exact prompt you used]
**Kevin's Response**: [paste response]
**My Rating**: X/10
**Notes**: [what worked, what didn't]

[Repeat for all 5 tests]

## Overall Impressions
[Your thoughts on Kevin as a teammate]
```

#### Activity 2.3: Atomic Commits Practice (30 minutes)

Make a separate commit for each test:
1. Commit 1: "Add Test 1: Writing assistance results"
2. Commit 2: "Add Test 2: Code generation results"
3. Commit 3: "Add Test 3: Learning support results"
4. Commit 4: "Add Test 4: Creative tasks results"
5. Commit 5: "Add Test 5: Analysis tasks results"
6. Commit 6: "Add overall impressions of Kevin"

Create PR: "Add Kevin capability testing - Fixes #2"

### Peer Interaction
1. Review one classmate's Kevin tests
2. Comment on their PR with:
   - One thing they tested that you didn't think of
   - One suggestion for another test
   - Positive feedback on their documentation

### Success Metrics for Day 2
- [ ] Kevin (Gemini Flash) access confirmed
- [ ] 5 capability tests completed
- [ ] 6 atomic commits made
- [ ] PR created and merged
- [ ] 1 peer review completed

---

## Day 3 (Friday): Professional Documentation & Reflection

### Learning Goals
- Master Markdown formatting
- Complete peer reviews
- Plan weekend exploration
- Reflect on Week 1 learning

### Asynchronous Activities

#### Activity 3.1: Markdown Mastery (45 minutes)

Create new Issue: "Improve repository documentation"
Create branch: `3-documentation-upgrade`

**Enhance your README.md with all Markdown features**:

```markdown
# My AI Journey 🚀

## 📚 Table of Contents
- [About](#about)
- [Current Progress](#current-progress)
- [Key Learnings](#key-learnings)
- [AI Tools](#ai-tools)
- [Contact](#contact)

## About
This repository documents my learning journey in **CSC-113 AI Fundamentals**.

### Course Details
| Week | Module | Status |
|------|--------|--------|
| 1 | AI - You're Already Doing It | ✅ Complete |
| 2 | Build a Bad Agent | ⏳ Upcoming |
| 3 | Build a Pretty-Good Agent | 🔮 Future |

## Current Progress
- [x] Created first repository
- [x] Learned GitHub workflow
- [x] Met Kevin from IT
- [ ] Build first AI assistant

## Key Learnings

### Week 1 Highlights
1. **GitHub is how professionals work**
   - Everything is tracked
   - Collaboration is built-in
   - History is permanent

2. **AI is already everywhere**
   > "I discovered I use AI at least 50 times per day without thinking about it"

3. **Kevin is surprisingly helpful**
   ```python
   def kevin_helps():
       return "More than I expected!"
   ```

## AI Tools

### Primary Assistant: Kevin (Gemini Flash)
- **Strengths**: Fast, creative, helpful
- **Weaknesses**: Sometimes too verbose
- **Best for**: First drafts, brainstorming

### Upcoming Tools
- [ ] Claude (Module 3)
- [ ] GPT-4 (Module 3)
- [ ] Local models (Module 5)

## Weekend Exploration Plan
I plan to explore:
1. How Kevin can help with my other classes
2. GitHub features I haven't tried yet
3. More advanced Markdown formatting

## Contact
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Course**: CSC-113 Fall 2025

---
*Last updated: [Today's Date]*
```

#### Activity 3.2: Peer Review Marathon (45 minutes)

1. **Find 2 classmates' PRs to review**
2. **Use this review template**:
   ```markdown
   ## Code Review
   
   ### Strengths
   - [Specific thing they did well]
   - [Another positive observation]
   
   ### Suggestions
   - [One specific improvement]
   - [Optional: Another idea]
   
   ### Questions
   - [Something you're curious about]
   
   Overall: [Approve/Request Changes/Comment]
   ```

3. **Respond to reviews on your PR**
   - Thank reviewers
   - Address suggestions
   - Answer questions

#### Activity 3.3: Module 1 Reflection (30 minutes)

Create a Discussion post with this template:

```markdown
# Module 1 Reflection: [Your Name]

## 🎯 What I Accomplished
- [List your completed deliverables]
- GitHub contributions: [X commits, Y PRs, Z reviews]

## 💡 Biggest Surprises
1. About AI: [your discovery]
2. About GitHub: [your discovery]
3. About Kevin: [your discovery]

## 🤔 Still Figuring Out
- [Concept or tool that's still confusing]
- [Question for classmates or instructor]

## 🚀 Ready for Module 2 Because
- [Why you're prepared]
- [What you're excited about]

## 📊 My Green Squares
Mon: 🟩 (X commits)
Wed: 🟩 (Y commits)
Fri: 🟩 (Z commits)

## 🎉 Proud Moment
[Something you're proud of from this week]
```

### Success Metrics for Day 3
- [ ] README enhanced with advanced Markdown
- [ ] 2 peer reviews completed
- [ ] Responded to peer feedback
- [ ] Module reflection posted
- [ ] 3 green squares this week

---

## Module 1 Deliverables Checklist

### Required (100% completion for full credit)
- [ ] GitHub account with professional profile
- [ ] Repository: `my-ai-journey`
- [ ] Minimum 10 commits across the week
- [ ] 3 Issues created and closed
- [ ] 3 PRs created and merged
- [ ] 2 peer reviews given
- [ ] Kevin capability tests documented
- [ ] Module reflection posted

### GitHub Activity Metrics
- [ ] Monday: Green square (any commits)
- [ ] Wednesday: Green square (any commits)
- [ ] Friday: Green square (any commits)
- [ ] Total commits: 10+ minimum
- [ ] Total PR reviews: 2+ minimum

### Quality Indicators
- [ ] Meaningful commit messages (not "fixed stuff")
- [ ] Helpful PR descriptions
- [ ] Constructive peer reviews
- [ ] Professional documentation

---

## Resources & Support

### Essential Links
- [GitHub Docs](https://docs.github.com)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [Google AI Studio](https://aistudio.google.com)
- [Course Discussion Board](https://github.com/csc113-fall-2025/discussions)

### Getting Help
1. **First**: Check the Discussion board (someone probably asked already)
2. **Second**: Ask Kevin! "Kevin, how do I [specific thing] in GitHub?"
3. **Third**: Post in Discussions with:
   - What you're trying to do
   - What you've tried
   - Error messages (if any)
4. **Last Resort**: Office hours (but try the above first!)

### Common Issues & Solutions

**"I can't create a branch"**
- Make sure you're in YOUR repository, not the course org
- Check that you have an open Issue first

**"Kevin isn't responding"**
- Check you're signed into Google AI Studio
- Try refreshing the page
- Use a simpler prompt

**"I messed up my repository"**
- It's fine! Create a new branch from main
- Or worst case: delete repo and start fresh (you're learning!)

**"I don't have a green square"**
- Commits must be pushed to GitHub (not just local)
- Check your email is verified in GitHub settings
- Make sure you're signed in when committing

---

## Looking Ahead: Module 2 Preview

Next week, you'll deliberately build a TERRIBLE AI assistant. Why? Because:
- Failure teaches better than success
- You'll understand what makes AI helpful by making it unhelpful
- It's surprisingly fun to build something awful on purpose
- Your peers will vote for "Worst Assistant Award"

Start thinking: What would make an AI assistant absolutely terrible at its job?

---

## Instructor Notes Section

### Grading Rubric for Module 1

| Component | Points | Criteria |
|-----------|---------|----------|
| GitHub Setup | 20 | Profile complete, repo created, organization joined |
| Commits & PRs | 30 | 10+ commits, 3 PRs, meaningful messages |
| Kevin Tests | 20 | 5 tests documented, thoughtful analysis |
| Peer Review | 15 | 2+ reviews, constructive feedback |
| Reflection | 15 | Thoughtful, complete, shows learning |

### Intervention Triggers
- No commits by Wednesday → Email check-in
- No PR by Thursday → Direct message in Discussion
- No peer reviews by Friday → Reminder in next module
- Less than 10 commits → Offer support session

### Module 1 Learning Analytics to Track
- Average commits per student
- PR review quality progression
- Kevin interaction sophistication
- Time between Issue creation and PR
- Peer interaction network formation

---

*End of Module 1 - Congratulations on becoming a GitHub user and meeting your first AI teammate!*