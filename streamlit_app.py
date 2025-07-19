
import streamlit as st
from auth_utils import (
    login_with_google,
    login_with_microsoft,
    handle_callback,
)
from lessonary_ui import render_lessonary_ui

# Break out of iframe sandbox (needed for Google/Microsoft auth to work properly)
st.components.v1.html(
    """
    <script>
        if (window.top !== window.self) {
            window.top.location = window.location.href;
        }
    </script>
    """,
    height=0,
)

st.set_page_config(page_title="Lessonary", page_icon="📘", layout="centered")

handle_callback()

if "user_info" in st.session_state:
    render_lessonary_ui()
else:
    st.image("assets/lessonary_logo.png", width=200)
    st.title("Login to Lessonary")

    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/google_logo.png", width=40)
        if st.button("Login with Google"):
            login_with_google()

    with col2:
        st.image("assets/microsoft_logo.png", width=40)
        if st.button("Login with Microsoft"):
            login_with_microsoft()
