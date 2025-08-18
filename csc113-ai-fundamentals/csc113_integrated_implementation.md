# CSC-113 AI Fundamentals: Integrated Implementation Guide
## "Teaching Professional Habits While Allowing Creative Exploration"

### Pre-Semester Setup Checklist

#### GitHub Infrastructure (Week -2)
- [ ] Create GitHub organization: `csc113-[semester]-[year]`
- [ ] Enable education benefits and set organization to private
- [ ] Create template repositories:
  - `student-portfolio-template`
  - `sage-assistant-template`
  - `weekly-retrospective-template`
  - `peer-review-template`
- [ ] Configure branch protection on all repos (require PR reviews, no direct main commits)

#### AI Services Configuration (Week -1)
- [ ] Set up Gemini 2.5 Flash as primary service
- [ ] Configure cascade routing: Flash-Lite → Flash → Pro
- [ ] Establish backup services (Claude, ChatGPT, local Ollama)
- [ ] Create AI persona templates:
  - **Kevin from IT**: Helpful, non-judgmental coding assistant
  - **Friend Computer**: Structured, process-oriented guide
  - **AdminBot**: Professional communication assistant
  - **IdeaBot**: Creative brainstorming partner
  - **ThinkerBot**: Technical analysis and architecture

#### Community Partnerships
- [ ] Recruit 3-5 local businesses/nonprofits as project partners
- [ ] Schedule Week 6 guest speaker sessions
- [ ] Prepare partnership agreements and project scoping templates

### Week-by-Week Implementation

#### Week 1: "Hello, Scholars!" - GitHub Initiation
**Day 1: The Foundation Ceremony**
```
Opening Script: "Before we write a single line of code, you're learning 
how every tech company on Earth actually works. This isn't homework - 
this is literally how I'd submit code at Google."

Live Demo Sequence:
1. Create repo: "my-sage-assistant"
2. Create Issue: "Feature: Administrative Assistant"
3. Create branch: "1-admin-assistant"
4. Edit README in browser (NO COMMAND LINE YET)
5. Commit with meaningful message
6. Open PR linking to issue
7. Merge and celebrate
```

**Days 2-5: Daily Standup Ritual**
- Every class starts with 30-second student updates
- Monitor GitHub activity via organization dashboard
- Intervention when students stuck on same issue 3+ days

#### Week 2: SAGE Assistant Development
**The AI Collaboration Bootcamp**
- Students build their first AI assistant using approved tool stack
- Introduce prompt engineering fundamentals
- Implement rate limit management strategies
- Document all AI interactions in GitHub

**Success Metrics:**
- 100% have working AI assistant
- 80% demonstrate prompt iteration
- 60% show evidence of critical evaluation
- Rate limit education: "Welcome to real development constraints!"

#### Weeks 3-6: Specialization Tracks

**Prompt Masters Track:**
- Focus: Natural language AI orchestration
- Tools: Google AI Studio, advanced prompt techniques
- Projects: Business workflow automation, content generation
- Portfolio: Custom GPT configurations, prompt libraries

**Code Builders Track:**
- Focus: Technical implementation with AI assistance
- Tools: GitHub Codespaces, Google Colab, local models
- Projects: Full-stack applications, API integrations
- Portfolio: Deployed applications, technical documentation

**Universal Requirements:**
- All work tracked in GitHub Issues and PRs
- Weekly retrospectives documenting learning
- Peer reviews across tracks for knowledge sharing
- Professional communication standards maintained

#### Weeks 7-8: Community Integration & Capstone

**Real-World Project Implementation:**
- Mixed-track teams assigned to community partners
- Authentic constraints and stakeholder feedback
- Public presentation of solutions
- Portfolio-ready case studies

### Crisis Management Protocols

#### Rate Limit Apocalypse
1. **Immediate**: Switch all students to Flash-Lite
2. **Short-term**: Implement aggressive response caching
3. **Medium-term**: Distribute across multiple accounts
4. **Teaching moment**: "This is why we optimize for cost in production"

#### GitHub Service Interruption
1. Check status.github.com
2. Switch to paper prototyping/planning
3. Continue with offline documentation
4. Resume when service returns
5. War story for future classes

#### Student Breakdown Response
1. "Let's take a breath"
2. "Show me where you're stuck"
3. Delete broken branch, start fresh
4. "Failure is just exercise"
5. Document learning in retrospective

### Assessment Implementation

#### GitHub Portfolio Evaluation Process
```python
# Automated metrics collection
portfolio_score = (
    commit_frequency * 0.2 +
    issue_documentation_quality * 0.25 +
    pr_review_participation * 0.25 +
    ai_collaboration_evidence * 0.3
)
```

#### Four-Category Rubric Application
1. **AI Partnership Quality (25%)**
   - Evidence: Prompt iteration in commit messages
   - Progression: Generic → Specific → Sophisticated
   - Red flags: Copy-paste without evaluation

2. **Problem-Solving Process (25%)**
   - Evidence: Issue descriptions and resolution documentation
   - Quality: Clear problem definition → systematic approach → reflection
   - Red flags: Jumping to solutions, no testing evidence

3. **Professional Communication (25%)**
   - Evidence: README quality, PR descriptions, peer reviews
   - Standards: Clear, actionable, audience-appropriate
   - Red flags: Incomprehensible documentation, unconstructive feedback

4. **Critical Thinking & Ethics (25%)**
   - Evidence: AI output evaluation comments, ethical considerations
   - Depth: Questioning outputs, identifying limitations, independent judgment
   - Red flags: Uncritical acceptance, no bias consideration

### Daily Operations Playbook

#### Morning Routine (15 minutes)
- [ ] Check GitHub notification feed
- [ ] Review overnight commit activity
- [ ] Scan for blocked students or new issues
- [ ] Prepare daily standup notes

#### During Class
- **First 5 min**: Standup ritual
- **Next 15 min**: Concept demonstration or problem-solving
- **Remaining time**: Student work with active circulation
- **Last 5 min**: Tomorrow's preview and commit reminder

#### Evening Routine (10 minutes)
- [ ] Review and approve pending PRs
- [ ] Leave specific feedback on incomplete work
- [ ] Update student progress tracking
- [ ] Plan tomorrow's interventions

### Resource Optimization

#### AI Cost Management
```python
# Token budget optimization
def route_request(task_complexity, student_budget):
    if task_complexity == "simple":
        return "flash-lite"  # $0.10/1M tokens
    elif task_complexity == "moderate":
        return "flash"       # $0.30/1M tokens
    elif task_complexity == "complex" and budget_allows:
        return "pro"         # $1.25/1M tokens
    else:
        return "local_model"  # Free but slower
```

#### GitHub Education Benefits
- Unlimited private repositories
- GitHub Codespaces (60-90 free hours/month)
- GitHub Copilot access for students
- Actions minutes for automation

### Success Metrics & Validation

#### Weekly Indicators
- GitHub commit activity and quality progression
- Issue/PR completion rates and documentation improvement
- Peer review participation and helpfulness scores
- AI collaboration sophistication evidence

#### Semester Outcomes
- 100% professional GitHub portfolios
- Successful community partner project delivery
- Demonstrated AI collaboration competency
- Industry-ready professional workflow skills

#### Long-term Validation
- Graduate employment and advancement rates
- Employer feedback on AI collaboration skills
- Alumni success in advanced coursework
- Adoption by other institutions

### Continuous Improvement Framework

#### Student Feedback Integration
- Weekly retrospective synthesis
- Mid-semester course corrections
- Final portfolio self-assessment
- Alumni follow-up surveys

#### Instructor Development
- Faculty collaboration and knowledge sharing
- Industry partnership feedback integration
- Technology evolution adaptation
- Pedagogical research contribution

### Emergency Protocols

#### When Everything Breaks
**The Panic Button Protocol:**
1. Announce: "Today we're doing AI Ethics Discussion"
2. Use downtime to fix infrastructure
3. Turn crisis into learning opportunity
4. Document for future prevention

#### Budget Exhaustion
1. Flash-Lite only mode
2. Disable thinking budgets
3. Implement peer response sharing
4. Switch to local models
5. Continue learning objectives

### Implementation Timeline

#### Month -2: Foundation Setup
- GitHub organization and templates
- AI service configuration and testing
- Community partner recruitment
- Instructor training and preparation

#### Month -1: Final Preparations
- Student orientation materials
- Crisis management protocol testing
- Assessment rubric calibration
- Technology backup verification

#### Semester Execution
- Week 1: Launch and foundation building
- Weeks 2-6: Progressive skill development
- Weeks 7-8: Real-world application
- Post-semester: Assessment and iteration

---

## Key Success Factors

1. **Start with Process, Not Tools**: GitHub workflow mastery enables everything else
2. **Embrace Failure as Exercise**: Create safe spaces for iteration and learning
3. **Maintain Professional Standards**: Industry-relevant practices from day one
4. **Balance Support and Independence**: Scaffold appropriately, remove gradually
5. **Document Everything**: GitHub provides automatic portfolio generation
6. **Community Integration**: Real stakeholders create authentic motivation
7. **Cost Consciousness**: Teach resource optimization as professional skill

*"We're not teaching them to code. We're teaching them to learn. The AI stuff is just the McGuffin. The real treasure was the GitHub portfolios we made along the way."*