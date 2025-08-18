# CSC-113 AI Fundamentals: Instructor Operations Manual

## "Failure is Just Exercise" - The GitHub-First Implementation Guide

### Purpose & Philosophy

This manual is your tactical playbook for running CSC-113 successfully. It contains everything you need to set up, manage, and troubleshoot a GitHub-first AI fundamentals course. When things break (and they will), this guide provides immediate, practical solutions.

**Core Operating Principle:** We teach professional workflows from Day 1. Students can experiment wildly with AI and code, but they do so within industry-standard practices. GitHub isn't an add-on skill—it's how we work.

---

## Pre-Semester Setup Checklist (T-minus 14 days)

### Week -2: Infrastructure Foundation

#### Day 1: GitHub Organization Setup

**Required Actions:**
```yaml
GitHub Organization Creation:
  □ Name format: "csc113-[semester]-[year]" (e.g., "csc113-spring-2025")
  □ Apply for GitHub Education benefits immediately
  □ Set organization visibility: Private initially
  □ Configure default permissions: Write access for members
  □ Enable features: Issues, Discussions, Projects, Wiki
  □ Create welcome repository with course overview
```

**Verification Steps:**
- Test student invitation process with dummy account
- Confirm education benefits are active
- Document organization URL for syllabus

#### Day 2: Template Repository Architecture

**Create Four Essential Templates:**

1. **student-portfolio-template**
   ```markdown
   Structure:
   ├── README.md (professional profile template)
   ├── projects/
   │   ├── ai-assistants/
   │   └── community-project/
   ├── reflections/
   └── resources/
   ```

2. **ai-assistant-template**
   ```markdown
   Structure:
   ├── README.md (assistant documentation)
   ├── prompts/
   ├── test-results/
   ├── iterations/
   └── .github/
       └── ISSUE_TEMPLATE/
   ```

3. **weekly-reflection-template**
   - Structured reflection prompts
   - Learning documentation format
   - Progress tracking sections

4. **peer-review-template**
   - Review checklist
   - Constructive feedback framework
   - Required elements verification

#### Day 3: Safety Rails Configuration

**Branch Protection Rules (Apply to ALL repos):**
```yaml
Main Branch Protection:
  □ Require pull request reviews before merging
  □ Dismiss stale PR approvals when new commits pushed
  □ Require branches to be up-to-date before merging
  □ Include administrators in restrictions
  □ Allow force pushes: NEVER
  □ Allow deletions: NEVER
```

**Automation Setup:**
```yaml
GitHub Actions:
  □ Auto-assign Issues to creators
  □ Welcome message for first-time contributors
  □ Stale Issue/PR notifications after 5 days
  □ Weekly activity summary generation
```

### Week -1: Academic Readiness

#### Day 1: AI Ecosystem Preparation

**Primary Tools Setup:**
```yaml
Gemini Flash Configuration:
  □ Test API access and rate limits
  □ Document quota: 15 RPM, 1M TPM, 1500 RPD
  □ Create instructor testing account
  □ Prepare rate limit management strategy

Kevin from IT Preparation:
  □ Create prompt template library
  □ Test handoff scenarios
  □ Document common failure modes
  □ Prepare backup AI service accounts
```

**Backup Systems:**
- Claude.ai account (free tier)
- ChatGPT account (free tier)
- Local Ollama installation (optional)

#### Day 2: External Stakeholder Engagement

**Community Partner Protocol:**
```yaml
Partner Recruitment:
  Target: 3-5 organizations minimum
  Types: Local businesses, nonprofits, municipal departments
  
  Requirements Communication:
  - 2-hour total time commitment
  - Week 6: Problem presentation (30 min)
  - Week 8: Solution review (90 min)
  - Simple feedback form completion
  
  Deliverables to Partners:
  □ Clear project timeline
  □ Student team assignments (Week 4)
  □ Presentation schedule (Week 8)
  □ Follow-up summary report
```

#### Day 3: Student Success Infrastructure

**Deploy Support Resources:**
```yaml
GitHub Pages Deployment:
  □ Host survival guide at: [org].github.io/survival-guide
  □ Create short URL redirect
  □ Test mobile responsiveness
  □ Verify all links functional
  □ Add analytics tracking

Communication Channels:
  □ Create course Discord/Slack
  □ Set up office hours calendar
  □ Establish emergency contact protocol
  □ Configure notification preferences
```

---

## Week-by-Week Operations Guide

### Week 1: "Hello, Scholars!" - Professional Foundations

#### Day 1: The GitHub Initiation

**Morning Preparation (30 minutes before class):**
```bash
□ Test projector/screen sharing
□ Open GitHub organization dashboard
□ Queue up live demo repository
□ Print backup instructions (power outage contingency)
□ Test guest WiFi access
```

**Class Opening Script:**
```markdown
"Hello, Scholars! Welcome to how professional developers work.
Before we explore AI, we're learning the collaboration system 
used by millions of professionals worldwide. This isn't extra—
this IS how modern work happens."
```

**Live Demonstration Checklist:**
1. Create repository in real-time
2. Create Issue: "Add personal introduction"
3. Create branch from Issue
4. Edit README directly in browser
5. Commit with descriptive message
6. Create Pull Request
7. Link PR to Issue
8. Show review process
9. Merge and celebrate

**Student Success Metrics (Day 1):**
- 100% GitHub account creation
- 90%+ organization invitation acceptance
- 80%+ first repository created
- 70%+ first Issue created

#### Daily Standup Ritual (Days 2-5)

**The 5-Minute Morning Ceremony:**
```python
for student in class_roster:
    print(f"{student.name}:")
    print(f"  Yesterday: {get_commits(student, hours=24)}")
    print(f"  Today: {get_current_issue(student)}")
    print(f"  Blockers: {check_help_requests(student)}")
```

**Your Intervention Decision Tree:**
```mermaid
Is student participating in standup?
├─ No → Private check-in after class
└─ Yes → Is progress visible on GitHub?
    ├─ No → Offer pairing session
    └─ Yes → Are they blocked?
        ├─ No → Recognition/encouragement
        └─ Yes → Immediate intervention
```

### Week 2: Assistant Development Deep Dive

#### Quality Assurance Framework

**Daily GitHub Health Check:**
```yaml
Morning Review (10 minutes):
  Repository Status:
    □ Active branches count
    □ Open PR queue length
    □ Unresolved Issues count
    □ Latest commit timestamps
  
  Student Engagement:
    □ Commit frequency analysis
    □ PR review participation
    □ Issue creation patterns
    □ Help request trends

Evening Actions (15 minutes):
  □ Approve ready PRs
  □ Provide feedback on incomplete work
  □ Clean up abandoned branches
  □ Update progress tracking
```

#### The "Everything is Broken" Protocol

**When Students Hit Crisis:**
```markdown
Step 1: Normalize the Experience
"This is exactly what professional development looks like.
You're not failing—you're iterating."

Step 2: Implement Recovery
1. Save any salvageable work (copy important text)
2. Delete problematic branch
3. Create fresh branch from main
4. Rebuild incrementally
5. Document lessons in retrospective

Step 3: Extract Learning
"What will you do differently next time?"
"What warning signs will you watch for?"
"How could you prevent this in the future?"
```

### Weeks 3-6: Differentiation & Specialization

#### Path Management System

**Track Coordination Framework:**
```yaml
Prompt Masters Track:
  Focus: Advanced prompt engineering
  Tools: Gemini, Claude, ChatGPT
  Deliverables: Sophisticated assistants via prompting
  
  Support Structure:
    □ Monday office hours (2-3 PM)
    □ Prompt pattern library access
    □ Peer review with other prompt engineers
    □ Weekly prompt challenge competitions

Code Builders Track:
  Focus: AI implementation with code
  Tools: Google Colab, Python, APIs
  Deliverables: Custom-coded AI solutions
  
  Support Structure:
    □ Wednesday office hours (2-3 PM)
    □ Code snippet repository access
    □ Debugging partnership assignments
    □ Weekly code review sessions
```

**Cross-Pollination Requirements:**
- Week 4: Mixed-track peer reviews
- Week 5: Collaborative feature development
- Week 6: Joint problem-solving session

#### Community Partner Project Management

**Week 4: The Matching Process**
```yaml
Team Formation Protocol:
  1. Students submit interest rankings (3 partners)
  2. Form teams of 3-4 with mixed tracks
  3. Assign primary and backup partners
  4. Schedule stakeholder meetings
  5. Create project repositories
```

**Week 5-6: Active Management**
```yaml
Weekly Check-ins:
  With Students:
    □ Daily standups include project updates
    □ Review project Issues and milestones
    □ Address scope creep immediately
    □ Support pivot decisions
  
  With Partners:
    □ Weekly email update
    □ Availability for questions
    □ Manage expectations
    □ Confirm presentation attendance
```

### Weeks 7-8: Capstone Excellence

#### Portfolio Assessment Protocol

**The 20-Minute Portfolio Review:**
```yaml
For Each Student:
  GitHub Profile Review (5 min):
    □ Professional README
    □ Pinned repositories
    □ Contribution graph activity
    □ Profile completeness
  
  Repository Deep Dive (10 min):
    □ Project documentation quality
    □ Commit message evolution
    □ Issue tracking sophistication
    □ Code/prompt iteration evidence
  
  Collaboration Assessment (5 min):
    □ PR review quality
    □ Issue discussions participation
    □ Team project contributions
    □ Professional communication
```

#### Presentation Day Operations

**The Logistics Checklist:**
```yaml
Week Before:
  □ Confirm partner attendance
  □ Send calendar invitations
  □ Test all presentation tech
  □ Prepare feedback forms
  □ Create presentation order

Day Of:
  Setup (30 min before):
    □ Test all student presentations load
    □ Verify internet connectivity
    □ Set up recording equipment
    □ Prepare backup laptop
    □ Welcome partners on arrival
  
  During Presentations:
    □ Strict 7-minute timer
    □ 3-minute Q&A facilitation
    □ Transition management
    □ Partner engagement monitoring
    □ Success documentation
```

---

## Crisis Management Playbook

### Technical Failure Recovery

#### Scenario: GitHub Outage

**Immediate Response:**
```yaml
Minute 1-5:
  □ Check status.github.com
  □ Announce calmly to class
  □ Switch to backup activity

Backup Activities:
  1. Prompt engineering workshop (paper-based)
  2. AI ethics discussion
  3. Portfolio planning session
  4. Peer algorithm reviews
  5. Industry video and discussion

Recovery:
  □ Document work done offline
  □ Prioritize critical submissions
  □ Extend deadlines appropriately
  □ Celebrate resilience
```

#### Scenario: AI Service Interruption

**Service Degradation Protocol:**
```yaml
Primary (Gemini) Fails:
  → Switch to Claude (backup 1)
  → Switch to ChatGPT (backup 2)  
  → Use local Ollama (emergency)
  → Paper-based planning (last resort)

Teaching Moment:
  "This is why professionals have multiple tools.
   Let's practice prompt adaptation across platforms."
```

### Academic Resistance Management

#### Challenge: "This Isn't Computer Science"

**Your Evidence-Based Response:**
```markdown
1. Industry Alignment
   "Google, Microsoft, and Meta all use this exact workflow."

2. Skill Development
   "You're learning version control, project management, 
    and collaboration—core CS competencies."

3. Portfolio Evidence
   "Your GitHub profile IS your professional portfolio."

4. Outcome Data
   "Previous students report these skills crucial in job interviews."
```

#### Challenge: Process Resistance

**Common Objections & Responses:**

| Objection | Response |
|-----------|----------|
| "Too much overhead" | "Overhead becomes essential at scale" |
| "Can't I just email files?" | "GitHub IS professional file sharing" |
| "I work better alone" | "Industry requires collaboration skills" |
| "This is too complicated" | "Complexity now prevents disasters later" |

---

## Assessment Operations

### The GitHub Grading Workflow

**Weekly Assessment Routine:**
```python
def assess_student_week(student_username):
    metrics = {
        'commits': count_commits(student_username, days=7),
        'issues_completed': count_closed_issues(student_username),
        'pr_reviews': count_reviews_given(student_username),
        'documentation': assess_readme_quality(student_username),
        'collaboration': measure_discussion_participation(student_username)
    }
    
    return calculate_week_score(metrics)
```

**Evidence Collection Protocol:**
```yaml
For Each Student:
  □ Screenshot exceptional work
  □ Document learning progression
  □ Note collaboration highlights
  □ Track skill development
  □ Record professional growth
```

### Peer Review Quality Management

**Review Quality Rubric:**
```markdown
Excellent Review (A):
- Specific line-by-line feedback
- Suggests improvements
- Asks clarifying questions
- Recognizes strengths
- Professional tone

Needs Improvement (C):
- Generic "looks good"
- No specific feedback
- Missed obvious issues
- Unclear comments
- Rushed appearance
```

---

## Weekly Instructor Routine

### Sunday: Strategic Planning (30 min)
```yaml
□ Review coming week's objectives
□ Check student progress trajectories
□ Identify at-risk students
□ Prepare intervention strategies
□ Update material based on class needs
```

### Wednesday: Mid-Week Calibration (20 min)
```yaml
□ Progress check against timeline
□ GitHub activity pulse check
□ Partner project status review
□ Adjustment planning if needed
□ Student support need identification
```

### Friday: Weekly Closure (25 min)
```yaml
□ Complete weekly assessments
□ Synthesize student reflections
□ Document successful patterns
□ Plan weekend monitoring level
□ Prepare next week's launches
```

---

## Quick Reference Troubleshooting

### The Top 10 Student Issues

1. **"I can't find my branch"**
   - Solution: GitHub web → Branches tab → View all
   - If gone: Start fresh, it's just exercise

2. **"My PR won't merge"**
   - Check: Conflicts? Behind main? Reviews pending?
   - Solution: Update branch or start fresh

3. **"Kevin isn't responding properly"**
   - Verify: Proper handoff format used?
   - Try: Different phrasing or different AI

4. **"I lost all my work"**
   - Check: GitHub commit history
   - Reality: If committed, it's never truly lost

5. **"This is too confusing"**
   - Response: "Confusion means you're learning"
   - Action: Pair with successful peer

6. **"My assistant doesn't work"**
   - Review: Iteration history in Issues
   - Solution: Start simpler, build up

7. **"I can't write good commit messages"**
   - Template: "Type: What and why"
   - Example: "Feature: Add greeting for better UX"

8. **"Nobody reviewed my PR"**
   - Check: Did they request reviews?
   - Solution: Assign specific reviewers

9. **"The AI gave me wrong code"**
   - Learning: "AIs assist, they don't replace thinking"
   - Process: Test, iterate, document

10. **"I'm behind everyone else"**
    - Truth: "Everyone progresses differently"
    - Focus: "Your growth, not others' speed"

---

## Success Metrics Dashboard

### Daily Health Indicators
- GitHub commit activity (target: 80% active daily)
- Issue creation rate (target: 2-3 per student/week)
- PR completion rate (target: 90% within 48 hours)
- Help request resolution time (target: <24 hours)
- Standup participation (target: 100%)

### Weekly Progress Markers
- Feature completion rate (target: 80%)
- Portfolio growth (commits, documentation)
- Peer review quality improvement
- Professional communication usage
- AI tool literacy demonstration

### Semester Success Criteria
- 100% students with professional GitHub portfolio
- 95% community partner satisfaction
- 90% student competency demonstration
- 85% student course satisfaction
- 80% students report career readiness improvement

---

## Emergency Resources

### Support Escalation Chain
1. Kevin from IT (AI assistant)
2. Peer support (classmate pairing)
3. Instructor intervention (office hours)
4. Campus resources (IT, counseling, success center)
5. External support (GitHub Education, community)

### Critical Contacts
```yaml
Technical:
  - Campus IT: [number]
  - GitHub Education: education.github.com/contact
  - LMS Support: [number]

Academic:
  - Department Chair: [email]
  - Academic Affairs: [number]
  - Student Success: [number]

Emergency:
  - Campus Security: [number]
  - Counseling Services: [number]
  - Title IX Coordinator: [number]
```

---

## End-of-Semester Procedures

### Portfolio Preservation
```yaml
Student Deliverables:
  □ Export repository as archive
  □ Generate GitHub contribution certificate
  □ Create LinkedIn summary
  □ Document learning journey
  □ Peer recommendation collection

Instructor Archives:
  □ Screenshot exceptional work
  □ Document success stories
  □ Save partner feedback
  □ Create highlight reel
  □ Generate grade reports
```

### Continuous Improvement
```yaml
Collect Feedback:
  □ Student course evaluations
  □ Partner experience surveys
  □ Peer instructor observations
  □ Self-reflection documentation
  □ Technology tool assessment

Iterate for Next Semester:
  □ Update templates based on pain points
  □ Refine timing based on actual progress
  □ Enhance materials from student feedback
  □ Adjust partner engagement model
  □ Optimize assessment workflow
```

---

## Remember Your Role

**You are not expected to be:**
- A Git expert
- An AI researcher
- A software engineer
- A debugging wizard

**You ARE expected to be:**
- A learning facilitator
- A process coach
- An encouragement source
- A professional model

**Your Mantra:** "Failure is just exercise. Delete the branch and try again."

**Your Success:** Students leave with professional portfolios, collaboration skills, and the confidence that they can learn any new technology by following good processes.

---

*This manual is a living document. Update it each semester with lessons learned. Your future self will thank you.*

