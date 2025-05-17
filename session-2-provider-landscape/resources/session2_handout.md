# Session 2: LLM Provider Landscape - Quick Reference

## Major LLM Providers at a Glance

### OpenAI
- **Models**: GPT-4, GPT-3.5-turbo, text-embeddings
- **Strengths**: Most mature, largest ecosystem, best general performance
- **Pricing**: 
  - GPT-3.5: $0.50/1M input, $1.50/1M output tokens
  - GPT-4: $10/1M input, $30/1M output tokens
- **Best for**: General purpose, prototyping, wide compatibility

### Anthropic (Claude)
- **Models**: Claude 3 Opus/Sonnet/Haiku
- **Strengths**: Large context (200K+), safety-focused, strong reasoning
- **Pricing**:
  - Haiku: $0.25/1M input, $1.25/1M output tokens
  - Sonnet: $3/1M input, $15/1M output tokens
- **Best for**: Long documents, safety-critical apps, complex reasoning

### Google (Gemini)
- **Models**: Gemini Pro, Gemini Ultra, Gemini Nano
- **Strengths**: Multimodal, Google integration, competitive pricing
- **Pricing**:
  - Gemini Pro: $0.25/1M input, $1.25/1M output tokens
- **Best for**: Multimodal tasks, Google ecosystem apps

### Others
- **Cohere**: Enterprise focus, custom models
- **Mistral**: Open weights, self-hosting option
- **Meta Llama**: Fully open source, no API costs

## Provider Selection Checklist

- [ ] Define your use case clearly
- [ ] Estimate monthly token usage
- [ ] Identify must-have features
- [ ] Consider compliance requirements
- [ ] Test with real prompts
- [ ] Calculate total costs
- [ ] Plan for provider switching

## Cost Optimization Tips

1. **Use appropriate models**: Don't use GPT-4 for simple tasks
2. **Implement caching**: Store common responses
3. **Optimize prompts**: Shorter prompts = lower costs
4. **Batch requests**: Reduce API overhead
5. **Monitor usage**: Set up alerts and limits

## Quick Decision Matrix

| Factor | Weight | OpenAI | Anthropic | Google |
|--------|--------|--------|-----------|--------|
| Cost | 25% | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Performance | 20% | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Features | 20% | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Reliability | 15% | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Ecosystem | 10% | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Support | 10% | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

## API Quick Start

### OpenAI
```python
import openai
openai.api_key = "sk-..."
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### Anthropic
```python
import anthropic
client = anthropic.Client(api_key="sk-...")
response = client.messages.create(
    model="claude-3-haiku-20240307",
    messages=[{"role": "user", "content": "Hello"}]
)
```

### Google
```python
import google.generativeai as genai
genai.configure(api_key="...")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello")
```

## Resources

- [OpenAI Pricing](https://openai.com/pricing)
- [Anthropic Pricing](https://anthropic.com/pricing)
- [Google AI Pricing](https://ai.google.dev/pricing)
- [LLM Leaderboard](https://artificialanalysis.ai/models)
- [Token Counter](https://platform.openai.com/tokenizer)