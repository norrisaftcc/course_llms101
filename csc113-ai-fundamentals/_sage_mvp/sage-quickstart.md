# 🚀 SAGE MVP - 5-Minute Quick Start

## You Need

1. **Python 3.8+** installed ([python.org](https://python.org))
2. **5 minutes** of your time
3. **Free Gemini API key** (we'll get this)

## Step-by-Step Setup

### 1️⃣ Download the Code (30 seconds)

**Option A: Download ZIP**
- Click "Code" → "Download ZIP" on GitHub
- Extract to a folder like `sage-mvp/`

**Option B: Git Clone**
```bash
git clone https://github.com/yourusername/sage-mvp.git
cd sage-mvp
```

### 2️⃣ Get Your Free API Key (2 minutes)

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (looks like: `AIzaSy...`)

### 3️⃣ Run the Setup (2 minutes)

**On Windows:**
```cmd
# Double-click start.bat
# OR run in terminal:
start.bat
```

**On Mac/Linux:**
```bash
# Make executable and run:
chmod +x start.sh
./start.sh
```

**Manual Setup:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Add your API key to .env file
# Edit .env and replace your_gemini_api_key_here with your actual key
```

### 4️⃣ Start SAGE (30 seconds)

```bash
python main.py
```

### 5️⃣ Open Your Browser

Go to: [http://localhost:8000](http://localhost:8000)

**That's it! You're done! 🎉**

---

## First Message to Try

Type this in the chat:
```
Explain what a function is in programming with a simple example
```

You should get a clear explanation with code examples!

---

## Quick Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "API key not found"
- Edit `.env` file
- Add: `GEMINI_API_KEY=your_actual_key_here`

### "Port 8000 already in use"
```bash
# Use different port
python main.py --port 8001
```

### Test Everything
```bash
python test_setup.py
```

---

## What You Get

- ✅ **900 free AI requests per day**
- ✅ **Smart study assistant** that remembers context
- ✅ **Multiple modes** (explain, practice, debug)
- ✅ **Clean web interface** that just works
- ✅ **API documentation** at `/docs`
- ✅ **Zero monthly cost**

---

## Folder Structure

After setup, you'll have:
```
sage-mvp/
├── venv/             # Python packages (created)
├── static/           # Web files
│   └── index.html    # Web interface
├── main.py           # Main app
├── ai_flows.py       # AI logic
├── gemini.py         # Gemini wrapper
├── db.py            # Database
├── models.py        # Data models
├── .env             # YOUR API KEY HERE
├── sage.db          # Database (created)
└── requirements.txt  # Dependencies
```

---

## Next Steps

1. **Try different modes**: Practice, Explain, Debug
2. **Check API docs**: http://localhost:8000/docs
3. **Monitor usage**: See daily count in header
4. **Customize subjects**: Edit the dropdown options
5. **Deploy online**: Use Render.com free tier

---

## Need Help?

1. Run `python test_setup.py` to check setup
2. Check terminal for error messages
3. Make sure `.env` has your real API key
4. Try a simple prompt first

**Remember**: This is YOUR study assistant. It's free, it's simple, and it works!

Ready to learn? Open [http://localhost:8000](http://localhost:8000) and start asking questions! 🎓