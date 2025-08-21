# Weeks 1-2: Learning GitHub & Scrum Through AI Assistant Development
## "You Can't Complete Your Feature Without These Skills"

### Core Learning Philosophy
Students learn project management and agile methodology **not as abstract concepts** but as **the only way to complete their work**. Every GitHub action and Scrum practice is introduced as "here's what you need to do to finish your assistant."

---

## Week 1: Sprint 1 - Administrative Assistant Feature

### **Day 1: Project Setup (The Only Way to Start)**
**Feature Goal:** "Create workspace for your AI assistant project"

#### Morning: "Every Developer Needs a Workspace"
**GitHub Concepts Learned Through Necessity:**

**Step 1: Repository Creation**
```
"To build your assistant, you need somewhere to store your work. 
Here's how developers do it:"

1. Create GitHub account (if needed)
2. Create repository: "my-ai-assistants" 
3. Initialize with README
4. Add description: "CSC-113 AI Assistant Development Project"
```

**Step 2: Issue Creation (Project Planning)**
```
"Before any developer writes code, they create an Issue describing what they're building:"

Navigate to Issues tab → New Issue
Title: "Feature: Administrative Assistant"
Description template:
---
## User Story
As a [student/professional/person], I need an administrative assistant that can help me with [specific tasks] so that I can [achieve specific goals].

## Acceptance Criteria
- [ ] Assistant responds to basic administrative requests
- [ ] Response time is under 30 seconds
- [ ] Tone matches my communication style
- [ ] Can handle scheduling, planning, and organization tasks

## Definition of Done
- [ ] Prompt is tested and working
- [ ] Documentation is complete
- [ ] Prompt is committed to repository
- [ ] Ready for peer review
---
```

**What Students Just Learned:**
- Repository as project workspace
- Issues as feature planning
- User stories and acceptance criteria
- Definition of Done concept

#### Afternoon: "Professional Development Workflow"
**Branch Creation & Setup**

```
"No developer works directly on the main code. Here's the professional way:"

1. Create branch from Issue: "1-administrative-assistant"
2. Clone or edit in GitHub Codespaces/web interface
3. Create folder structure:
   /assistants
     /admin-assistant
       prompt.md
       test-results.md
       README.md
```

**What Students Learn:**
- Feature branching
- Project organization
- Working in isolation from main code

**Homework:** Write first draft of admin assistant prompt in `prompt.md`

### **Day 2: Sprint Development - Prompt Engineering**
**Feature Goal:** "Build and test your administrative assistant"

#### Morning: "Iterative Development Process"
**Scrum Concepts Through Daily Practice:**

**Daily Standup (5 minutes)**
Each student reports:
- What I completed yesterday: [Repository setup, initial prompt draft]
- What I'm working on today: [Prompt testing and refinement]
- Any blockers: [Gemini Flash access issues, unclear requirements]

**Sprint Work: Prompt Development**
```
Students work in their feature branch:

1. Edit prompt.md with initial assistant prompt
2. Test prompt in Gemini Flash web interface
3. Document results in test-results.md
4. Iterate based on results
5. Commit changes with descriptive messages
```

**Commit Message Learning:**
```
"Every change needs a clear description for your team:"

Good commit messages:
- "Add initial admin assistant prompt v1"
- "Fix scheduling response format issue"  
- "Update prompt to handle task prioritization"

Bad commit messages:
- "Update"
- "Fix stuff"
- "Changes"
```

#### Afternoon: "Testing and Quality Assurance"
**Testing Methodology Through Practice:**

**Test Cases Students Must Complete:**
```
Create test-results.md documenting:

Test 1: Basic Scheduling
Input: "Help me plan my Tuesday"
Expected: Organized response asking clarifying questions
Actual: [paste response]
Status: Pass/Fail/Needs Work

Test 2: Task Prioritization  
Input: "I have homework, work, and social plans. Help me prioritize"
Expected: Clear prioritization with reasoning
Actual: [paste response]
Status: Pass/Fail/Needs Work

Test 3: Quick Organization
Input: "My desk is a mess. Quick advice?"
Expected: Fast, actionable advice
Actual: [paste response]
Status: Pass/Fail/Needs Work
```

**What Students Learn:**
- Test-driven development mindset
- Documentation standards
- Quality assurance processes

### **Day 3: Code Review & Integration**
**Feature Goal:** "Get your assistant reviewed and deployed"

#### Morning: "Pull Request Creation"
**Professional Review Process:**

```
"No feature goes live without review. Here's how to request it:"

1. Push your branch to GitHub
2. Create Pull Request
3. Title: "Feature: Administrative Assistant [Closes #1]"
4. Description:
   - Summary of what was built
   - Link to test results
   - Any issues or limitations noted
   - Request specific feedback
```

**Pull Request Template Students Use:**
```markdown
## Feature Summary
Built administrative assistant for [brief description of your use case]

## Testing Completed
- [x] Basic scheduling functionality
- [x] Task prioritization  
- [x] Quick organization advice
- [ ] Advanced calendar integration (future enhancement)

## Documentation
- Prompt is documented in /assistants/admin-assistant/prompt.md
- Test results available in test-results.md
- README updated with usage instructions

## Review Requests
- Does the prompt clarity meet professional standards?
- Are there edge cases I should test?
- How can I improve the assistant's responses?

Closes #1
```

#### Afternoon: "Peer Review Process"
**Code Review Learning Through Practice:**

**Students Review Classmate PRs:**
```
Review checklist provided:
- [ ] Prompt is clear and well-structured
- [ ] Test results show working functionality  
- [ ] Documentation explains how to use assistant
- [ ] Commit messages are descriptive
- [ ] No sensitive information exposed

Feedback framework:
1. What works well
2. Suggestions for improvement
3. Questions about approach
4. Approval or "Request Changes"
```

**What Students Learn:**
- Constructive feedback techniques
- Quality standards
- Collaborative development
- Professional communication

### **Day 4: Merge & Sprint Retrospective**
**Feature Goal:** "Deploy your assistant and plan improvements"

#### Morning: "Feature Deployment"
**Merge Process:**
```
After PR approval:
1. Merge pull request
2. Delete feature branch  
3. Close Issue #1
4. Update main README with assistant description
5. Tag release: "v1.0-admin-assistant"
```

#### Afternoon: "Sprint Retrospective"
**Agile Reflection Process:**

**Retrospective Framework Students Use:**
```markdown
## Sprint 1 Retrospective: Administrative Assistant

### What Went Well (Keep Doing)
- Testing process helped me improve my prompt
- Branching kept my work organized
- Peer review caught issues I missed

### What Didn't Go Well (Stop Doing)  
- Waited too long to start testing
- Commit messages were unclear at first
- Didn't read requirements carefully enough

### What Could Be Better (Start Doing)
- Test more edge cases earlier
- Ask for help sooner when stuck
- Write clearer documentation

### Action Items for Next Sprint
- [ ] Start testing on Day 1
- [ ] Create commit message checklist
- [ ] Set up regular check-ins with study partner
```

**What Students Learn:**
- Continuous improvement mindset
- Self-reflection skills
- Team learning principles

---

## Week 2: Sprint 2 - Deep Thinking Assistant Feature

### **Day 5: Sprint Planning**
**Feature Goal:** "Plan development of your analytical assistant"

#### Morning: "Sprint Planning Meeting"
**Agile Planning Through Necessity:**

**Issue Creation for Sprint 2:**
```
Students create Issue #2: "Feature: Deep Thinking Assistant"

User Story:
As a [student/professional], I need a deep thinking assistant that can help me analyze complex problems so that I can make better decisions and understand issues thoroughly.

Sprint Goals:
- Build assistant focused on analytical thinking
- Test with real academic/professional problems  
- Compare effectiveness with admin assistant
- Document when to use which assistant

Story Points Estimation:
Students estimate effort: Small/Medium/Large
(Learning basic agile estimation)
```

**Sprint Backlog Creation:**
```
Break down into tasks:
- [ ] Research analytical prompt strategies
- [ ] Create initial prompt draft  
- [ ] Test with complex scenarios
- [ ] Refine based on results
- [ ] Document usage guidelines
- [ ] Create comparative analysis
- [ ] Submit for review
```

#### Afternoon: "Advanced Branching Strategy"
**Professional Git Workflow:**

```
"For more complex features, developers use advanced branching:"

1. Create branch: "2-deep-thinking-assistant"
2. Set up folder structure:
   /assistants
     /deep-thinking-assistant  
       prompt.md
       test-scenarios.md
       usage-guide.md
       comparison-with-admin.md
3. Create initial commits for file structure
```

### **Day 6-7: Development Sprint**
**Feature Goal:** "Build and iterate on your analytical assistant"

#### Daily Standups & Sprint Work
**Agile Development Cycle:**

**Each Day Starts With:**
- 5-minute standup (progress, plan, blockers)
- Review of yesterday's commits and tests
- Plan for today's iteration cycle

**Development Workflow Students Follow:**
```
1. Write/refine prompt
2. Test with real scenario
3. Analyze results  
4. Identify improvements
5. Commit changes
6. Repeat

Each commit represents one iteration cycle
Students learn rapid prototyping and continuous improvement
```

**Advanced Testing Scenarios:**
```
Students must test with increasingly complex problems:

Day 6: Academic scenarios
- "Help me analyze this research paper's methodology"
- "What are the implications of this historical event?"

Day 7: Professional scenarios  
- "Analyze the pros and cons of this business decision"
- "Help me prepare for a difficult conversation with my boss"

Real-world application teaches prompt engineering
```

### **Day 8: Integration & Comparison**
**Feature Goal:** "Compare assistants and create usage guidelines"

#### Morning: "Comparative Analysis"
**Systems Thinking Through Practice:**

**Students Create Comparison Document:**
```markdown
## Assistant Comparison Analysis

### Speed Test
Admin Assistant: [average response time]
Deep Thinking Assistant: [average response time]
Winner: Admin for quick tasks

### Complexity Handling
Test scenario: [complex problem description]
Admin Assistant result: [summary]
Deep Thinking Assistant result: [summary]  
Winner: Deep Thinking for analysis

### Usage Guidelines
Use Admin Assistant when:
- Need quick response
- Simple task organization
- Basic scheduling/planning

Use Deep Thinking Assistant when:
- Complex problem analysis
- Multiple perspectives needed
- Strategic decision making
- Research and investigation
```

#### Afternoon: "Documentation & Knowledge Sharing"
**Professional Documentation Standards:**

**Students Create README.md:**
```markdown
# My AI Assistant Ecosystem

## Overview
This repository contains two specialized AI assistants built for personal productivity and problem-solving.

## Assistants

### Administrative Assistant
- **Purpose**: Fast responses for daily tasks
- **Best for**: Scheduling, organization, quick decisions
- **Response time**: < 30 seconds
- **Usage**: [link to prompt.md]

### Deep Thinking Assistant  
- **Purpose**: Complex analysis and strategic thinking
- **Best for**: Research, decision analysis, problem-solving
- **Response time**: 2-5 minutes for thorough analysis
- **Usage**: [link to prompt.md]

## Quick Start Guide
1. Choose appropriate assistant based on your need
2. Copy prompt from respective folder
3. Paste into Gemini Flash web interface
4. Customize with your personal context
5. Begin conversation

## Testing Results
Both assistants have been tested with [X] scenarios
See individual test-results.md files for details

## Contributing
This is a learning project for CSC-113
Feedback welcome via GitHub Issues
```

### **Day 9-10: Final Review & Sprint Demo**
**Feature Goal:** "Present your assistant ecosystem professionally"

#### Day 9: "Final Pull Request & Review"
**Professional Quality Standards:**

**Students Submit Final PR:**
```
Title: "Feature: Deep Thinking Assistant & Complete Ecosystem [Closes #2]"

Description includes:
- Complete feature summary
- Comparative analysis results  
- Usage documentation
- Test coverage report
- Future enhancement ideas
```

**Advanced Peer Review:**
```
Students review for:
- Professional documentation quality
- Comprehensive testing coverage
- Clear usage guidelines
- Effective prompt engineering
- Professional Git workflow
```

#### Day 10: "Sprint Demo & Planning"
**Agile Demonstration & Retrospective:**

**Demo Format (10 minutes per student):**
```
1. Problem statement (2 min)
   "Here's what I was trying to solve..."

2. Solution demonstration (4 min)
   Live demo of both assistants solving real problems

3. Technical approach (2 min)  
   "Here's how I built and tested them..."

4. Lessons learned (2 min)
   "Here's what I discovered about prompt engineering..."
```

**Final Retrospective:**
```
## Two-Week Sprint Retrospective

### Project Management Skills Learned
- Issue tracking and feature planning
- Branching and version control
- Pull request and code review
- Documentation standards
- Testing methodologies

### AI Skills Developed  
- Prompt engineering strategies
- Comparative analysis techniques
- Use case identification
- Quality assurance for AI outputs

### Professional Skills Gained
- GitHub workflow proficiency
- Agile development practices
- Peer collaboration techniques
- Technical presentation skills

### Next Sprint Planning
Students identify what they want to build next:
- Path A: Prompt Masters (advanced workflows)
- Path B: Code Builders (web applications)
```

---

## What Students Actually Learn (Without Realizing It)

### GitHub Skills Mastered Through Necessity
- Repository management
- Issue tracking and project planning
- Feature branching workflow
- Pull request process
- Code review and collaboration
- Documentation standards
- Version control best practices

### Scrum/Agile Methodology Internalized
- Sprint planning and goal setting
- Daily standups and progress tracking
- Iterative development cycles
- Sprint retrospectives and improvement
- User story creation
- Definition of Done
- Continuous integration practices

### Professional Development Habits
- Systematic testing and quality assurance
- Clear communication and documentation
- Constructive peer feedback
- Continuous learning and adaptation
- Professional presentation skills

### AI-Specific Competencies
- Prompt engineering through iteration
- Systematic testing of AI outputs
- Comparative analysis of AI performance
- Use case identification and optimization
- Quality evaluation frameworks

---

## Assessment Rubric (Weeks 1-2)

### GitHub Workflow Competency (25%)
- **Proficient**: Consistent use of Issues, branches, PRs, clear commits
- **Developing**: Some workflow elements missing or unclear
- **Beginning**: Basic repository use but missing professional practices

### Agile Practice Demonstration (25%)
- **Proficient**: Clear sprint planning, daily progress, effective retrospectives
- **Developing**: Some agile practices evident but inconsistent
- **Beginning**: Limited evidence of iterative development approach

### AI Assistant Functionality (25%)  
- **Proficient**: Both assistants work effectively for intended use cases
- **Developing**: One assistant works well, other needs improvement
- **Beginning**: Basic functionality but limited effectiveness

### Professional Communication (25%)
- **Proficient**: Clear documentation, effective peer reviews, professional presentations
- **Developing**: Good communication in some areas, needs work in others  
- **Beginning**: Basic communication but lacks professional polish

### Success Metrics
**By Week 2 End, Every Student Has:**
- Working GitHub repository with professional README
- Two functional AI assistants with documented testing
- Experience with complete agile development cycle
- Portfolio demonstrating project management competency
- Foundation for choosing advanced specialization path

**The Hidden Curriculum Success:**
Students think they're "just building AI assistants" but they've actually mastered the foundational project management and development skills they'll use throughout their careers. The GitHub workflow and agile practices become second nature because they were learned as "the way you do real work" rather than abstract concepts.