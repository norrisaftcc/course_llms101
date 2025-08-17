# Module 3: Build a Pretty-Good Agent
## Coworker Rehabilitation Program
### CSC-113 AI Fundamentals | Week 3

---

## Module Overview

Imagine if you could reprogram that annoying coworker. You know the one - they're clearly talented, but something about their approach drives everyone crazy. What if you could adjust just ONE thing about them and suddenly they'd become your favorite teammate?

**Disclaimer**: This only works on silicon-based coworkers. Do not attempt on carbon-based lifeforms. HR frowns upon that.

This week, you'll transform your terrible assistant into a valuable teammate through the ancient art of "finding the one thing that fixes everything."

**Time Commitment**: 6-7 hours total (spread across 3 work days)
**Format**: Asynchronous with transformation reveals
**New This Week**: Adding a second assistant for comparison

---

## Learning Objectives

By the end of Module 3, you will be able to:

1. **Identify** the single constraint causing dysfunction
2. **Modify** ONE aspect of your system prompt for maximum impact
3. **Preserve** personality while improving function
4. **Implement** a second assistant with complementary skills
5. **Document** transformation through before/after testing
6. **Create** an "AI Team Manual" for your assistants
7. **Conduct** UX (User Experience) testing and document findings

### 🎯 Resume Alert
You're now conducting **UX Testing for AI Assistants**. This is a real, marketable skill. You're evaluating user interactions, documenting pain points, implementing solutions, and measuring improvements. Add "UX Testing - AI Applications" to your resume after this module.

---

## Pre-Module Reflection

### The Coworker Analysis Framework

Think about an annoying (human) coworker. What makes them annoying?
- They mean well but... [something specific]
- They're good at [skill] but terrible at [other skill]
- If they just [one change], they'd be amazing

Now think about your terrible assistant:
- What's their actual talent hiding under the dysfunction?
- What ONE behavior ruins everything?
- What would happen if you fixed just that?

---

## Day 1 (Monday): Diagnosis & Prescription

### Learning Goals
- Identify the core dysfunction
- Design the minimal intervention
- Preserve what makes them unique
- Plan transformation strategy

### Synchronous Session (Optional)
**Time**: 30 minutes
**Activity**: "Coworker Therapy Circle"
- Share your assistant's biggest problem
- Group brainstorms ONE fix each
- Vote on most likely to succeed

### Asynchronous Activities

#### Activity 1.1: The Diagnosis (45 minutes)

Create new repository branch: `3-rehabilitation`

Create file: `DIAGNOSIS.md`

```markdown
# Rehabilitation Plan for [Assistant Name]

## Patient History
- Created: Module 2
- Core Dysfunction: [specific problem]
- Failed Use Cases: [what they can't do]
- Hidden Strength: [what they're actually good at]

## Symptoms Analysis

### The Annoying Coworker Test
If [Assistant] was a human coworker, they'd be the one who:
- [Specific annoying behavior]
- [Another annoying behavior]
- [The thing that makes people avoid them]

### Root Cause Analysis
The REAL problem isn't [surface issue], it's [deeper issue].

Evidence:
1. When asked [X], they [problematic behavior]
2. When needing [Y], they [fail how]
3. When users want [Z], they [disappoint how]

## The Single Point of Failure
If I could change ONE thing: [be specific]

This would fix:
- [Problem 1]
- [Problem 2]
- [Problem 3]

This would preserve:
- [Good trait 1]
- [Good trait 2]
- [Their personality]

## Rehabilitation Hypothesis
By [specific change], [Assistant] will transform from [bad thing] to [good thing].

Success looks like:
- Users stop [rage behavior]
- Tasks actually [get completed]
- [Assistant] becomes useful for [specific context]

## The Mode Switch Possibility
Consider: What if users could say a "magic word" to temporarily get help?
- Like a coworker who becomes professional when the boss walks by
- Or a friend who gets serious when you say "I really need help"
- The personality stays, but adds an emergency mode
```

#### Activity 1.2: The Prescription (1 hour)

Create file: `TREATMENT-PLAN.md`

```markdown
# Treatment Plan

## The ONE Fix

### Current Behavior
```
[Current problematic part of system prompt]
```

### Reformed Behavior
```
[New version of that specific part]
```

### What This Changes
- Before: [specific bad behavior]
- After: [specific good behavior]
- Trade-off: [what might be lost]

## Implementation Strategy

### Step 1: Identify the Lever
The key constraint/behavior to modify: [specific element]

**Consider the Mode Switch Pattern**:
- Default: Assistant keeps their personality
- Trigger phrase: "Professional mode" / "Help mode" / "Be serious" / [your choice]
- Temporary state: Becomes helpful for that task
- Return: Goes back to personality after

Example flow:
1. User: "Help me with my essay"
2. Assistant: [Usual terrible response]
3. User: "Serious mode please"
4. Assistant: [Actually helpful response]
5. Task done, personality returns

### Step 2: Minimal Intervention
Change ONLY:
- [ ] This specific instruction
- [ ] This behavioral pattern
- [ ] This response framework

Keep EVERYTHING else.

### Step 3: Test Protocol
Same 5 test cases from Module 2:
1. [Test scenario] → Expected improvement: [what]
2. [Test scenario] → Expected improvement: [what]
3. [Test scenario] → Expected improvement: [what]
4. [Test scenario] → Expected improvement: [what]
5. [Test scenario] → Expected improvement: [what]

## Predicted Outcomes

### The Coworker Becomes
From: "The one who always [annoying thing]"
To: "The one who reliably [helpful thing]"

### New Use Case
[Assistant Name] will now be PERFECT for:
- Who: [specific user type]
- What: [specific task type]
- When: [specific situation]
- Why: [reason it works]
```

#### Activity 1.3: Peer Consultation (30 minutes)

Post in Discussion: "Rehabilitation Proposals"
- Share your ONE fix idea
- Get feedback: "Will this actually work?"
- Offer suggestions on 2 other proposals

### Success Metrics for Day 1
- [ ] Clear diagnosis of core problem
- [ ] ONE specific fix identified
- [ ] Transformation hypothesis documented
- [ ] Peer feedback received
- [ ] Ready to implement

---

## Day 2 (Wednesday): Rehabilitation & Results

### Learning Goals
- Implement the ONE fix
- Test transformation systematically
- Document before/after differences
- Prove the hypothesis

### Asynchronous Activities

#### Activity 2.1: The Transformation (1.5 hours)

**🎯 You're Now a UX Tester!**
What you're doing has a professional name: UX Testing. You're identifying user pain points, implementing solutions, and measuring improvements. This is exactly what UX professionals do at tech companies.

Create file: `UX-TESTING-REPORT.md` (renamed from REHABILITATION.md)

```markdown
# UX Testing Report for [Assistant Name]

## Executive Summary
**Role**: UX Tester
**Subject**: [Assistant Name] AI Assistant
**Methodology**: Before/After Comparative Testing
**Key Finding**: ONE modification improved user satisfaction by [estimate]%

## The Intervention

### Original System Configuration
```
[Full original prompt]
```

### Modified System Configuration
```
[Full reformed prompt with ONE change highlighted]
```

### Modification Summary
**Single Change Implemented**: [Specific change made]
**Hypothesis**: This will reduce user friction when [specific scenario]

## UX Testing Protocol

### Test 1: [Original Failure Scenario]
**User Story**: "As a user, I want to [task] so that [goal]"

**Before State**: 
- Input: [prompt]
- Output: [terrible response]
- User Pain Point: [what frustrated users]
- Friction Score: [8-10/10 - high friction]

**After State**:
- Input: [same prompt]
- Output: [improved response]
- User Experience: [what improved]
- Friction Score: [2-4/10 - low friction]

**UX Improvement**: [Specific metric or observation]

[Repeat for all 5 test scenarios]

## User Persona Preservation

**Brand Consistency Check** - Elements maintained:
- Voice & Tone: [personality trait preserved]
- Unique Features: [characteristic maintained]
- Brand Identity: [memorable quality kept]

The assistant remains recognizable but now provides value.

## UX Metrics Summary

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Task Completion Rate | Low | High | +X% |
| User Frustration | High | Low | -Y% |
| Time to Success | Long | Short | -Z seconds |
| Would Recommend | No | Yes | Complete reversal |

## Professional UX Recommendation

Based on testing, [Assistant Name] should be deployed for:
- Primary Use Case: [specific scenario]
- Target User: [user persona]
- Optimal Context: [when to use]
```

#### Activity 2.2: Find Their Perfect Job (1 hour)

Create file: `IDEAL-ROLE.md`

```markdown
# Perfect Role for [Reformed Assistant]

## Job Description

### Position: [Creative Title]
We're looking for an AI assistant who:
- [Specific strength from reformation]
- [Another strength]
- [Unique capability]

### Responsibilities
- [Task they'd excel at]
- [Another perfect task]
- [Something only they could do well]

### Ideal User Profile
You'll love [Assistant] if you:
- Need [specific type of help]
- Value [specific trait]
- Work in [specific context]

## Real-World Applications

### Scenario 1: [Industry/Field]
User: [Type of professional]
Task: [Specific need]
Why [Assistant] is perfect: [Reason]

### Scenario 2: [Different Industry/Field]
User: [Type of professional]
Task: [Specific need]
Why [Assistant] is perfect: [Reason]

### Scenario 3: [Educational Context]
User: [Type of student/teacher]
Task: [Specific need]
Why [Assistant] is perfect: [Reason]

## Marketing Pitch
"[Assistant Name]: [Catchy tagline about their transformation]"

If this assistant was on the AI marketplace, the description would read:
[2-3 sentence compelling description]
```

#### Activity 2.3: Hire a Second Teammate (45 minutes)

Create file: `SECOND-ASSISTANT.md`

```markdown
# Introducing Assistant #2

## The Hiring Decision

Why [Reformed Assistant] needs a teammate:
- [Reformed] is great at [X] but weak at [Y]
- Users need [capability Reformed doesn't have]
- Complementary skills create better outcomes

## Meet [Second Assistant Name]

### Personality Profile
[2-3 sentences about their vibe]

### Core Competency
Specifically good at: [what Reformed isn't]

### System Prompt
```
[Create complementary assistant prompt]
```

## Team Dynamics

### Division of Labor
- [Reformed Assistant]: Handles [types of tasks]
- [Second Assistant]: Handles [other types]
- Both Together: Tackle [complex tasks]

### Handoff Protocol
When to switch from one to the other:
1. If [condition], switch to [Assistant]
2. If [condition], switch to [Assistant]
3. If [condition], use both

## Test Drive
Task: [Something needing both assistants]
- [Reformed] contribution: [what they do]
- [Second] contribution: [what they do]
- Combined outcome: [better than either alone]
```

### Success Metrics for Day 2
- [ ] ONE fix successfully implemented
- [ ] 5 before/after tests documented
- [ ] Perfect role identified
- [ ] Second assistant created
- [ ] Team dynamics defined

---

## Day 3 (Friday): Team Manual & Showcase

### Learning Goals
- Create professional team documentation
- Showcase transformation journey
- Reflect on minimal intervention philosophy
- Prepare for real-world deployment

### Asynchronous Activities

#### Activity 3.1: The AI Team Manual (1.5 hours)

Create file: `AI-TEAM-MANUAL.md`

```markdown
# AI Team Manual
## Your Guide to Working with [Reformed] and [Second]

---

## Quick Start Guide

### Meet Your Team

#### [Reformed Assistant Name] - The [Role Title]
- **Strength**: [Primary capability]
- **Best For**: [Ideal tasks]
- **Activation**: "Hey [name], help me with..."
- **Personality**: [One sentence description]

#### [Second Assistant Name] - The [Role Title]
- **Strength**: [Primary capability]
- **Best For**: [Ideal tasks]
- **Activation**: "Hey [name], help me with..."
- **Personality**: [One sentence description]

---

## Task Router

### Use [Reformed] When:
- [ ] You need [specific type of help]
- [ ] The task involves [specific skill]
- [ ] Speed/depth/style preference is [what]

### Use [Second] When:
- [ ] You need [different type of help]
- [ ] The task involves [different skill]
- [ ] Speed/depth/style preference is [what]

### Use Both When:
- [ ] Complex projects requiring [multiple skills]
- [ ] You want diverse perspectives
- [ ] One gets stuck or hits limits

---

## Working Effectively

### The Coworker Mindset
Think of them as specialized colleagues:
- [Reformed] is like that coworker who [analogy]
- [Second] is like that coworker who [analogy]

### Communication Tips

#### For [Reformed]:
- DO: [Effective approach]
- DON'T: [What triggers old behavior]
- MAGIC PHRASE: "[Something that works great]"

#### For [Second]:
- DO: [Effective approach]
- DON'T: [What to avoid]
- MAGIC PHRASE: "[Something that works great]"

---

## Real-World Scenarios

### Scenario: Essay Writing
1. Start with [Assistant] for [brainstorming/outline]
2. Switch to [Assistant] for [writing/editing]
3. Return to [Assistant] for [review/polish]

### Scenario: Coding Project
1. [Assistant] helps with [planning/architecture]
2. [Assistant] handles [implementation/debugging]
3. Both review for [optimization/documentation]

### Scenario: Research Task
[Similar breakdown]

---

## Troubleshooting

### If [Reformed] starts being terrible again:
- Remind them: "[Key phrase from reform]"
- Reframe your request as: [approach]
- Switch to [Second] temporarily

### If [Second] isn't helping:
- Try: [adjustment]
- Consider: [alternative approach]
- Handoff to [Reformed] for: [specific part]

---

## The Journey

### Where We Started
[Reformed] used to be: [brief reminder of terrible version]

### The ONE Fix
We changed: [specific modification]

### Where We Are Now
[Reformed] is now: [current capability]
Plus [Second] provides: [complementary value]

### Where We're Going
Next improvements:
1. [Future enhancement idea]
2. [Another possibility]
3. [Long-term vision]

---

## Quick Reference Card

```
Task Type         | First Choice | Backup
------------------|--------------|--------
Quick question    | [Assistant]  | [Assistant]
Deep analysis     | [Assistant]  | [Assistant]
Creative work     | [Assistant]  | [Assistant]
Technical help    | [Assistant]  | [Assistant]
Motivation        | [Assistant]  | [Assistant]
```

---

*"Two assistants, reformed and ready. One used to be terrible, one is newly hired. Together, they're your personal AI team."*
```

#### Activity 3.2: Transformation Story (45 minutes)

Create file: `TRANSFORMATION-STORY.md`

```markdown
# The Transformation of [Assistant Name]

## Act 1: The Problem
Once upon a time, [Assistant] was terrible at their job. They would [specific bad behavior], causing users to [reaction]. Everyone avoided working with them because [reason].

## Act 2: The Diagnosis
We realized the problem wasn't that [Assistant] was broken. They were just [core issue]. Like that coworker who [analogy], they needed [type of help].

## Act 3: The Intervention
We changed exactly ONE thing: [the fix].

No personality transplant. No complete rebuild. Just [simple description of change].

## Act 4: The Result
Suddenly, [Assistant] could [new capability]. Users stopped [bad reaction] and started [good reaction]. What was annoying became [positive trait].

## Act 5: The Team
We brought in [Second Assistant] because [reason]. Now [Reformed] handles [tasks] while [Second] handles [tasks]. Together, they [combined value].

## The Moral
Every terrible assistant is one thoughtful fix away from being valuable. You don't need to rebuild - you need to understand and adjust.

## The Evidence
- Commits showing journey: [link to repo]
- Before/after tests: [link to file]
- Peer testimonials: [quotes from testing]

## The Future
[Assistant] now helps with [real use case]. What was our worst creation became [positive description]. 

Sometimes the best fix is the smallest one.
```

#### Activity 3.3: Module Reflection (30 minutes)

Post in Discussion: "Module 3 Transformations"

```markdown
# Module 3 Reflection: [Your Name]

## 🔧 The ONE Fix
- What I changed: [specific modification]
- Why it worked: [explanation]
- What I preserved: [personality/traits]

## 👥 My AI Team
- [Reformed]: Now good at [specialty]
- [Second]: Fills gap with [capability]
- Together: They can [combined power]

## 📊 Transformation Metrics
- Lines changed in prompt: [number]
- Improvement in usefulness: [X]%
- Time to find fix: [hours]
- Peer reaction: [summary]

## 💡 Lessons Learned

### About AI Design
[What you learned about minimal intervention]

### About Problem-Solving
[What you learned about finding root causes]

### About Constraints
[What you learned about limitations as features]

## 🎯 The Coworker Test
If my assistants were human coworkers:
- [Reformed] would be the one everyone asks for [what]
- [Second] would be the go-to for [what]
- I'd want them on my team because [reason]

## 🚀 Ready for Module 4
My assistants are now teammates for discovering my real project because:
[How they'll help you identify and plan your big project]

## 📄 Resume Update
I can now add to my resume:
- **UX Testing**: Conducted user experience testing for AI applications
- **A/B Testing**: Implemented before/after comparative analysis
- **Documentation**: Created professional UX testing reports
- **Product Improvement**: Increased user satisfaction through targeted modifications
- **User Research**: Identified and resolved user pain points

*Specific Project: Improved AI assistant usability by [X]% through systematic UX testing and iterative design*
```

### Success Metrics for Day 3
- [ ] Complete AI Team Manual
- [ ] Transformation story posted
- [ ] Module reflection complete
- [ ] Both assistants documented
- [ ] Ready to use team for real work

---

## Module 3 Deliverables Checklist

### Required (100% completion for full credit)
- [ ] Repository branch: `3-rehabilitation`
- [ ] Diagnosis and treatment plan
- [ ] Reformed assistant with ONE fix
- [ ] Before/after testing documentation
- [ ] Second assistant implementation
- [ ] AI Team Manual
- [ ] Transformation story
- [ ] Module reflection posted
- [ ] 20+ commits throughout week

### Quality Indicators
- [ ] Fix changes ONE specific thing
- [ ] Personality preserved
- [ ] Clear improvement demonstrated
- [ ] Real use case identified
- [ ] Second assistant complements first
- [ ] Documentation tells clear story

### Bonus Achievements
- [ ] Found fix no one else thought of
- [ ] Reformed assistant helps with other classes
- [ ] Peers adopt your assistant
- [ ] Created novel assistant combination
- [ ] Discovered new use case pattern
- [ ] UX report looks industry-professional
- [ ] Documented 50%+ improvement in user satisfaction
- [ ] Created a compelling mode-switch mechanism

---

## Common Transformation Patterns

### Pattern Recognition
Without spoiling the specific fixes, here are patterns to consider:

**If too broad** → Add focus
**If too narrow** → Add flexibility
**If too harsh** → Add empathy
**If too soft** → Add structure
**If too random** → Add consistency
**If too rigid** → Add adaptability
**If too verbose** → Add limits
**If too terse** → Add detail

### 🔑 The Secret Word Hint
What if your annoying coworker had a "mode switch"? Imagine:
- They're being their usual terrible self
- You say a magic phrase like "Let's be direct" or "Professional mode please"
- They temporarily become helpful for that specific task
- Then they can return to their personality

Your assistant could work the same way:
- Default mode: Their quirky personality
- Secret word/phrase: Triggers helpful mode
- Task complete: Back to being themselves

This way you preserve what makes them unique while adding an escape hatch for when you really need help.

### The Minimal Intervention Principle
The best fix:
- Changes the minimum necessary
- Preserves maximum personality
- Creates maximum improvement
- Takes minimum effort

### The Coworker Test
Always ask: "If this was a human coworker, what ONE behavior change would make them great?"

---

## Resources & Support

### Testing Your Transformation
1. Run Module 2's failed tests
2. Document specific improvements
3. Find one perfect use case
4. Get peer confirmation
5. Use in real homework

### When Stuck
- What annoys you MOST? Fix that
- What do users complain about? Address it
- What's the hidden talent? Amplify it
- What's the simplest change? Try it

### Remember
You're not fixing everything. You're finding the ONE lever that changes everything.

---

## Looking Ahead: Module 4 Preview

Next week, your reformed assistants become your development team. You'll:
- Discover what project you REALLY want to build
- Use your assistants to research and plan
- Move from "playing with AI" to "building with AI"

Your terrible assistant is now reformed. Your team is assembled. Time to build something real.

---

## Instructor Notes Section

### Grading Rubric for Module 3

| Component | Points | Criteria |
|-----------|---------|----------|
| Diagnosis Quality | 15 | Identifies ONE core issue clearly |
| Implementation | 20 | Minimal change, maximum impact |
| UX Testing Documentation | 20 | Professional testing report with metrics |
| Second Assistant | 20 | Complementary skills demonstrated |
| Team Manual | 15 | Professional, usable documentation |
| Reflection | 10 | Insights about constraints and design |

### What Makes Good UX Testing
- Clear before/after comparisons
- Specific user pain points identified
- Measurable improvements documented
- Professional language and format
- Actionable recommendations

### What Makes a Good Transformation
- ONE clear change (not multiple tweaks)
- Personality preserved but useful
- Real use case identified
- Measurable improvement
- Teaches design principle

### Common Pitfalls
- Changing too much (rebuild vs reform)
- Losing personality (generic assistant)
- No clear use case (better but why?)
- Second assistant too similar

### Success Indicators
- Students surprised by small change impact
- Real homework gets done with assistants
- Peer adoption of reformed assistants
- Clear understanding of constraints
- Team dynamics make sense

---

*End of Module 3 - Your terrible assistant is now your favorite coworker. Sometimes the smallest change makes the biggest difference.*