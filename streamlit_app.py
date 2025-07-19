
import streamlit as st

st.caption("🐛 Starting app...")

try:
    from auth_utils import (
        login_with_google,
        login_with_microsoft,
        handle_google_auth_callback,
        handle_microsoft_auth_callback
    )
    st.caption("✅ auth_utils.py loaded successfully")
except Exception as e:
    st.error(f"❌ Failed to load auth_utils: {e}")

# Always show the login screen for testing
st.image("assets/lessonary_logo.png", width=200)
st.title("Login to Lessonary")

if st.button("Login with Google", key="login_google"):
    login_with_google()
    st.experimental_rerun()

if st.button("Login with Microsoft", key="login_microsoft"):
    login_with_microsoft()
    st.experimental_rerun()

# Callback handler (if redirected back with code)
try:
    handle_google_auth_callback()
    handle_microsoft_auth_callback()
except Exception as e:
    st.error(f"❌ Callback error: {e}")
