# Meeting Notes - Course Strategy Pivot

## Date: [Today's Date]
## Attendees: Development Team + Management

### Strategic Direction from Management

**New Directive**: Create an open source (MIT License) version of the course as a free trial
- 90-minute in-person session format
- Focus on getting people the basics quickly
- Serve as entry point to full paid course

### MVP Approach - Agile Development Strategy

**Core Principle**: Build vertical slice first, iterate based on feedback

#### What This Means:
1. **Minimal Viable Product (MVP)** - Not minimal effort, but minimal scope with maximum learning value
2. **Vertical Slice** - Complete experience from start to finish, just narrower in scope
3. **Iterative Development** - Launch fast, learn faster, improve continuously

### Scope Adjustment for 90-Minute Session

#### Original 8-Session Course → 90-Minute Experience

**From**: Comprehensive 16-hour journey  
**To**: High-impact 90-minute introduction

#### New Learning Objectives:
1. Understand what LLMs can do for business (10 min)
2. Experience hands-on LLM interaction (20 min)
3. Build your first AI-powered application (45 min)
4. Identify immediate opportunities (10 min)
5. Q&A and next steps (5 min)

### Technical Stack Decision

**Leverage existing open-source foundations:**

#### Frontend: Streamlit
- Rapid prototyping
- No frontend expertise required
- Python-based (familiar to many)
- Built-in components for AI apps

#### Backend: Supabase
- PostgreSQL made simple
- Built-in auth and real-time features
- REST APIs out of the box
- Generous free tier

#### LLM Integration: OpenAI/Claude APIs
- Direct API calls (no complex orchestration)
- Simple prompt templates
- Basic error handling

### The "Build in an Hour" Component

**Live Coding Demo**: Create a Simple AI-Powered Blog

**What participants will build:**
1. User authentication (Supabase)
2. Create/Read/Update/Delete posts (CRUD)
3. AI-powered content generation for posts
4. AI-powered comment moderation
5. Simple analytics dashboard

**Why this works:**
- Immediately practical
- Covers full stack
- Shows LLM integration
- Takes ~45 minutes with guidance
- Extensible for their own projects

### Resource Constraints & Opportunities

#### Current Resources:
- Our own staff as instructors (paid)
- No external contractors yet
- Limited budget for initial rollout

#### Future Resources:
- Student volunteers as teaching assistants
- Community contributors for open-source materials
- Potential sponsorships from API providers

### Implementation Timeline

#### Week 1: Content Adaptation
- Condense Session 1 into 20-minute intro
- Create Streamlit + Supabase tutorial
- Design the blog building exercise
- Prepare setup instructions

#### Week 2: Technical Preparation
- Build reference implementation
- Create troubleshooting guide
- Test on multiple machines
- Record backup video

#### Week 3: Pilot Sessions
- Run 2-3 test sessions with internal team
- Document common issues
- Refine timing
- Gather feedback

#### Week 4: Public Launch
- Announce free sessions
- Open registration
- Run first public session
- Iterate based on feedback

### Success Metrics for MVP

1. **Participation**: 20+ attendees per session
2. **Completion**: 80% successfully build the demo app
3. **Conversion**: 10% sign up for full course
4. **Satisfaction**: 4.5+ rating out of 5
5. **Referral**: 30% bring a colleague to next session

### Marketing Strategy for Free Trial

**Positioning**: "From Zero to AI App in 90 Minutes"

**Target Audiences**:
1. Technical managers wanting to understand LLMs
2. Developers new to AI integration
3. Business analysts exploring automation
4. Entrepreneurs seeking rapid prototyping skills

**Distribution Channels**:
- Local tech meetups
- LinkedIn posts
- Company tech talks
- University partnerships

### Open Source Strategy

#### What We'll Open Source:
1. Session materials (slides, exercises)
2. Code templates and examples
3. Setup guides and documentation
4. Video recordings of sessions

#### What Remains Proprietary:
1. Advanced course content
2. Enterprise case studies
3. One-on-one mentoring
4. Certification program

### Risk Mitigation

**Technical Risks**:
- WiFi issues → Provide mobile hotspots
- API key problems → Have spare keys ready
- Installation issues → Provide cloud workspace backup
- Time overruns → Clear stopping points

**Business Risks**:
- Low attendance → Partner with local groups
- Poor conversion → Refine value proposition
- Competitor copying → Move fast, build community

### Next Steps

1. **Immediate Actions**:
   - Create GitHub repo with MIT license
   - Adapt Session 1 content for 90 minutes
   - Build Streamlit + Supabase template
   - Design registration page

2. **This Week**:
   - Assign roles and responsibilities
   - Set up development environment
   - Create project board for tracking
   - Schedule first internal pilot

3. **This Month**:
   - Launch registration for free sessions
   - Run 4-5 pilot sessions
   - Gather and analyze feedback
   - Plan full course based on insights

### Budget Implications

**Cost Reduction**:
- No venue costs (use company space)
- No external instructors initially
- Leverage free API credits
- Use open-source tools throughout

**Revenue Opportunity**:
- Upsell to full course
- Corporate training contracts
- Sponsorship from tool providers
- Consulting spin-offs

### Team Assignments

**Content Team**: Adapt materials for 90-minute format
**Technical Team**: Build demo app and templates
**Marketing Team**: Create landing page and promotion strategy
**Operations Team**: Handle registration and logistics

### Definition of Success

**For Participants**:
"I built my first AI app and see exactly how to use this at work"

**For Us**:
"We validated market demand and built a pipeline for the full course"

**For the Community**:
"Quality AI education is accessible to everyone"

---

## Action Items

- [ ] Create open-source repository with MIT license
- [ ] Design 90-minute session flow
- [ ] Build Streamlit + Supabase blog template
- [ ] Create registration system
- [ ] Schedule first pilot session
- [ ] Draft marketing materials
- [ ] Set up feedback collection system

## Next Meeting: [One Week From Today]
Focus: Review progress on MVP development

---

*Note: This represents a strategic pivot from comprehensive training to accessible entry point. The full course remains our north star, but this MVP approach lets us validate assumptions and build community faster.*