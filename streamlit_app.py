import streamlit as st
from auth_utils import (
    get_google_auth_url,
    get_microsoft_auth_url,
    handle_google_callback,
    handle_microsoft_callback,
)
from lessonary_ui import render_lessonary_ui

st.set_page_config(page_title="Lessonary", page_icon="📘", layout="centered")

def handle_callback():
    query_params = st.query_params
    if "code" in query_params:
        provider = st.session_state.get("oauth_provider", "google")
        code = query_params["code"]
        if provider == "google":
            handle_google_callback(code)
        elif provider == "microsoft":
            handle_microsoft_callback(code)
        st.rerun()

handle_callback()

if "user" in st.session_state:
    render_lessonary_ui()
else:
    st.image("assets/lessonary_logo.png", width=200)
    st.title("Login to Lessonary")

    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/google_logo.png", width=40)
        if st.button("Login with Google"):
            st.session_state['oauth_provider'] = 'google'
            st.switch_page(get_google_auth_url())

    with col2:
        st.image("assets/microsoft_logo.png", width=40)
        if st.button("Login with Microsoft"):
            st.session_state['oauth_provider'] = 'microsoft'
            st.switch_page(get_microsoft_auth_url())
