# AI & Machine Learning in 2025: A Responsible Approach
## Course Syllabus - Emphasizing Data Sovereignty, Privacy, and Portable Skills

### Course Philosophy
This course teaches AI/ML as a tool for empowerment, not dependency. Students will learn to leverage AI while maintaining control over their data, avoiding vendor lock-in, and understanding the ethical implications of their choices.

### Core Principles
1. **Data Sovereignty**: Your data belongs to you
2. **Vendor Independence**: Skills that transfer across platforms
3. **Privacy First**: Understanding what you're sharing and why
4. **Open Alternatives**: Always know the FOSS option
5. **Informed Consent**: Understanding the trade-offs

## Module 1: Foundations Without Handcuffs (Weeks 1-2)

### Week 1: Understanding AI/ML Landscape
- **History with a Critical Lens**
  - From academic research to corporate control
  - The open-source AI movement
  - Why "free as in freedom" matters for AI
  
- **How AI Actually Works**
  - Demystifying neural networks
  - Understanding training data (and who owns it)
  - The real cost of "free" AI services
  
- **Lab**: Run your first local LLM (Ollama/llama.cpp)
  - No cloud required
  - Understanding hardware requirements
  - Comparing local vs. cloud performance

### Week 2: The Data Economy
- **Your Data as Currency**
  - What happens to your prompts?
  - Training data and intellectual property
  - Terms of Service deep dive
  
- **Privacy-Preserving Techniques**
  - Anonymization strategies
  - Local-first architectures
  - Federated learning basics
  
- **Lab**: Build a privacy audit tool
  - Analyze what data apps are sending
  - Create data firewalls
  - Implement prompt sanitization

## Module 2: Practical AI Without Selling Your Soul (Weeks 3-4)

### Week 3: Vendor-Agnostic Skills
- **Prompt Engineering as Universal Skill**
  - Techniques that work everywhere
  - Understanding model differences
  - Avoiding platform-specific patterns
  
- **API Abstraction Layers**
  - Building switchable backends
  - LangChain/LlamaIndex patterns
  - Cost comparison frameworks
  
- **Lab**: Multi-provider chatbot
  - Support OpenAI, Anthropic, and local models
  - Implement provider switching
  - Build cost tracking

### Week 4: Open Source Alternatives
- **Local Model Ecosystem**
  - Hugging Face and model selection
  - Ollama, llama.cpp, and alternatives
  - GPU vs CPU considerations
  
- **Self-Hosted Solutions**
  - LocalAI setup
  - Privacy-preserving deployments
  - Building your own API endpoints
  
- **Lab**: Deploy your own AI stack
  - Set up local inference server
  - Implement caching and optimization
  - Create usage monitoring

## Module 3: Responsible Development (Weeks 5-6)

### Week 5: Data Ethics and Security
- **Responsible Data Handling**
  - PII detection and removal
  - Data retention policies
  - Right to deletion implementation
  
- **Security Considerations**
  - Prompt injection prevention
  - Output validation
  - API key management
  
- **Lab**: Build a privacy-first AI app
  - Implement data minimization
  - Add consent mechanisms
  - Create audit logs

### Week 6: Avoiding Lock-in Patterns
- **Portable Architectures**
  - Standard formats (ONNX, etc.)
  - Migration strategies
  - Backup and export tools
  
- **Cost Management**
  - Token optimization
  - Hybrid local/cloud strategies
  - Building kill switches
  
- **Lab**: Migration toolkit
  - Export from proprietary platforms
  - Convert between formats
  - Implement gradual migration

## Module 4: Real-World Applications (Weeks 7-8)

### Week 7: Building Sustainable AI Products
- **Business Models That Respect Users**
  - Alternatives to data harvesting
  - Transparent pricing
  - User-controlled features
  
- **Case Studies**
  - Successful privacy-first AI products
  - Failed vendor lock-in stories
  - Community-driven projects
  
- **Project**: Design a responsible AI product
  - Define data policies
  - Plan for vendor independence
  - Create user bill of rights

### Week 8: Future-Proofing Your Skills
- **Staying Current Without Dependence**
  - Following open research
  - Contributing to open source
  - Building learning networks
  
- **The Next Frontiers**
  - Decentralized AI
  - Homomorphic encryption for AI
  - Personal AI assistants
  
- **Final Project**: Complete AI solution
  - Must support 3+ providers
  - Include privacy controls
  - Demonstrate data portability

## Assessment Approach

### Projects (60%)
- All projects must demonstrate:
  - Multi-vendor support
  - Data privacy considerations
  - Export/migration capabilities
  - Clear documentation of trade-offs

### Critical Analysis (20%)
- Analyze terms of service
- Evaluate privacy policies
- Compare total cost of ownership
- Assess vendor lock-in risks

### Community Contribution (20%)
- Contribute to open-source AI projects
- Create educational content
- Help others avoid common pitfalls
- Share migration tools/scripts

## Required Resources

### Software (All Free/Open Source)
- Python with key libraries
- Ollama or similar local runner
- Git for version control
- Docker for deployments
- VS Code or preferred editor

### Hardware
- Minimum: 8GB RAM, any modern CPU
- Recommended: 16GB RAM, modest GPU
- Optional: Dedicated AI hardware

### Readings
- "The Cathedral and the Bazaar" (Eric Raymond)
- "Weapons of Math Destruction" (Cathy O'Neil)
- Selected papers on federated learning
- EFF's AI privacy guides
- FSF's stance on AI freedom

## Learning Outcomes

By course end, students will:
1. **Technical Skills**
   - Build AI applications using multiple providers
   - Deploy local and cloud-based models
   - Implement privacy-preserving techniques
   - Create vendor-agnostic architectures

2. **Critical Thinking**
   - Evaluate true costs of AI services
   - Identify lock-in patterns
   - Assess privacy implications
   - Make informed trade-offs

3. **Practical Wisdom**
   - Know when to use cloud vs. local
   - Understand data sovereignty issues
   - Build sustainable AI solutions
   - Contribute to open ecosystem

## Ethical Framework

This course operates under these principles:
- **Transparency**: Always know what's happening to your data
- **Choice**: Multiple options for every solution
- **Control**: User maintains ownership and decision rights
- **Education**: Understanding enables better decisions
- **Community**: Shared knowledge benefits everyone

## Instructor Notes

### Key Messages to Reinforce
1. "Free" services are paid with your data
2. Today's convenient choice can be tomorrow's prison
3. Open source isn't just idealistic—it's practical
4. Privacy and functionality aren't mutually exclusive
5. Your skills should outlive any company

### Common Misconceptions to Address
- "Local AI is too slow/hard" (Show modern solutions)
- "I have nothing to hide" (Explain systemic issues)
- "Open source is inferior" (Demonstrate parity)
- "It's too late to care about privacy" (Every step matters)
- "This is too technical for me" (Start where they are)

### Success Metrics
- Students successfully migrate projects between providers
- Students can articulate privacy trade-offs
- Students contribute to open-source projects
- Students help others make informed choices
- Students build habits of critical evaluation