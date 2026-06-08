import streamlit as st
from src.main import generate_email

st.set_page_config(page_title="AI Email Generator", page_icon="✉️", layout="centered")

st.title("AI Email Generator")
st.write("Enter the email subject, audience, and tone, then click generate.")

subject = st.text_input("Subject", placeholder="Product launch, meeting follow-up, job offer, etc.")
audience = st.text_input("Audience", placeholder="Customer, manager, investor, team, etc.")
tone = st.selectbox("Tone", ["Professional", "Friendly", "Formal", "Casual", "Persuasive"])

if st.button("Generate Email"):
    if not subject.strip() or not audience.strip():
        st.warning("Please enter both a subject and an audience.")
    else:
        with st.spinner("Generating your email..."):
            email_text = generate_email(subject, audience, tone)
        st.success("Email generated!")
        st.text_area("Generated Email", email_text, height=300)

st.markdown(
    "---\n"
    "Built with Ollama and Streamlit. Use this app to generate email drafts from a prompt."
)
