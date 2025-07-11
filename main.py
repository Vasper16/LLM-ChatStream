from utils import export_chat_to_pdf
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import datetime

# ---------------------- Streamlit Config FIRST ----------------------
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",
    layout="centered",
)

# ---------------------- Load Environment ----------------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ---------------------- Gemini Model Init ----------------------
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-1.5-flash')

# ---------------------- Session Init ----------------------
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "turns" not in st.session_state:
    st.session_state["turns"] = 0

# ---------------------- Theme Definitions ----------------------
THEMES = {
    "dark": """
        body {
            background-color: #1e1e1e;
            color: #f0f0f0;
        }
        .chat-bubble {
            background-color: #374151;
            color: #f0f0f0;
        }
        .user-bubble {
            background-color: #3b82f6;
            color: white;
        }
    """,
    "light": """
        body {
            background-color: #ffffff;
            color: #111111;
        }
        .chat-bubble {
            background-color: #f0f0f0;
            color: #111111;
        }
        .user-bubble {
            background-color: #3b82f6;
            color: white;
        }
    """
}

# ---------------------- Sidebar ----------------------
with st.sidebar:
    st.header("📊 Chat Metrics")
    st.metric("Total Messages", st.session_state["turns"])

    st.markdown("---")
    st.subheader("📄 Export Chat")
    if st.button("Download Chat as PDF"):
        filename = export_chat_to_pdf(st.session_state.chat_session.history)
        with open(filename, "rb") as f:
            st.download_button(
                label="📥 Save chat_log.pdf",
                data=f,
                file_name="chat_log.pdf",
                mime="application/pdf"
            )

    st.markdown("---")
    st.subheader("🔁 Reset Chat")
    if st.button("🔄 Reset Conversation"):
        st.session_state.chat_session = model.start_chat(history=[])
        st.session_state["turns"] = 0
        st.rerun()

    st.markdown("---")
    st.subheader("💡 Quick Prompts")
    if st.button("What is Python?"):
        st.session_state.quick_prompt = "What is Python?"
    if st.button("Explain Quantum Computing"):
        st.session_state.quick_prompt = "Explain Quantum Computing"
    if st.button("Benefits of AI in Education"):
        st.session_state.quick_prompt = "Benefits of AI in Education"

    st.markdown("---")
    st.subheader("🎨 Choose Theme")
    selected_theme = st.radio("Theme", ["dark", "light"], index=0)

# ---------------------- Apply Theme CSS ----------------------
st.markdown(f"<style>{THEMES[selected_theme]}</style>", unsafe_allow_html=True)

# ---------------------- Load Global Style ----------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------------- Title ----------------------
st.title("🤖 Gemini Pro - ChatBot")

# ---------------------- Display Chat History ----------------------
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

for message in st.session_state.chat_session.history:
    role = translate_role_for_streamlit(message.role)
    bubble_class = "user-bubble" if role == "user" else "assistant-bubble"
    with st.chat_message(role):
        st.markdown(
            f"<div class='chat-bubble {bubble_class}'>{message.parts[0].text}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<small style='color:gray;'>{datetime.datetime.now().strftime('%H:%M')}</small>",
            unsafe_allow_html=True
        )

# ---------------------- Input & Response Handling ----------------------
user_prompt = st.chat_input("Ask Gemini-Pro...")

# Handle Quick Prompts
if user_prompt is None and "quick_prompt" in st.session_state:
    user_prompt = st.session_state.quick_prompt
    del st.session_state.quick_prompt

# Handle User Input
if user_prompt:
    with st.chat_message("user"):
        st.markdown(
            f"<div class='chat-bubble user-bubble'>{user_prompt}</div>",
            unsafe_allow_html=True
        )
    st.session_state["turns"] += 1

    gemini_response = st.session_state.chat_session.send_message(
        user_prompt,
        stream=True
    )

    with st.chat_message("assistant"):
        full_response = ""
        response_box = st.empty()
        for chunk in gemini_response:
            full_response += chunk.text
            response_box.markdown(
                f"<div class='chat-bubble assistant-bubble'>{full_response}▌</div>",
                unsafe_allow_html=True
            )
        response_box.markdown(
            f"<div class='chat-bubble assistant-bubble'>{full_response}</div>",
            unsafe_allow_html=True
        )
