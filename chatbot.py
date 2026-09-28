import streamlit as st
import ollama

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

/* 🌈 Main background */
.stApp {
    background: linear-gradient(135deg, #dff6ff, #e8ddff, #fff1d6);
}

/* 🤖 Main title */
h1 {
    text-align: center;
    color: #4a148c;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 5px;
}

/* 💬 Subtitle */
.subtitle {
    text-align: center;
    color: #5e35b1;
    font-size: 20px;
    font-weight: 500;
}

/* 📦 Input label */
label {
    color: #4a148c !important;
    font-weight: bold !important;
    font-size: 17px !important;
}

/* ✏️ Input box */
.stTextInput input {
    background-color: #ffffff;
    border: 3px solid #7e57c2;
    border-radius: 15px;
    padding: 14px;
    font-size: 16px;
}

/* 🤖 Ask AI button */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #7b1fa2, #3949ab);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 14px;
    font-size: 19px;
    font-weight: bold;
    box-shadow: 0px 5px 12px rgba(0,0,0,0.2);
}

.stButton button:hover {
    background: linear-gradient(90deg, #512da8, #1565c0);
    color: white;
    transform: scale(1.02);
}

/* 💡 Response box */
.response-box {
    background: linear-gradient(135deg, #ffffff, #f3e5f5);
    padding: 25px;
    border-radius: 20px;
    border-left: 7px solid #7b1fa2;
    margin-top: 25px;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
}

/* Response heading */
.response-box h3 {
    color: #6a1b9a;
    font-size: 24px;
}

/* Response text */
.response-box p {
    color: #333333;
    font-size: 17px;
    line-height: 1.6;
}

/* ✨ Divider */
hr {
    border: none;
    height: 2px;
    background: #b39ddb;
}

/* Footer */
.footer {
    text-align: center;
    color: #5e35b1;
    font-size: 14px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.title("🤖 Friendly AI Bot")

st.markdown(
    '<p class="subtitle">✨ Ask me anything and let AI help you! 💡</p>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- QUESTION ----------------

st.markdown("### 💬 Ask Your Question")

question = st.text_input(
    "Enter your question:",
    placeholder="✍️ Type your question here..."
)


# ---------------- ASK AI ----------------

if st.button("🚀 Ask AI"):

    if question:

        with st.spinner("🤖 AI is thinking... 💭"):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        You are a friendly and funny AI assistant.
                        Explain things in simple language.
                        Be helpful and encouraging.
                        """
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = response["message"]["content"]

        # 🤖 AI Response
        st.markdown(
            f"""
            <div class="response-box">
                <h3>🤖 AI Response ✨</h3>
                <p>{answer}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.warning("⚠️ Please enter a question first!")


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    """
    <div class="footer">
        🤖 Friendly AI Bot &nbsp; | &nbsp;
        🧠 Powered by Llama 3.2 &nbsp; | &nbsp;
        💻 Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)