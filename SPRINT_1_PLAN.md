# Sprint 1: Ship Weeks 1-2 MVP

## What We Can Ship NOW (2-week sprint)

### Week 1: "Your First Local LLM" 
**Ship a working lab where students actually run AI locally**

Minimal Viable Content:
1. **Setup Guide** (2 hours to write)
   - Ollama installation for Mac/Windows/Linux
   - Pull llama2 or mistral
   - "Hello World" test
   
2. **Lab Exercise** (3 hours to build)
   - Compare local vs ChatGPT responses
   - Measure response times
   - Check what data stays local
   
3. **Assignment** (1 hour to create)
   - "Run 5 prompts locally and 5 on ChatGPT"
   - "Document the differences you notice"
   - "What data did you share with each?"

### Week 2: "Audit Your AI Data Trail"
**Ship a working privacy audit tool**

Minimal Viable Content:
1. **Python Script** (4 hours to build)
   ```python
   # privacy_audit.py
   - Check what APIs are installed
   - Show API key exposure risks  
   - Demonstrate prompt logging
   - Create data flow diagram
   ```

2. **ToS Analysis Exercise** (2 hours to create)
   - Template for reviewing ToS
   - ChatGPT vs Claude vs Local comparison
   - "Find the data retention clause" exercise

3. **Assignment** (1 hour to create)
   - Audit one AI service you use
   - Document what they keep
   - Propose safer alternatives

## Sprint 1 Deliverables (Total: ~16 hours work)

### Must Have (Ship or Die)
- [ ] Ollama setup guide that actually works
- [ ] Week 1 lab instructions 
- [ ] Week 2 privacy audit script
- [ ] Basic assignments for both weeks

### Nice to Have (If Time)
- [ ] Video of Ollama setup
- [ ] Prettier data flow visualizations
- [ ] More model options documented

### Won't Do This Sprint
- Weeks 3-8 (next sprints)
- Complex multi-provider abstractions
- Docker containers
- Auto-grading

## Definition of Done
- Student can run an LLM locally in Week 1
- Student can audit AI data practices in Week 2
- Both weeks have clear learning outcomes
- Materials tested on at least Mac + Windows

## Sprint Velocity Assumptions
- 1 developer
- 16 hours of actual work
- Ship Friday, whatever's done

## Next Sprint Preview (Sprint 2)
- Week 3: Multi-provider chatbot
- Week 4: Vendor comparison framework
- OR: Polish Weeks 1-2 based on feedback

## The Scrum Reality
We're shipping 25% of the course because:
1. Something > Nothing
2. Real feedback > Perfect plans  
3. Students can start learning NOW
4. We'll iterate based on what actually breaks

## Quick Start Commands
```bash
# Start Sprint 1
gh issue create --title "[SPRINT 1] Week 1 - Local LLM Lab" --label "high-priority"
gh issue create --title "[SPRINT 1] Week 2 - Privacy Audit Tool" --label "high-priority"

# Ship Sprint 1
git tag v0.1.0-sprint1
git push origin v0.1.0-sprint1
```