# course_llms101
LLMS 101, short form class proposed.

# README

# LLM in Enterprise Applications

## Course Overview

This repository contains all materials for the "Large Language Models in Enterprise Applications" course, designed for second-year students developing their first enterprise applications. The course explores how to effectively integrate and leverage LLMs in business contexts through a hands-on, project-based approach.

## Learning Objectives

By the end of this course, students will be able to:

- Understand the capabilities and limitations of modern LLM technology
- Evaluate different LLM providers for specific enterprise use cases
- Design effective prompts for consistent and useful outputs
- Safely integrate LLM APIs into applications
- Implement LLM-powered solutions for administrative tasks
- Use advanced tools to create complex LLM workflows

## Repository Structure

This repository is organized into 8 session directories, each containing:

- **slides/**: Presentation materials for the lecture
- **exercises/**: In-class activities and workshops
- **assignment/**: Weekly assignments with instructions and starter files
- **resources/**: Additional materials and references

Additional directories include:

- **example-projects/**: Complete reference implementations
- **resources/**: Cross-session materials and guides

## Getting Started

### Prerequisites

- Basic programming knowledge (JavaScript/Python)
- Familiarity with RESTful APIs
- GitHub account
- Text editor or IDE

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-university/llm-enterprise-course.git
   ```

2. Follow the instructions in `SETUP.md` to:
   - Create accounts with LLM providers
   - Set up API keys
   - Install required dependencies

3. Review the first session materials before class

## Course Schedule

### Session 1: Introduction to Large Language Models
Understanding the fundamentals of LLM technology and exploring potential enterprise applications.

### Session 2: LLM Provider Landscape
Comparing offerings from major providers including OpenAI, Anthropic, Google, Meta, and others.

### Session 3: Effective One-on-One LLM Interaction
Developing strategies for productive human-LLM collaboration and workflow design.

### Session 4: API Integration Fundamentals
Learning to safely integrate LLM capabilities via APIs with proper security practices.

### Session 5: Prompt Engineering Foundations
Creating effective prompts that yield consistent, useful outputs for business contexts.

### Session 6: Advanced Prompt Engineering
Applying sophisticated prompting techniques to solve complex enterprise challenges.

### Session 7: LLMs for Administrative Automation
Implementing LLM-powered solutions for common business processes and workflows.

### Session 8: Advanced Integration Tools & Final Projects
Exploring n8n and Voiceflow for advanced integration scenarios and presenting final projects.

## Assignments

Weekly assignments (40% of final grade) will be released at the end of each session and are due before the next session. Submit assignments by pushing to your personal branch:

```
git checkout -b firstname-lastname
git add .
git commit -m "Submission for Assignment X"
git push origin firstname-lastname
```

## Final Project (40% of final grade)

The final project requires you to design and implement an LLM-integrated enterprise application. Details and requirements can be found in the `session-8-advanced-tools/final-project/` directory.

Projects will be presented during the final session, with both working demonstrations and code reviews.

## Resources

### API Credits
Each student will receive approximately $15 worth of API credits for use throughout the course. Instructions for accessing these credits are in the `resources/api-keys-guide/` directory.

### Recommended Reading
- "Building LLM-Powered Applications" by various authors
- "Prompt Engineering for Enterprise" by various authors
- Additional readings listed in `resources/reading-list/`

## Troubleshooting

If you encounter issues with the course materials or assignments, please:

1. Check the `resources/troubleshooting/` directory for common solutions
2. Open an issue on this repository with a detailed description
3. Contact the course instructor during office hours

## License

This course material is licensed under [appropriate license] - see the LICENSE file for details.

---

Developed by [Your Institution] © 2025


# Directory Structure
example repository structure we may follow.


llm-enterprise-course/
│
├── README.md                      # Course overview and repository instructions
├── SETUP.md                       # Environment setup instructions
├── LICENSE                        # Repository license
│
├── session-1-introduction/        # Introduction to Large Language Models
│   ├── slides/                    # Presentation materials
│   ├── exercises/                 # In-class activities
│   ├── assignment/                # First assignment details and starter files
│   └── resources/                 # Additional reading and links
│
├── session-2-provider-landscape/  # LLM Provider Landscape
│   ├── slides/
│   ├── exercises/                 # Model comparison exercises
│   ├── assignment/                # Provider evaluation assignment
│   └── resources/                 # Provider documentation links
│
├── session-3-one-on-one/          # Effective One-on-One LLM Interaction
│   ├── slides/
│   ├── exercises/                 # Conversation exercises
│   ├── assignment/                # Workflow process document assignment
│   └── templates/                 # Workflow templates
│
├── session-4-api-integration/     # API Integration Fundamentals
│   ├── slides/
│   ├── code/                      # Example code for API calls
│   ├── exercises/                 # API practice activities
│   ├── assignment/                # Simple application assignment
│   └── security-guide/            # API security best practices
│
├── session-5-prompt-engineering/  # Prompt Engineering Foundations
│   ├── slides/
│   ├── exercises/                 # Prompt practice activities
│   ├── assignment/                # Prompt development assignment
│   └── examples/                  # Example prompts by category
│
├── session-6-advanced-prompting/  # Advanced Prompt Engineering
│   ├── slides/
│   ├── exercises/                 # Complex prompting scenarios
│   ├── assignment/                # Advanced strategy assignment
│   └── case-studies/              # Real-world prompting examples
│
├── session-7-admin-automation/    # LLMs for Administrative Automation
│   ├── slides/
│   ├── exercises/                 # Automation examples
│   ├── assignment/                # Admin solution assignment
│   └── templates/                 # Templates for common admin tasks
│
├── session-8-advanced-tools/      # Advanced Integration Tools
│   ├── slides/
│   ├── n8n-examples/              # n8n workflow examples
│   ├── voiceflow-examples/        # Voiceflow conversation designs
│   └── final-project/             # Final project requirements and rubric
│
├── example-projects/              # Complete example projects
│   ├── customer-service-bot/
│   ├── content-generator/
│   └── data-extraction-tool/
│
└── resources/                     # Shared resources across sessions
    ├── api-keys-guide/            # How to obtain and manage API keys
    ├── cost-calculator/           # Spreadsheet for estimating API costs
    ├── reading-list/              # Recommended books and papers
    └── troubleshooting/           # Common issues and solutions
