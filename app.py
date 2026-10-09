
import streamlit as st

st.set_page_config(
    page_title="Chandu AI Hub",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Chandu AI Hub")
st.subheader("Your AI tools, all in one place!")

st.write(
    "Welcome! Choose an AI assistant below "
    "to get started."
)

st.divider()

st.markdown("### 🤖 General AI Chatbot")
st.write("Ask questions and get AI-powered answers.")

st.link_button(
    "Open AI Chatbot 🚀",
    "https://aichatbot-hbksl92ybagtcfgjtgmrcp.streamlit.app/",
    use_container_width=True
)

st.divider()

st.markdown("### 🎓 College Information Chatbot")
st.write("Explore college-related information.")

st.link_button(
    "Open College Chatbot 🎓",
    "https://clginfoextroctor-kf2prpg8ggqk4ht2s5pls4.streamlit.app/",
    use_container_width=True
)

st.divider()

st.caption("Created by Chandu ❤️")
