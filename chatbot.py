import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(page_title="Gym & Mental Health Chatbot", layout="centered")

# Custom CSS styles with white background
st.markdown("""
    <style>
    body, .stApp {
        background-color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        color: #2E8B57;
        font-size: 3em;
        font-weight: bold;
        margin-top: 30px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #555;
        margin-bottom: 20px;
    }
    .chat-container {
        display: flex;
        justify-content: center;
        padding: 20px;
    }
    iframe {
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Frontend content
st.markdown("<div class='title'>🏋️ Gym & Mental Health Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask me anything about fitness, workouts, or mental wellness!</div>", unsafe_allow_html=True)

# Embed Dialogflow chatbot iframe
components.html(
    """
    <div class="chat-container">
        <iframe width="350" height="430" allow="microphone;" 
        src="https://console.dialogflow.com/api-client/demo/embedded/bd484113-fc43-4e0c-abcf-0355d64f88db">
        </iframe>
    </div>
    """,
    height=500
)
