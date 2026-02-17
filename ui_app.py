import streamlit as st
from abh_app.agents.diff_agent import detect_bug_line
from abh_app.agents.explanation_agent import generate_explanation

st.set_page_config(page_title="Agentic Bug Hunter", layout="wide")

st.title("🐞 Agentic Bug Hunter")
st.markdown("Detects C++ bugs, identifies error type, and explains them using MCP-powered retrieval.")

st.divider()

st.subheader("Paste Incorrect Code")
incorrect_code = st.text_area("Incorrect Code", height=200)

st.subheader("Paste Correct Code")
correct_code = st.text_area("Correct Code", height=200)

if st.button("🔍 Detect Bug"):

    if not incorrect_code or not correct_code:
        st.warning("Please paste both incorrect and correct code.")
    else:
        bug_line = detect_bug_line(incorrect_code, correct_code)

        explanation = generate_explanation(
            incorrect_code,
            correct_code,
            bug_line
        )

        st.success(f"Bug Detected at Line: {bug_line}")

        st.subheader("📖 Detailed Explanation")
        st.text_area("Explanation", explanation, height=350)

st.divider()

st.caption("Powered by MCP + Vector Retrieval + Rule-Based Bug Classification")
