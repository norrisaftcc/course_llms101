# Troubleshooting Guide for 90-Minute LLM Session

## Table of Contents
1. [Pre-Session Setup Issues](#pre-session-setup-issues)
2. [During Session Problems](#during-session-problems)
3. [API and Connection Issues](#api-and-connection-issues)
4. [Platform-Specific Problems](#platform-specific-problems)
5. [Quick Fixes Cheat Sheet](#quick-fixes-cheat-sheet)

## Pre-Session Setup Issues

### Python Installation Problems

#### Issue: "Python not found" or wrong version
**Solution**:
```bash
# Check current version
python --version
python3 --version

# If not installed or wrong version:
# Mac:
brew install python@3.11

# Windows:
# Download from python.org and add to PATH

# Linux:
sudo apt-get update
sudo apt-get install python3.11
```

#### Issue: Multiple Python versions causing confusion
**Solution**:
```bash
# Use python3 explicitly
python3 -m pip install streamlit

# Or create a virtual environment
python3 -m venv llm_env
source llm_env/bin/activate  # Mac/Linux
llm_env\Scripts\activate  # Windows
```

### Package Installation Issues

#### Issue: "pip: command not found"
**Solution**:
```bash
# Install pip
python3 -m ensurepip

# Or on Ubuntu/Debian
sudo apt-get install python3-pip
```

#### Issue: Permission denied when installing packages
**Solution**:
```bash
# Install for user only
pip install --user streamlit openai supabase

# Or use virtual environment (recommended)
python3 -m venv llm_env
source llm_env/bin/activate
pip install streamlit openai supabase
```

#### Issue: SSL certificate errors during installation
**Solution**:
```bash
# Temporary fix (not recommended for production)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org streamlit

# Better solution: Update certificates
# Mac:
brew install ca-certificates

# Or use corporate proxy settings
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
```

## During Session Problems

### Streamlit Issues

#### Issue: "streamlit: command not found"
**Solution**:
```bash
# Run with python module
python3 -m streamlit run ai_blog.py

# Or add to PATH
export PATH=$PATH:$HOME/.local/bin

# Windows: Add Python Scripts to PATH
```

#### Issue: Streamlit app won't load
**Solution**:
1. Check if port 8501 is already in use:
   ```bash
   # Mac/Linux
   lsof -i :8501
   
   # Windows
   netstat -ano | findstr :8501
   ```
2. Kill the process or use different port:
   ```bash
   streamlit run ai_blog.py --server.port 8502
   ```

#### Issue: Streamlit shows blank page
**Solution**:
- Clear browser cache
- Try different browser
- Disable browser extensions
- Use incognito/private mode

### Import Errors

#### Issue: "ModuleNotFoundError: No module named 'openai'"
**Solution**:
```bash
# Ensure you're in the right environment
which python3
which pip3

# Reinstall packages
pip3 install openai supabase streamlit

# Check installation
pip3 list | grep openai
```

#### Issue: Version conflicts
**Solution**:
```bash
# Install specific versions
pip install openai==0.28.1 streamlit==1.28.1 supabase==2.0.3

# Or use requirements.txt
pip install -r requirements.txt
```

## API and Connection Issues

### OpenAI API Issues

#### Issue: "Invalid API key"
**Solution**:
1. Check your API key:
   ```bash
   echo $OPENAI_API_KEY
   ```
2. Set correctly:
   ```bash
   export OPENAI_API_KEY="sk-..."
   ```
3. Or use .env file:
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=sk-..." > .env
   ```

#### Issue: Rate limit exceeded
**Solution**:
- Wait 60 seconds
- Use smaller model (gpt-3.5-turbo instead of gpt-4)
- Implement rate limiting in code

#### Issue: Connection timeout
**Solution**:
- Check internet connection
- Verify firewall settings
- Try using a VPN
- Check OpenAI service status

### Supabase Issues

#### Issue: "Invalid Supabase URL or key"
**Solution**:
1. Get correct values from Supabase dashboard:
   - Settings → API → Project URL
   - Settings → API → anon public key
2. Set environment variables:
   ```bash
   export SUPABASE_URL="https://xxxx.supabase.co"
   export SUPABASE_KEY="eyJhbGc..."
   ```

#### Issue: Database connection failed
**Solution**:
- Check if project is paused (free tier)
- Verify database is created
- Run SQL schema in Supabase SQL editor
- Check network connectivity

## Platform-Specific Problems

### Windows-Specific

#### Issue: Long path names causing errors
**Solution**:
```powershell
# Enable long paths in Windows
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

#### Issue: Execution policy blocking scripts
**Solution**:
```powershell
# Allow script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### macOS-Specific

#### Issue: SSL certificate errors on corporate network
**Solution**:
```bash
# Export corporate certificates
export REQUESTS_CA_BUNDLE=/path/to/corporate-cert.pem
export SSL_CERT_FILE=/path/to/corporate-cert.pem
```

#### Issue: M1/M2 Mac compatibility
**Solution**:
```bash
# Install for ARM64 architecture
arch -arm64 brew install python@3.11
arch -arm64 pip install streamlit openai supabase
```

### Linux-Specific

#### Issue: Missing system dependencies
**Solution**:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev build-essential

# RHEL/CentOS
sudo yum install python3-devel gcc
```

## Quick Fixes Cheat Sheet

### Before the Session Checklist
```bash
# 1. Run setup verification
python3 verify_setup.py

# 2. Test Streamlit
streamlit hello

# 3. Check API keys
echo $OPENAI_API_KEY
echo $SUPABASE_URL
echo $SUPABASE_KEY

# 4. Test internet
ping openai.com
ping supabase.com

# 5. Create backup .env
cp .env .env.backup
```

### Common Commands
```bash
# Kill stuck Streamlit
pkill -f streamlit

# Clear pip cache
pip cache purge

# Reinstall everything
pip uninstall -y streamlit openai supabase
pip install -r requirements.txt

# Check Python path
which python3
python3 -c "import sys; print(sys.path)"

# Test OpenAI connection
python3 -c "import openai; print('OpenAI OK')"

# Test Supabase connection
python3 -c "import supabase; print('Supabase OK')"
```

### Emergency Fallbacks

1. **Use Google Colab**:
   - Upload code to Colab
   - Install packages in notebook
   - Run Streamlit with localtunnel

2. **Use pre-configured Codespace**:
   - Fork the repo to your GitHub
   - Open in GitHub Codespaces
   - Everything pre-installed

3. **Use local SQLite instead of Supabase**:
   - Comment out Supabase code
   - Use in-memory database
   - Focus on AI features

### Getting Help

**During Session**:
- Raise hand for instructor help
- Post in Discord #help channel
- Check pinned messages for updates

**Resources**:
- Discord: [Course Discord Server]
- Email: support@llmcourse.com
- Office Hours: Thursdays 3-4 PM

### Session Day Emergency Kit

1. **Backup API Keys** (instructor will provide if needed)
2. **Offline Demo** (if internet fails)
3. **Pre-recorded Videos** (backup demonstrations)
4. **USB with Dependencies** (for offline install)
5. **Mobile Hotspot** (backup internet)

Remember: The goal is learning, not perfect setup. We'll help you get running!