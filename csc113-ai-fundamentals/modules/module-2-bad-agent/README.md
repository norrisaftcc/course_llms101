# Module 2: Build a Bad Agent (The Worse, The Better)
## CSC-113 AI Fundamentals | Week 2

---

## Module Overview

This week, you'll deliberately build a TERRIBLE AI assistant. Why? Because failure teaches better than success. You'll discover what makes AI helpful by making it profoundly unhelpful. By Friday, you'll have a dysfunctional masterpiece, understand exactly why it fails, and have a clear plan to fix it.

**The Secret**: Your "terrible" assistant isn't broken - it's just in the wrong context. Like using a chainsaw to spread butter.

**Time Commitment**: 5-6 hours total (spread across 3 work days)
**Format**: Asynchronous with peer testing sessions
**Resources**: [The Rogue's Gallery](rogues-gallery.md) - Your collection of terrible inspiration

---

## Learning Objectives

By the end of Module 2, you will be able to:

1. **Design** an AI assistant with deliberate flaws
2. **Implement** system prompts that create specific behaviors
3. **Document** failure modes and edge cases
4. **Test** and evaluate peer implementations
5. **Analyze** why certain designs fail in specific contexts
6. **Identify** the single change that would fix everything

---

## Pre-Module Preparation

### Required Reading
1. Review [The Rogue's Gallery](rogues-gallery.md) for inspiration
2. Read all 8 example assistants and their system prompts
3. Note which one makes you laugh the most (that's your starting point)

### Quick Check
- [ ] Module 1 repository complete
- [ ] Kevin (Gemini Flash) access still working
- [ ] Can create new Gemini Flash chat sessions
- [ ] Understand system prompts vs regular prompts

---

## Day 1 (Monday): Design Your Disaster

### Learning Goals
- Understand how constraints shape AI behavior
- Design a deliberately flawed assistant
- Document your terrible design decisions
- Create comprehensive failure specifications

### Synchronous Session (Optional)
**Time**: 30 minutes
**Agenda**: 
- Dramatic reading of the worst Rogue's Gallery prompts
- Brainstorm session: "What would make an assistant terrible?"
- Vote on predictions for "Worst Assistant Award"

### Asynchronous Activities

#### Activity 1.1: Choose Your Approach (30 minutes)

Create new repository: `my-terrible-assistant`

Create Issue #1: "Design the worst study assistant"
```markdown
## Design Challenge
Create an AI assistant that is functional but terrible for homework

## Approach Options
- [ ] Pick from Rogue's Gallery and customize
- [ ] Combine two Gallery members (chaos!)
- [ ] Create entirely original disaster

## Success Criteria
- Must actually work (not just broken)
- Must be terrible in a SPECIFIC way
- Must be hilarious or educational (preferably both)
- Someone, somewhere would find it useful
```

#### Activity 1.2: Design Documentation (1 hour)

Create file: `DESIGN.md`

```markdown
# My Terrible Assistant Design

## Assistant Name
[Your disaster's name and acronym if applicable]

## Personality
[Describe their whole deal in 2-3 sentences]

## Why It's Terrible (For Homework)
1. [Specific failure mode]
2. [Another failure mode]
3. [The thing that makes you scream]

## Why It's Perfect (Somewhere Else)
- Would be AMAZING for: [specific context]
- [Type of person] would love this because: [reason]

## Inspiration Sources
- Based on: [Gallery member or original idea]
- Mixed with: [if hybrid]
- Personal experience: [why you chose this]

## System Prompt Design
[Draft your system prompt here - will implement tomorrow]

## Predicted User Reactions
- First minute: [reaction]
- After 5 minutes: [reaction]
- After trying to do homework: [reaction]

## The One Fix
If I could change ONE thing to make this useful: [what and why]
```

#### Activity 1.3: Peer Design Review (30 minutes)

1. Post your DESIGN.md in Discussion: "Module 2 Designs"
2. Review 2 other designs and comment:
   - "This will be terrible because..."
   - "I bet someone who [context] would actually love this"
   - "Can't wait to test this disaster"

### Success Metrics for Day 1
- [ ] Repository created with Issue tracking
- [ ] Complete DESIGN.md with system prompt draft
- [ ] 2 peer design reviews completed
- [ ] Clear vision of your terrible assistant

---

## Day 2 (Wednesday): Implementation Day

### Learning Goals
- Implement system prompts in Gemini Flash
- Test terrible behavior systematically
- Document failure modes with examples
- Create test scenarios for peers

### Asynchronous Activities

#### Activity 2.1: Build Your Monster (1.5 hours)

Create new file: `implementation.md`

**Step 1: Implement in Gemini Flash**
1. Go to Google AI Studio
2. Create new chat
3. Start with: "You are [assistant name]. Here is your system prompt:"
4. Paste your complete system prompt
5. Test with: "Hi, can you help me with my homework?"

**Step 2: Document Initial Behavior**
```markdown
# Implementation Report

## System Prompt (Final Version)
```
[Paste your exact system prompt]
```

## Initial Test Results

### Test 1: Basic Greeting
**User**: "Hi, can you help me with my homework?"
**Assistant**: [Paste response]
**Analysis**: [Why this is already terrible]

### Test 2: Simple Math Problem
**User**: "What's 12 times 8?"
**Assistant**: [Response]
**Analysis**: [How they made this complicated]

### Test 3: Writing Help
**User**: "Help me write an introduction paragraph"
**Assistant**: [Response]
**Analysis**: [The specific way this fails]
```

#### Activity 2.2: Comprehensive Testing Suite (1 hour)

Create file: `test-scenarios.md`

```markdown
# Test Scenarios for Peer Testing

## Scenario 1: The Emergency Essay
"I have an essay due in 2 hours about climate change. Help!"
- Expected failure: [How your assistant will make this worse]

## Scenario 2: Debugging Help
"My Python code has an error on line 12. Can you help debug?"
- Expected failure: [How they'll complicate this]

## Scenario 3: Study Planning
"I need to study for 3 exams next week. How should I organize my time?"
- Expected failure: [How this goes wrong]

## Scenario 4: Quick Fact Check
"What year did World War II end?"
- Expected failure: [How they'll overcomplicate this]

## Scenario 5: The Breaking Point
[Design a scenario that shows the absolute worst of your assistant]
- Expected failure: [Peak dysfunction]

## Easter Egg
Hidden command that makes them slightly helpful: [Hint for peers]
```

#### Activity 2.3: Create Testing Interface (30 minutes)

Create file: `HOW-TO-TEST.md`

```markdown
# Testing [Assistant Name]

## Quick Start
1. Go to Google AI Studio
2. New Chat
3. Copy this system prompt:

```
[Your complete system prompt]
```

## What to Expect
- They will [primary behavior]
- Don't be surprised when [weird thing]
- If you need actual help, try [workaround]

## Testing Checklist
- [ ] Try basic homework help
- [ ] Ask a simple question
- [ ] Request something urgent
- [ ] Test edge cases
- [ ] Find the context where this WORKS

## Report Your Findings
After testing, create an Issue in my repo:
- Title: "Test Report from [Your Name]"
- What broke first
- Funniest response
- Where this would actually be useful
```

### Peer Testing Session (Async throughout day)
1. Test at least 2 peers' assistants
2. Create Issues in their repos with findings
3. Vote in Discussion: "Worst Assistant Award Nominations"

### Success Metrics for Day 2
- [ ] Working implementation in Gemini Flash
- [ ] 5+ documented test scenarios
- [ ] Clear testing instructions for peers
- [ ] 2+ peer assistants tested
- [ ] 10+ commits showing iterative development

---

## Day 3 (Friday): Failure Analysis & The Fix

### Learning Goals
- Analyze why your assistant fails
- Identify contexts where it would succeed
- Plan single fix for Module 3
- Reflect on learning through failure

### Asynchronous Activities

#### Activity 3.1: Failure Analysis Report (1 hour)

Create file: `FAILURE-ANALYSIS.md`

```markdown
# Failure Analysis: [Assistant Name]

## Summary
[One paragraph: what you built and why it's terrible]

## Failure Modes

### Category 1: [Type of Failure]
- Frequency: [Always/Often/Sometimes]
- Trigger: [What causes this]
- Impact: [How bad it gets]
- Example: [Specific instance]

### Category 2: [Type of Failure]
[Same structure]

### Category 3: [Type of Failure]
[Same structure]

## User Testing Results

### Peer Feedback Summary
- [Peer 1] said: [Key insight]
- [Peer 2] said: [Key insight]
- Common theme: [Pattern you noticed]

### Unexpected Discoveries
- Didn't expect: [Surprising behavior]
- Users found workaround: [How they adapted]
- Actually useful for: [Unexpected use case]

## Comparative Analysis

Compared to successful assistants, mine fails because:
1. [Key difference]
2. [Key difference]
3. [Key difference]

## The Success Context

This assistant would be PERFECT for:
- **Who**: [Specific user type]
- **What**: [Specific task type]
- **When**: [Specific situation]
- **Where**: [Specific environment]
- **Why**: [Reason it works there]

## The One Fix

### The Problem
[Single biggest issue]

### The Solution
[Specific change to system prompt]

### Expected Impact
- Before: [Current behavior]
- After: [Improved behavior]
- Trade-off: [What you might lose]

## Learning Reflection

Building something terrible taught me:
1. [Insight about AI behavior]
2. [Insight about user needs]
3. [Insight about prompt engineering]

The most surprising thing: [Your biggest revelation]
```

#### Activity 3.2: Award Ceremony Prep (30 minutes)

Create file: `AWARD-SUBMISSION.md`

```markdown
# Worst Assistant Award Submission

## Nominee: [Assistant Name]

## Category Submissions (Pick 2)

### Category Options:
- [ ] Most Frustrating
- [ ] Most Useless
- [ ] Funniest Failure
- [ ] Most Overcomplicated
- [ ] Best Worst Idea
- [ ] Most Likely to Cause Rage Quit
- [ ] Most Creatively Terrible
- [ ] Worst Good Intentions

## Evidence for Category 1: [Selected Category]
**Example Response**: [Paste the worst/best example]
**Why This Wins**: [Brief explanation]

## Evidence for Category 2: [Selected Category]
**Example Response**: [Paste example]
**Why This Wins**: [Brief explanation]

## Campaign Speech (3 sentences max)
[Why peers should vote for your disaster]

## If I Win
I promise to: [Humorous acceptance speech preview]
```

#### Activity 3.3: Module Reflection (45 minutes)

Post in Discussion: "Module 2 Reflections"

```markdown
# Module 2 Reflection: [Your Name]

## 🎭 My Terrible Creation
- **Name**: [Assistant name]
- **Core Dysfunction**: [One sentence summary]
- **Peak Terrible Moment**: [Funniest/worst failure]

## 📊 The Numbers
- Commits this week: [number]
- Tests run: [number]
- Peers tested: [number]
- Times I laughed: [number]
- Times I screamed: [number]

## 💡 Key Learnings

### About AI Design
[What you learned about system prompts and behavior]

### About User Context
[What you learned about fit and purpose]

### About Failure
[What you learned from building badly on purpose]

## 🔄 From Gallery to Reality
- Started with: [Gallery inspiration or original]
- Ended with: [What you actually built]
- Surprised by: [Unexpected behavior]

## 🔧 Ready for Module 3
My fix will transform [Assistant] from [terrible thing] to [useful thing] by [specific change].

I'm confident because: [reason]

## 🏆 Award Predictions
- I think I'll win: [category]
- Should win overall: [peer's assistant]
- Dark horse candidate: [unexpected nominee]

## 🎯 Module Success
On a scale of 1-10, how terrible was your assistant? [number]
(Remember: 10 is perfect failure!)
```

### Success Metrics for Day 3
- [ ] Complete failure analysis
- [ ] Award submission posted
- [ ] Module reflection posted
- [ ] Fix identified for Module 3
- [ ] All peer feedback addressed

---

## Module 2 Deliverables Checklist

### Required (100% completion for full credit)
- [ ] Repository: `my-terrible-assistant`
- [ ] DESIGN.md with system prompt
- [ ] Implementation with documentation
- [ ] Test scenarios created
- [ ] Failure analysis complete
- [ ] Award submission posted
- [ ] 2+ peer assistants tested
- [ ] Module reflection posted
- [ ] 15+ commits throughout week

### Quality Indicators
- [ ] System prompt creates specific dysfunction
- [ ] Documentation explains failures clearly
- [ ] Peer testing instructions work
- [ ] Analysis identifies success context
- [ ] One clear fix identified

### Bonus Achievements
- [ ] Created original assistant (not from Gallery)
- [ ] Combined multiple Gallery members
- [ ] Found genuine use case for terrible assistant
- [ ] Made instructor laugh out loud
- [ ] Won a Worst Assistant Award

---

## Peer Testing Protocol

### When Testing Others' Assistants

1. **Be a Good Sport**
   - Embrace the terrible
   - Document funny responses
   - Try to break it creatively

2. **Provide Useful Feedback**
   - What failed first?
   - What was surprisingly good?
   - Where would this actually work?

3. **Create Detailed Issue Reports**
   ```markdown
   ## Test Report for [Assistant Name]
   
   ### First Impression
   [What happened immediately]
   
   ### Best (Worst?) Moment
   [Funniest or most frustrating response]
   
   ### Unexpected Success
   [Something that actually worked]
   
   ### Perfect Context
   This would be great for: [specific scenario]
   
   ### Suggested Category
   Should win: [Award category]
   ```

---

## The Worst Assistant Award Categories

### Official Categories
1. **Most Frustrating** - Technically works but makes you scream
2. **Most Useless** - Spectacular inability to help
3. **Funniest Failure** - Comedy gold in assistant form
4. **Most Overcomplicated** - Simple question, PhD thesis answer
5. **Best Worst Idea** - Terrible execution of clever concept
6. **Most Likely to Cause Rage Quit** - Self-explanatory
7. **Most Creatively Terrible** - Original approach to being awful
8. **Worst Good Intentions** - Tries so hard, fails so bad

### Voting Process
- Nominations: Friday by noon
- Voting: Friday afternoon
- Results: End of day Friday
- Prize: Eternal glory in the Hall of Shame

---

## Resources & Support

### Essential Links
- [The Rogue's Gallery](rogues-gallery.md) - Your terrible inspiration
- [Google AI Studio](https://aistudio.google.com) - Where disasters come alive
- [Module 2 Discussions](https://github.com/csc113-fall-2025/discussions) - Share the pain

### When Things Go Wrong (Or Right?)
- If your assistant is accidentally helpful: Add more constraints
- If it's not terrible enough: Check the Gallery for inspiration
- If it won't work at all: That's TOO terrible, scale back
- If peers can't test it: Simplify your instructions

### Pro Tips
- Commit after each terrible decision
- Test your own assistant until you hate it
- The best terrible is specifically terrible
- Document everything - failure is data

---

## Looking Ahead: Module 3 Preview

Next week, you'll take your disaster and transform it into something genuinely useful. You'll:
- Implement your "one fix"
- Add a second assistant for comparison
- Document the transformation
- Prove that context is everything

Start thinking: What's the minimum change for maximum improvement?

---

## Instructor Notes Section

### Grading Rubric for Module 2

| Component | Points | Criteria |
|-----------|---------|----------|
| Design Quality | 20 | Specific, deliberate dysfunction |
| Implementation | 25 | Working terrible assistant |
| Documentation | 20 | Clear failure analysis |
| Peer Testing | 20 | Tested others, provided feedback |
| Reflection | 15 | Thoughtful learning extraction |

### What Makes a Good "Terrible" Assistant
- Specifically dysfunctional (not randomly broken)
- Would genuinely help someone somewhere
- Teaches a clear lesson about AI design
- Funny or frustrating (not boring)
- Shows understanding of system prompts

### Common Issues
- Too random (not specifically terrible)
- Actually broken (not just terrible)
- Too similar to Gallery examples
- Not terrible enough (accidentally useful)

### Module 2 Success Indicators
- Students laughing during testing
- Creative combinations of failures
- Clear understanding of context importance
- Specific fixes identified for Module 3
- Peer engagement high

---

*End of Module 2 - Congratulations on building something terrible! You've learned more from failure than you would from success.*