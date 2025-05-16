#!/usr/bin/env python3
"""
Setup Verification Script for LLM 90-Minute Session
Checks that all prerequisites are properly installed and configured
"""

import sys
import subprocess
import os
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color

def print_status(message, status):
    """Print colored status messages"""
    if status == "success":
        print(f"{GREEN}✓{NC} {message}")
    elif status == "error":
        print(f"{RED}✗{NC} {message}")
    elif status == "warning":
        print(f"{YELLOW}!{NC} {message}")
    else:
        print(f"  {message}")

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    try:
        version = sys.version_info
        if version.major == 3 and version.minor >= 8:
            print_status(f"Python {version.major}.{version.minor}.{version.micro} detected", "success")
            return True
        else:
            print_status(f"Python {version.major}.{version.minor} detected. Need 3.8+", "error")
            return False
    except:
        print_status("Could not detect Python version", "error")
        return False

def check_package(package_name):
    """Check if a Python package is installed"""
    try:
        __import__(package_name)
        print_status(f"{package_name} installed", "success")
        return True
    except ImportError:
        print_status(f"{package_name} not installed", "error")
        return False

def check_api_keys():
    """Check if required API keys are set"""
    keys_found = True
    
    # Check for API keys in environment or .env file
    openai_key = os.getenv("OPENAI_API_KEY")
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    # Also check .env file if it exists
    if Path(".env").exists():
        try:
            from dotenv import load_dotenv
            load_dotenv()
            openai_key = openai_key or os.getenv("OPENAI_API_KEY")
            supabase_url = supabase_url or os.getenv("SUPABASE_URL")
            supabase_key = supabase_key or os.getenv("SUPABASE_KEY")
        except:
            pass
    
    if openai_key:
        print_status("OpenAI API key found", "success")
    else:
        print_status("OpenAI API key not found", "warning")
        print("  Set with: export OPENAI_API_KEY=your-key-here")
        keys_found = False
    
    if supabase_url:
        print_status("Supabase URL found", "success")
    else:
        print_status("Supabase URL not found", "warning")
        print("  Set with: export SUPABASE_URL=your-url-here")
        keys_found = False
    
    if supabase_key:
        print_status("Supabase key found", "success")
    else:
        print_status("Supabase key not found", "warning")
        print("  Set with: export SUPABASE_KEY=your-key-here")
        keys_found = False
    
    return keys_found

def check_git():
    """Check if Git is installed"""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        print_status("Git installed", "success")
        return True
    except:
        print_status("Git not installed", "error")
        return False

def check_internet():
    """Check internet connectivity"""
    try:
        import urllib.request
        urllib.request.urlopen('https://openai.com', timeout=5)
        print_status("Internet connection working", "success")
        return True
    except:
        print_status("No internet connection", "error")
        return False

def test_streamlit():
    """Test if Streamlit can be launched"""
    try:
        # Create a minimal test app
        test_app = """
import streamlit as st
st.title("Test App")
st.write("If you see this, Streamlit is working!")
"""
        
        with open("test_streamlit.py", "w") as f:
            f.write(test_app)
        
        print_status("Streamlit test file created", "success")
        print_status("To test Streamlit, run: streamlit run test_streamlit.py", "info")
        return True
    except Exception as e:
        print_status(f"Could not create Streamlit test: {e}", "error")
        return False

def main():
    """Run all verification checks"""
    print("\n🔍 LLM Course Setup Verification\n")
    
    all_good = True
    
    # Check Python version
    print("1. Checking Python version...")
    if not check_python_version():
        all_good = False
    print()
    
    # Check required packages
    print("2. Checking required packages...")
    packages = ["streamlit", "openai", "supabase"]
    for package in packages:
        if not check_package(package):
            all_good = False
    print()
    
    # Check API keys
    print("3. Checking API keys...")
    if not check_api_keys():
        all_good = False
    print()
    
    # Check Git
    print("4. Checking Git installation...")
    if not check_git():
        all_good = False
    print()
    
    # Check internet
    print("5. Checking internet connection...")
    if not check_internet():
        all_good = False
    print()
    
    # Test Streamlit
    print("6. Setting up Streamlit test...")
    test_streamlit()
    print()
    
    # Final summary
    print("="*40)
    if all_good:
        print(f"{GREEN}✓ All checks passed! You're ready for the session.{NC}")
    else:
        print(f"{YELLOW}! Some issues found. Please fix them before the session.{NC}")
        print("\nQuick fixes:")
        print("1. Install missing packages: pip install streamlit openai supabase")
        print("2. Set up API keys in environment variables or .env file")
        print("3. Ensure you have a stable internet connection")
    print("="*40)
    
    # Create .env template if it doesn't exist
    if not Path(".env").exists():
        print("\nCreating .env template...")
        with open(".env", "w") as f:
            f.write("""# API Keys for LLM Course
OPENAI_API_KEY=your-openai-api-key-here
SUPABASE_URL=your-supabase-url-here
SUPABASE_KEY=your-supabase-anon-key-here
""")
        print_status(".env template created. Add your API keys here.", "success")

if __name__ == "__main__":
    main()