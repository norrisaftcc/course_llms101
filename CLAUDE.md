# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **course_llms101** repository, containing all materials for the "Large Language Models in Enterprise Applications" course. The course is designed for second-year students developing their first enterprise applications and focuses on integrating LLMs in business contexts through project-based learning.

## Repository Structure

The repository is organized into 8 session directories:
- `session-1-introduction/` - Introduction to Large Language Models
- `session-2-provider-landscape/` - LLM Provider Landscape  
- `session-3-one-on-one/` - Effective One-on-One LLM Interaction
- `session-4-api-integration/` - API Integration Fundamentals
- `session-5-prompt-engineering/` - Prompt Engineering Foundations
- `session-6-advanced-prompting/` - Advanced Prompt Engineering
- `session-7-admin-automation/` - LLMs for Administrative Automation
- `session-8-advanced-tools/` - Advanced Integration Tools

Each session directory contains:
- `slides/` - Presentation materials
- `exercises/` - In-class activities
- `assignment/` - Weekly assignments with instructions
- `resources/` - Additional materials

Additional directories:
- `example-projects/` - Complete reference implementations
- `resources/` - Cross-session materials and guides

## Common Commands

### Git Operations
```bash
# Clone the repository
git clone https://github.com/your-university/llm-enterprise-course.git

# Submit assignments (on personal branch)
git checkout -b firstname-lastname
git add .
git commit -m "Submission for Assignment X"
git push origin firstname-lastname
```

## Development Guidelines

1. This is primarily a course repository containing educational materials rather than executable code
2. Focus on organizing course content, assignments, and resources clearly
3. When adding new materials, follow the existing directory structure pattern
4. Maintain consistency in file naming and organization across sessions

## Course Content Status

### Completed Materials
1. **Session 1: Introduction to LLMs**
   - Session outline with timing
   - Hands-on workshop exercises
   - Assignment: Identifying LLM opportunities
   - Quick reference guide
   - LLM readiness checklist

2. **Session 2: LLM Provider Landscape** ✅
   - Session outline with timing
   - Hands-on provider comparison exercises (`session2_exercises.py`)
   - Provider evaluation matrix template
   - Quick reference handout with pricing
   - Assignment: Provider comparison tool

3. **Instructor Materials**
   - INSTRUCTOR_BEST_PRACTICES.md - Comprehensive guide on course design
   - SESSION_TEMPLATE.md - Standardized template for all sessions

### Delivery Formats
- **90-minute MVP Session**: Complete AI blog application using Streamlit + Supabase
- **60-minute Lunch & Learn**: Condensed overview with interactive demos
- **8-week Full Course**: Comprehensive curriculum (Sessions 1-2 completed)

## API Credits and Security

- Each student receives approximately $15 worth of API credits
- API key management instructions are in `resources/api-keys-guide/`
- Security best practices are covered in `session-4-api-integration/security-guide/`

## Next Steps

1. Develop Session 3: Effective One-on-One LLM Interaction
2. Create Session 4: API Integration Fundamentals  
3. Build more example projects
4. Set up technical infrastructure for demos