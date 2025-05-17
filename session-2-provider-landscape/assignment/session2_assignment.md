# Session 2 Assignment: Provider Comparison Tool

## Objective
Build a simple web application that compares LLM providers for your specific use case.

## Requirements

### Part 1: Basic Comparison (Required)
Create a Streamlit app that:
1. Accepts a user prompt
2. Sends the prompt to at least 2 different LLM providers
3. Displays the responses side-by-side
4. Shows response time and estimated cost for each

### Part 2: Advanced Features (Choose 2)
- Add a cost calculator for monthly usage estimates
- Implement response quality scoring (subjective 1-5 scale)
- Create a provider recommendation based on criteria
- Add prompt templates for common use cases
- Export comparison results to CSV/JSON

### Part 3: Documentation
Write a brief report (1-2 pages) covering:
1. Your chosen use case and requirements
2. Provider evaluation criteria and weights
3. Test results and analysis
4. Final recommendation with justification

## Starter Code

```python
import streamlit as st
import time
from datetime import datetime
import pandas as pd

# Import your provider clients here
# import openai
# import anthropic

st.title("LLM Provider Comparison Tool")

# Sidebar for configuration
st.sidebar.header("Configuration")
selected_providers = st.sidebar.multiselect(
    "Select Providers",
    ["OpenAI", "Anthropic", "Google"],
    default=["OpenAI", "Anthropic"]
)

# Main interface
prompt = st.text_area("Enter your prompt:", height=100)

if st.button("Compare Responses"):
    if not prompt:
        st.error("Please enter a prompt")
    else:
        results = {}
        
        # Create columns for side-by-side comparison
        cols = st.columns(len(selected_providers))
        
        for idx, provider in enumerate(selected_providers):
            with cols[idx]:
                st.subheader(provider)
                
                # TODO: Implement provider API calls
                # start_time = time.time()
                # response = call_provider_api(provider, prompt)
                # end_time = time.time()
                
                # Display results
                # st.write(response)
                # st.metric("Response Time", f"{end_time - start_time:.2f}s")
                # st.metric("Estimated Cost", f"${calculate_cost(provider, tokens):.4f}")
                
                st.info("Implementation needed")
```

## Submission Guidelines

1. **Code Repository**
   - Create a GitHub repository for your project
   - Include requirements.txt with dependencies
   - Add a README with setup instructions

2. **Live Demo**
   - Deploy your app (Streamlit Cloud, Heroku, etc.)
   - Include the URL in your submission

3. **Report**
   - Submit as PDF or Markdown
   - Include screenshots of your tool
   - Provide cost analysis calculations

## Evaluation Criteria

- **Functionality** (40%): Does the tool work as specified?
- **Code Quality** (20%): Is the code clean and well-organized?
- **Analysis** (25%): How thorough is the provider evaluation?
- **Documentation** (15%): Is the project well-documented?

## Bonus Points
- Implement error handling and retry logic
- Add authentication management for API keys
- Create visualization of comparison results
- Include more than 3 providers

## Resources
- [Streamlit Documentation](https://docs.streamlit.io)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Anthropic API Reference](https://docs.anthropic.com)
- [Google Gemini API](https://ai.google.dev/docs)

## Due Date
Submit your completed assignment before the next session.

## Tips
- Start with 2 providers and expand once working
- Use environment variables for API keys
- Test with simple prompts first
- Consider rate limiting in your implementation
- Cache responses to avoid repeated API calls

Good luck! Contact the instructor if you have questions.