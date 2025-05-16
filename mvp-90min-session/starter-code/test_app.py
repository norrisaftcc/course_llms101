
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
