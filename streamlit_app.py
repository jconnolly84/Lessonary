import streamlit as st
from auth_utils import (
    login_with_google,
    login_with_microsoft,
    handle_google_auth_callback,
    handle_microsoft_auth_callback
)

# Show branding
st.image("assets/lessonary_logo.png", width=200)
st.title("Login to Lessonary")

# Google login
if st.button("Login with Google", key="login_google"):
    auth_url = login_with_google()
    st.markdown(f"<meta http-equiv='refresh' content='0; url={auth_url}'>", unsafe_allow_html=True)

# Microsoft login
if st.button("Login with Microsoft", key="login_microsoft"):
    auth_url = login_with_microsoft()
    st.markdown(f"<meta http-equiv='refresh' content='0; url={auth_url}'>", unsafe_allow_html=True)

# Handle callbacks from providers
handle_google_auth_callback()
handle_microsoft_auth_callback()