
import streamlit as st
from auth_utils import (
    login_with_google,
    login_with_microsoft,
    handle_google_auth_callback,
    handle_microsoft_auth_callback
)

st.set_page_config(
    page_title="Lessonary Login",
    page_icon="favicon.png",
    layout="centered"
)

st.image("assets/lessonary_logo.png", width=200)
st.title("Login to Lessonary")

if st.button("Login with Google", key="login_google"):
    login_with_google()

if st.button("Login with Microsoft", key="login_microsoft"):
    login_with_microsoft()

handle_google_auth_callback()
handle_microsoft_auth_callback()
