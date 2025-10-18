import streamlit as st
from src.chatbot import ask_chatbot

# ----------------------
# Page configuration
# ----------------------
st.set_page_config(
    page_title="ML Mentor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------
# Dark Mode CSS
# ----------------------
st.markdown("""
<style>
/* Page background and text */
body {
    background-color: #1e1e2f;
    color: #f0f0f0;
    font-family: 'Segoe UI', sans-serif;
}

/* Sidebar */
.sidebar .sidebar-content {
    background-color: #2a2a3a;
    padding: 15px;
}

/* Sidebar header */
.sidebar-header {
    font-size: 1.4rem;
    font-weight: 700;
    color: #f0f0f0;
    text-align: center;
    margin-bottom: 1rem;
}

/* Topic cards */
.topic-card {
    background-color: #33334d;
    padding: 10px 12px;
    border-radius: 8px;
    border-left: 3px solid #4dabf5;
    margin: 6px 0;
    transition: all 0.2s ease;
}
.topic-card:hover {
    background-color: #3a3a5a;
    transform: translateY(-1px);
}

/* Section titles */
.section-title {
    font-size: 1.1rem;
    font-weight: 600;
    color: #f0f0f0;
    margin: 15px 0 10px 0;
    border-bottom: 2px solid #4dabf5;
    padding-bottom: 5px;
}

/* Quick question buttons */
.quick-question-btn {
    background-color: #3ecf8e;
    color: #1e1e2f;
    border: none;
    border-radius: 12px;
    padding: 8px 12px;
    margin: 4px 0;
    font-size: 0.85rem;
    width: 100%;
    text-align: left;
    transition: all 0.2s ease;
    cursor: pointer;
}
.quick-question-btn:hover {
    background-color: #36b576;
    transform: translateY(-1px);
}

/* Main content */
.main-title {
    text-align: center;
    margin-bottom: 20px;
    font-size: 2rem;
}

/* Input box */
.stTextInput>div>div>input {
    background-color: #2a2a3a;
    color: #f0f0f0;
}

/* Send button */
.stButton>button {
    background-color: #4dabf5;
    color: #1e1e2f;
    font-weight: 600;
}
.stButton>button:hover {
    background-color: #3a9ee0;
}

/* Chat container */
.chat-container {
    background-color: #2a2a3a;
    border-radius: 10px;
    padding: 20px;
    margin: 15px 0;
    max-height: 400px;
    overflow-y: auto;
}

/* Messages */
.user-message {
    background-color: #4dabf5;
    color: #f0f0f0;
    padding: 10px 15px;
    border-radius: 15px 15px 5px 15px;
    margin: 8px 0;
    max-width: 80%;
    margin-left: auto;
    font-size: 0.95rem;
}

.bot-message {
    background-color: #3a3a5a;
    color: #f0f0f0;
    padding: 10px 15px;
    border-radius: 15px 15px 15px 5px;
    margin: 8px 0;
    max-width: 80%;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------
# Session state
# ----------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------
# Layout with columns
# ----------------------
# Columns: left sidebar, main, right sidebar
left_col, main_col, right_col = st.columns([1, 3, 1])

# ----------------------
# Left Sidebar (topics + info)
# ----------------------
with left_col:
    st.markdown('<div class="sidebar-header">🧠 ML Mentor</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📚 Topics</div>', unsafe_allow_html=True)
    topics = [
        {"icon": "🎯", "name": "Feature Engineering"},
        {"icon": "📊", "name": "Model Evaluation"},
        {"icon": "💬", "name": "NLP"},
        {"icon": "🧠", "name": "Neural Networks"},
        {"icon": "👨‍🏫", "name": "Supervised Learning"},
        {"icon": "🔍", "name": "Unsupervised Learning"}
    ]
    for topic in topics:
        st.markdown(f"""
        <div class="topic-card">
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="font-size: 1.1rem;">{topic['icon']}</div>
                <div style="font-weight: 600;">{topic['name']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">ℹ️ How to Use</div>', unsafe_allow_html=True)
    st.markdown("""
    - Click **quick questions** on the right  
    - Or type your **own question** below  
    - Ask about **any ML topic**  
    - **Clear chat** to start fresh
    """)

# ----------------------
# Right Sidebar (quick questions)
# ----------------------
with right_col:
    st.markdown('<div class="section-title">🚀 Quick Questions</div>', unsafe_allow_html=True)
    quick_questions = [
        "What is supervised learning?",
        "How do neural networks work?",
        "What is feature engineering?",
        "Explain model evaluation metrics",
        "What is NLP used for?",
        "Compare supervised vs unsupervised learning"
    ]
    for i, question in enumerate(quick_questions):
        if st.button(f"💬 {question}", key=f"quick_{i}"):
            st.session_state.chat_history.append(("You", question))
            with st.spinner("🤖 Thinking..."):
                answer = ask_chatbot(question)
            st.session_state.chat_history.append(("Bot", answer))
            st.rerun()

# ----------------------
# Main Column (input + conversation)
# ----------------------
with main_col:
    st.markdown('<div class="main-title">💭 Ask Your Question</div>', unsafe_allow_html=True)

    user_input = st.text_input(
        "Type your question:",
        placeholder="Enter your machine learning question here...",
        label_visibility="collapsed"
    )
    if st.button("Send 🚀", use_container_width=True) and user_input.strip():
        st.session_state.chat_history.append(("You", user_input))
        with st.spinner("🤖 ML Mentor is thinking..."):
            answer = ask_chatbot(user_input)
        st.session_state.chat_history.append(("Bot", answer))
        st.rerun()

    st.markdown("### 💬 Conversation")
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    if not st.session_state.chat_history:
        st.markdown("""
        <div style="text-align:center; color:#999; padding:50px 20px;">
            ML Mentor is ready for your question!
        </div>
        """, unsafe_allow_html=True)
    else:
        for speaker, text in st.session_state.chat_history:
            if speaker == "You":
                st.markdown(f'<div class="user-message"><strong>You:</strong> {text}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-message"><strong>ML Mentor:</strong> {text}</div>',
                            unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Clear chat button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.chat_history = []
        st.rerun()
