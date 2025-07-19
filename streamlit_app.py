
import streamlit as st
from auth_utils import (
    login_with_google,
    login_with_microsoft,
    handle_google_auth_callback,
    handle_microsoft_auth_callback
)

# Always show the login screen for testing
st.image("assets/lessonary_logo.png", width=200)
st.title("Login to Lessonary")

if st.button("Login with Google", key="login_google"):
    login_with_google()
    st.rerun()

if st.button("Login with Microsoft", key="login_microsoft"):
    login_with_microsoft()
    st.rerun()

# Callback handler (if redirected back with code)
handle_google_auth_callback()
handle_microsoft_auth_callback()
