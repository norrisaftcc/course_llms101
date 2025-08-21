# CLAUDE.md

Developer guidance for contributing to the **AI & Machine Learning in 2025** course - a privacy-first, vendor-independent approach to teaching AI/ML.

## What This Course Actually Is

This is NOT another "enterprise AI" course that teaches vendor lock-in. We're building a course that:
- **Respects data sovereignty** - Your prompts, your data, your choice
- **Teaches portable skills** - Work with ANY provider or run locally
- **Prioritizes privacy** - Understand what you're trading when you use "free" services
- **Embraces open source** - Ollama, llama.cpp, Hugging Face first
- **Treats students as adults** - Default API safety settings, critical thinking expected

## Current Project Status (Honest Assessment)

### ✅ What Actually Exists
- **Core Philosophy**: Defined in `SYLLABUS_2025.md` and `CONTENT_STANDARDS.md`
- **Session 1-2**: Basic materials from old enterprise-focused version (need refactoring)
- **MVP Session**: 90-minute workshop with Streamlit + Supabase
- **Some CSC113 materials**: In `csc113-ai-fundamentals/` (different course format)

### ❌ What's Empty/Needs Work
- **Sessions 3-8**: Directory structure exists but NO CONTENT
- **Local-first labs**: Need to build Ollama/llama.cpp exercises
- **Privacy tools**: Data audit tools, prompt sanitization not built
- **Multi-provider support**: Abstraction layers not implemented
- **Migration toolkit**: Vendor escape tools not created

## Repository Structure

```
course_llms101/
├── SYLLABUS_2025.md          # Our actual philosophy & approach
├── CONTENT_STANDARDS.md      # Pragmatic content approach
├── ISSUES_ROADMAP.md          # What we're building
├── session-*/                # 8 sessions (only 1-2 have content)
│   ├── slides/
│   ├── exercises/
│   ├── assignment/
│   └── resources/
├── mvp-90min-session/         # Quick workshop version
├── csc113-ai-fundamentals/   # Different course (some reusable)
└── resources/                 # Shared materials
```

## Development Setup

### Local LLM Environment
```bash
# Install Ollama (macOS/Linux)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama2
ollama pull mistral

# Test it works
ollama run llama2 "Hello world"

# For GPU acceleration (optional)
# Check compatibility at ollama.ai/docs/gpu
```

### Python Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install core dependencies
pip install langchain ollama openai anthropic
pip install streamlit pandas numpy
pip install python-dotenv requests
```

### Multi-Provider Setup
```bash
# Create .env for API keys (NEVER commit this)
cat > .env << 'EOF'
# Optional - only if testing cloud providers
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
# Local models need no keys!
EOF

# Test provider abstraction
python scripts/test_providers.py  # TODO: Create this
```

## Critical Development Patterns

### 1. Always Provide Local Alternative
```python
# BAD - Vendor lock-in
from openai import OpenAI
client = OpenAI()

# GOOD - Provider agnostic
from langchain.llms import Ollama, OpenAI
llm = Ollama(model="llama2") if LOCAL_MODE else OpenAI()
```

### 2. Privacy-First Design
```python
# BAD - Sends everything to cloud
response = cloud_llm.complete(user_input)

# GOOD - Sanitize first
sanitized = remove_pii(user_input)
response = llm.complete(sanitized)
```

### 3. Cost Transparency
```python
# Always track and display costs
tokens_used = count_tokens(prompt + response)
cost = calculate_cost(tokens_used, provider="openai")
print(f"This request cost: ${cost:.4f}")
```

## What We Need Contributors to Build

### High Priority (Blocking other work)
1. **Local LLM lab exercises** - Get students running Ollama day 1
2. **Privacy audit tool** - Show what data apps are leaking
3. **Multi-provider chatbot** - Same code, multiple backends
4. **Cost comparison matrix** - Real numbers, no BS

### Medium Priority
5. **Migration scripts** - Export from OpenAI/Claude/etc
6. **PII detection lab** - Find and redact sensitive data
7. **Prompt injection demos** - Security awareness
8. **Performance benchmarks** - Local vs cloud reality check

### Nice to Have
9. **Docker environments** - One-click setup
10. **Auto-grading** - For scalability
11. **Video tutorials** - For different learning styles

## Commit Standards

```bash
# Good commit messages
git commit -m "Add Ollama setup guide for Week 1 lab"
git commit -m "Fix privacy leak in provider abstraction"
git commit -m "Refactor Session 2 to include open-source options"

# Bad commit messages
git commit -m "updates"
git commit -m "fixed stuff"
git commit -m "WIP"
```

## Testing Your Contributions

### For Course Materials
- [ ] Works with local models (Ollama/llama.cpp)
- [ ] Includes cost analysis for cloud options
- [ ] Has privacy implications documented
- [ ] No vendor-specific patterns
- [ ] Treats students as competent adults

### For Code
- [ ] Runs without cloud API keys
- [ ] Has local fallback options
- [ ] Sanitizes user data appropriately
- [ ] Includes migration path
- [ ] Documents trade-offs honestly

## Common Pitfalls to Avoid

1. **Don't assume cloud access** - Many students can't/won't pay
2. **Don't hide complexity** - Show real costs and trade-offs
3. **Don't patronize** - Students are adults, skip the hand-holding
4. **Don't trust marketing** - Test everything, measure reality
5. **Don't create lock-in** - Every solution needs an exit strategy

## Where to Start

1. Read `SYLLABUS_2025.md` - Understand the philosophy
2. Check `ISSUES_ROADMAP.md` - Pick an issue to work on
3. Look at Sessions 1-2 - See what needs updating
4. Run local LLMs - Get familiar with Ollama
5. Break something - Then fix it and document

## Getting Help

- **Philosophy questions**: Reference SYLLABUS_2025.md
- **Technical issues**: Check if local models work first
- **Privacy concerns**: Default to MORE privacy, not less
- **Content standards**: See CONTENT_STANDARDS.md

## The Bottom Line

We're building a course that teaches REAL skills, not vendor propaganda. Every lab should work locally. Every tool should respect privacy. Every lesson should build vendor-independent competence.

If you're adding content that requires a specific cloud provider, you're doing it wrong. If you're hiding costs or trade-offs, you're doing it wrong. If you're treating students like children, you're doing it wrong.

Build tools you'd want to use. Teach skills that survive company bankruptcies. Respect user privacy like it's your own.