import streamlit as st
from auth_utils import (
    login_with_google,
    login_with_microsoft,
    handle_google_auth_callback,
    handle_microsoft_auth_callback,
)

st.set_page_config(page_title="Lessonary Login", page_icon="📘", layout="centered")

st.image("assets/lessonary_logo.png", width=150)
st.title("Login to Lessonary")

# Show login buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("🔴 Login with Google", key="google_btn"):
        login_with_google()
with col2:
    if st.button("🔵 Login with Microsoft", key="ms_btn"):
        login_with_microsoft()

# Auth callbacks (if redirected back)
handle_google_auth_callback()
handle_microsoft_auth_callback()
