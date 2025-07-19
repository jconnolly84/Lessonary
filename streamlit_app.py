import streamlit as st
from auth_utils import (
    get_google_login_url,
    get_microsoft_login_url,
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
        st.experimental_redirect(get_google_login_url())

with col2:
    if st.button("🔵 Login with Microsoft"):
        st.experimental_redirect(get_microsoft_login_url())

handle_google_auth_callback()
handle_microsoft_auth_callback()