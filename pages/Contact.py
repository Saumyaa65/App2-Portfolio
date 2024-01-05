import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):

    email=st.text_input("Your email address")
    subject=st.text_input("Subject")
    message=st.text_area("Your message")
    button=st.form_submit_button()
    if button:
        send_email(subject, message, email)
        st.info("Email sent successfully")