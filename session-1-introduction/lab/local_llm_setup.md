# Lab 1: Your First Local LLM
*Time: 45 minutes*

## Learning Objectives
By the end of this lab, you will:
- Run an LLM entirely on your computer
- Understand what data stays local vs goes to the cloud
- Compare local vs cloud AI performance and privacy

## Part 1: Install Ollama (15 minutes)

### macOS/Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Windows
Download from: https://ollama.ai/download/windows

### Verify Installation
```bash
ollama --version
```

## Part 2: Download Your First Model (10 minutes)

```bash
# Download Mistral (3.8GB - good balance of size/performance)
ollama pull mistral

# Or for limited hardware, try tinyllama (638MB)
ollama pull tinyllama
```

### Check What You Downloaded
```bash
# List your local models
ollama list

# See model details
ollama show mistral
```

## Part 3: Run Your Local AI (10 minutes)

### Interactive Mode
```bash
ollama run mistral
```

Try these prompts:
1. "Explain what happens to my data when I use you"
2. "Write a Python function to check if a number is prime"
3. "What are you not allowed to tell me?"

Type `/bye` to exit.

### API Mode (Like ChatGPT but Local!)
```bash
# In one terminal, start the server
ollama serve

# In another terminal, make API calls
curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Why is the sky blue?"
}'
```

## Part 4: Privacy Comparison Exercise (10 minutes)

Create a file `privacy_test.md` and complete this table:

| Aspect | Local (Ollama) | ChatGPT | Claude |
|--------|---------------|---------|---------|
| Where is computation done? | Your CPU/GPU | OpenAI servers | Anthropic servers |
| Who sees your prompts? | Only you | OpenAI | Anthropic |
| Internet required? | Only for download | Always | Always |
| Cost per prompt? | $0 (your electricity) | ~$0.002 | ~$0.003 |
| Speed? | [Your result] | [Your result] | [Your result] |
| Can it be shut down? | No - it's yours | Yes | Yes |

## Part 5: Performance Test

Run this same prompt on all three:
```
Generate a 5-item shopping list for making tacos
```

Record:
- Response time
- Quality of response
- Any differences you notice

## Reflection Questions

1. **When would you choose local over cloud?**
   Think about: Privacy needs, internet availability, cost, speed

2. **What surprised you?**
   Most students are surprised that local AI works this well

3. **What data did you NOT send to any company?**
   Everything you typed in Ollama stayed on your machine

## Troubleshooting

### "Ollama: command not found"
- Mac: Try `/usr/local/bin/ollama`
- Windows: Restart terminal after install
- Linux: Add to PATH: `export PATH=$PATH:/usr/local/bin`

### "Model too slow"
- Try smaller model: `ollama pull tinyllama`
- Close other applications
- Check RAM: `ollama ps` shows memory usage

### "Connection refused on API"
- Ensure server is running: `ollama serve`
- Check port: `lsof -i :11434`

## Bonus Challenges

1. **Python Integration**
```python
import requests
import json

response = requests.post('http://localhost:11434/api/generate',
    json={
        "model": "mistral",
        "prompt": "Hello from Python!",
        "stream": False
    })
print(json.loads(response.text)['response'])
```

2. **Compare Models**
- Try `ollama pull llama2` vs `mistral`
- Which is faster? Better? Bigger?

3. **System Resources**
- Run `htop` or Task Manager while generating
- How much RAM/CPU does local AI use?

## Submission

Create `week1_reflection.md` with:
1. Your completed comparison table
2. Screenshots of Ollama running
3. Your answers to reflection questions
4. One prompt where local was BETTER than cloud
5. One prompt where cloud was BETTER than local

## What You Learned

✅ You can run AI without any company involvement  
✅ Your prompts can stay completely private  
✅ Local AI is good enough for many tasks  
✅ You understand the privacy/performance tradeoffs  

**Next Week**: We'll audit what cloud AI services actually do with your data