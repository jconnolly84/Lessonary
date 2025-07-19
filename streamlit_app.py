
import streamlit as st
from auth_utils import (
    login_with_google,
    login_with_microsoft,
    handle_google_auth_callback,
    handle_microsoft_auth_callback
)

st.set_page_config(
    page_title="Lessonary",
    page_icon="favicon.png"
)

st.image("assets/lessonary_logo.png", width=200)
st.title("Login to Lessonary")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔴 Login with Google"):
        login_with_google()

with col2:
    if st.button("🔵 Login with Microsoft"):
        login_with_microsoft()

handle_google_auth_callback()
handle_microsoft_auth_callback()
