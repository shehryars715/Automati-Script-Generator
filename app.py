import streamlit as st
from main import generate_script

st.set_page_config(page_title="YouTube Script Generator", page_icon="🎬", layout="centered")

st.title("🎬 YouTube Title & Script Generator")
st.write("Generate a catchy YouTube title and script using **Gemini AI** + LangChain.")

# User input
topic = st.text_input("Enter your video topic:")

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic first!")
    else:
        with st.spinner("Generating your title and script..."):
            try:
                script = generate_script(topic)
                st.subheader("Generated Script 📜")
                st.write(script)
            except Exception as e:
                st.error(f"Error: {e}")
                         
