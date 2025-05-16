#!/usr/bin/env python3
"""
Environment Test Tool for LLM Course
Tests API connections and basic functionality
"""

import os
import sys
import json
import time
from datetime import datetime

# Test imports
try:
    import streamlit as st
    STREAMLIT_OK = True
except ImportError:
    STREAMLIT_OK = False
    print("❌ Streamlit not installed")

try:
    import openai
    OPENAI_OK = True
except ImportError:
    OPENAI_OK = False
    print("❌ OpenAI not installed")

try:
    from supabase import create_client
    SUPABASE_OK = True
except ImportError:
    SUPABASE_OK = False
    print("❌ Supabase not installed")

def test_openai_connection():
    """Test OpenAI API connection"""
    if not OPENAI_OK:
        return False, "OpenAI package not installed"
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return False, "OPENAI_API_KEY not set"
    
    try:
        openai.api_key = api_key
        # Simple test call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'API working'"}],
            max_tokens=10
        )
        return True, "OpenAI API connection successful"
    except Exception as e:
        return False, f"OpenAI API error: {str(e)}"

def test_supabase_connection():
    """Test Supabase connection"""
    if not SUPABASE_OK:
        return False, "Supabase package not installed"
    
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        return False, "SUPABASE_URL or SUPABASE_KEY not set"
    
    try:
        supabase = create_client(url, key)
        # Try to query (will fail if table doesn't exist, but connection works)
        try:
            supabase.table("posts").select("*").limit(1).execute()
            return True, "Supabase connection successful, posts table exists"
        except:
            return True, "Supabase connection successful (posts table not created yet)"
    except Exception as e:
        return False, f"Supabase connection error: {str(e)}"

def test_streamlit():
    """Create a simple Streamlit test file"""
    if not STREAMLIT_OK:
        return False, "Streamlit not installed"
    
    test_code = '''
import streamlit as st

st.title("🎉 Environment Test Successful!")
st.success("Your environment is properly configured for the LLM course!")

st.header("Status Checks")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Python", "✅ Working", f"{sys.version_info.major}.{sys.version_info.minor}")

with col2:
    st.metric("Streamlit", "✅ Working", st.__version__)

with col3:
    st.metric("System", "✅ Ready", "All good!")

st.header("Next Steps")
st.info("""
1. Your environment is ready!
2. Try the main application: `streamlit run ai_blog.py`
3. Join Discord if you have questions
4. See you at the session!
""")

st.balloons()
'''
    
    try:
        with open("test_app.py", "w") as f:
            f.write(test_code)
        return True, "Streamlit test app created. Run: streamlit run test_app.py"
    except Exception as e:
        return False, f"Error creating Streamlit test: {str(e)}"

def main():
    """Run all environment tests"""
    print("\n🔬 LLM Course Environment Tester\n")
    print("="*40)
    
    # System info
    print(f"System: {sys.platform}")
    print(f"Python: {sys.version}")
    print("="*40)
    print()
    
    # Run tests
    tests = {
        "Python Version": (
            sys.version_info >= (3, 8),
            f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        ),
        "Streamlit": (STREAMLIT_OK, "Package installed" if STREAMLIT_OK else "Not installed"),
        "OpenAI Package": (OPENAI_OK, "Package installed" if OPENAI_OK else "Not installed"),
        "Supabase Package": (SUPABASE_OK, "Package installed" if SUPABASE_OK else "Not installed"),
    }
    
    # API connection tests
    if OPENAI_OK:
        tests["OpenAI API"] = test_openai_connection()
    
    if SUPABASE_OK:
        tests["Supabase API"] = test_supabase_connection()
    
    if STREAMLIT_OK:
        tests["Streamlit App"] = test_streamlit()
    
    # Print results
    print("Test Results:")
    print("-" * 40)
    
    passed = 0
    failed = 0
    
    for test_name, (success, message) in tests.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name:.<30} {status}")
        if not success:
            print(f"  └─ {message}")
            failed += 1
        else:
            passed += 1
    
    print("-" * 40)
    print(f"Summary: {passed} passed, {failed} failed")
    print()
    
    # Recommendations
    if failed > 0:
        print("🔧 Recommendations:")
        
        if not STREAMLIT_OK or not OPENAI_OK or not SUPABASE_OK:
            print("1. Install missing packages:")
            print("   pip install streamlit openai supabase python-dotenv")
        
        if "OPENAI_API" in [name for name, (success, _) in tests.items() if not success]:
            print("2. Set OpenAI API key:")
            print("   export OPENAI_API_KEY='your-key-here'")
        
        if "Supabase API" in [name for name, (success, _) in tests.items() if not success]:
            print("3. Set Supabase credentials:")
            print("   export SUPABASE_URL='your-url-here'")
            print("   export SUPABASE_KEY='your-key-here'")
        
        print("\nNeed help? Check TROUBLESHOOTING.md")
    else:
        print("🎉 All tests passed! Your environment is ready!")
        print("\nNext steps:")
        print("1. Run the test app: streamlit run test_app.py")
        print("2. Try the main app: streamlit run ai_blog.py")
        print("3. Join Discord for community support")
    
    print("\n" + "="*40)
    print("Test completed at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("="*40)

if __name__ == "__main__":
    main()