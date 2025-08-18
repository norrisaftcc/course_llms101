#!/usr/bin/env python3
"""
SAGE MVP Setup Test Script
Verifies that everything is configured correctly
"""

import sys
import os
from pathlib import Path

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 50)
    print(f"  {text}")
    print("=" * 50)

def print_status(item, status, details=""):
    """Print status with formatting"""
    icon = "✅" if status else "❌"
    print(f"{icon} {item}")
    if details:
        print(f"   {details}")

def test_python_version():
    """Check Python version"""
    version = sys.version_info
    is_valid = version.major == 3 and version.minor >= 8
    
    print_status(
        "Python Version",
        is_valid,
        f"Found: {version.major}.{version.minor}.{version.micro}"
    )
    
    if not is_valid:
        print("   ⚠️  Python 3.8+ required")
    
    return is_valid

def test_dependencies():
    """Check if required packages are installed"""
    required = {
        "fastapi": "FastAPI web framework",
        "uvicorn": "ASGI server",
        "pydantic": "Data validation",
        "google.generativeai": "Gemini API client",
        "dotenv": "Environment variables"
    }
    
    all_installed = True
    
    for package, description in required.items():
        try:
            if package == "google.generativeai":
                import google.generativeai
            elif package == "dotenv":
                from dotenv import load_dotenv
            else:
                __import__(package)
            
            print_status(f"{description}", True, f"({package})")
        except ImportError:
            print_status(f"{description}", False, f"Missing: {package}")
            all_installed = False
    
    if not all_installed:
        print("\n   💡 Run: pip install -r requirements.txt")
    
    return all_installed

def test_project_files():
    """Check if all required files exist"""
    required_files = [
        "main.py",
        "ai_flows.py",
        "gemini.py",
        "db.py",
        "models.py",
        "requirements.txt",
        ".env.example"
    ]
    
    all_exist = True
    
    for file in required_files:
        exists = Path(file).exists()
        print_status(f"File: {file}", exists)
        
        if not exists:
            all_exist = False
    
    # Check for static directory and index.html
    static_exists = Path("static").exists()
    print_status("Directory: static/", static_exists)
    
    if static_exists:
        index_exists = Path("static/index.html").exists()
        print_status("File: static/index.html", index_exists)
        all_exist = all_exist and index_exists
    else:
        all_exist = False
    
    return all_exist

def test_environment():
    """Check environment configuration"""
    env_exists = Path(".env").exists()
    
    print_status(".env file", env_exists)
    
    if not env_exists:
        print("   💡 Run: cp .env.example .env")
        print("   Then add your GEMINI_API_KEY")
        return False
    
    # Check if API key is configured
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            print_status("GEMINI_API_KEY", False, "Not found in .env")
            return False
        
        if api_key == "your_gemini_api_key_here":
            print_status("GEMINI_API_KEY", False, "Still using placeholder")
            print("   💡 Get your key at: https://aistudio.google.com/app/apikey")
            return False
        
        # Mask the key for display
        masked_key = api_key[:10] + "..." + api_key[-4:]
        print_status("GEMINI_API_KEY", True, f"Found: {masked_key}")
        
        return True
        
    except ImportError:
        print_status("GEMINI_API_KEY", False, "Can't check (dotenv not installed)")
        return False

def test_gemini_connection():
    """Test Gemini API connection"""
    try:
        import google.generativeai as genai
        from dotenv import load_dotenv
        
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key or api_key == "your_gemini_api_key_here":
            print_status("Gemini API Test", False, "Invalid API key")
            return False
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Try a simple request
        response = model.generate_content(
            "Say 'SAGE test successful' in exactly 3 words",
            generation_config={'temperature': 0.1, 'max_output_tokens': 10}
        )
        
        if response and response.text:
            print_status("Gemini API Test", True, "Connection successful!")
            return True
        else:
            print_status("Gemini API Test", False, "No response received")
            return False
            
    except Exception as e:
        print_status("Gemini API Test", False, f"Error: {str(e)[:50]}")
        return False

def test_database():
    """Test database creation"""
    try:
        from db import Database
        
        # Create test database
        test_db = Database("test_sage.db")
        
        # Try to save an interaction
        test_db.save_interaction(
            user_id="test_user",
            message="Test message",
            response="Test response",
            mode="test"
        )
        
        # Check if it was saved
        usage = test_db.get_daily_usage("test_user")
        
        if usage > 0:
            print_status("Database Test", True, "SQLite working")
            
            # Clean up test database
            Path("test_sage.db").unlink(missing_ok=True)
            return True
        else:
            print_status("Database Test", False, "Could not save data")
            return False
            
    except Exception as e:
        print_status("Database Test", False, f"Error: {str(e)[:50]}")
        return False

def main():
    """Run all tests"""
    print("\n" + "🎓 SAGE MVP Setup Verification".center(50))
    print("=" * 50)
    
    results = []
    
    # Test 1: Python version
    print_header("1. Python Environment")
    results.append(test_python_version())
    
    # Test 2: Dependencies
    print_header("2. Dependencies")
    results.append(test_dependencies())
    
    # Test 3: Project files
    print_header("3. Project Files")
    results.append(test_project_files())
    
    # Test 4: Environment configuration
    print_header("4. Environment Configuration")
    results.append(test_environment())
    
    # Test 5: Gemini API (optional)
    if results[3]:  # Only if environment is configured
        print_header("5. Gemini API Connection")
        results.append(test_gemini_connection())
    
    # Test 6: Database
    if results[1]:  # Only if dependencies are installed
        print_header("6. Database")
        results.append(test_database())
    
    # Summary
    print_header("Summary")
    
    total = len(results)
    passed = sum(results)
    
    if passed == total:
        print("🎉 All tests passed! SAGE is ready to run.")
        print("\n📚 Start with: python main.py")
        print("🌐 Then open: http://localhost:8000")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
        print("\nFix the issues above, then run this test again.")
        
        if not results[1]:
            print("\n💡 Start by installing dependencies:")
            print("   pip install -r requirements.txt")
        elif not results[3]:
            print("\n💡 Configure your environment:")
            print("   1. Copy .env.example to .env")
            print("   2. Add your GEMINI_API_KEY")
            print("   Get a key at: https://aistudio.google.com/app/apikey")
    
    print("\n" + "=" * 50)
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)