
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

if st.button("Login with Google"):
    login_with_google()
    st.experimental_rerun()

if st.button("Login with Microsoft"):
    login_with_microsoft()
    st.experimental_rerun()

# Callback handler (if redirected back with code)
handle_google_auth_callback()
handle_microsoft_auth_callback()
