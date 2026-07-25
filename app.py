import streamlit as st

from src.config import APP_TITLE
from src.gemini_client import generate_response

if "history" not in st.session_state:
    st.session_state.history = []


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏦",
    layout="centered"
)

st.title(APP_TITLE)
st.write("Ask any banking policy question.")

question = st.text_area(
    "Your Question",
    placeholder="Example: What is KYC?"
)

if st.button("Ask Gemini"):
    if question.strip():

        try:
            with st.spinner("Thinking..."):
                answer = generate_response(question)

            st.subheader("Response")
            st.write(answer)

            st.session_state.history.append(
                {
                    "question": question,
                    "answer": answer,
                }
)

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.warning("Please enter a question.")

if st.session_state.history:

    st.divider()
    st.subheader("Conversation History")

    for chat in reversed(st.session_state.history):

        st.markdown(f"**You:** {chat['question']}")
        st.markdown(f"**Assistant:** {chat['answer']}")