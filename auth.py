
import streamlit as st
from PIL import Image
import os

def login_screen():
    st.title("👋 Welcome to Lessonary")
    st.markdown("Please login to continue.")
    st.header("🔐 Login to Lessonary")

    col1, col2 = st.columns(2)

    with col1:
        if os.path.exists("google_logo.png"):
            st.image("google_logo.png", width=25)
        if st.button("Login with Google", key="google"):
            st.session_state["user"] = "google_user"
            st.success("Logged in with Google")
            st.experimental_rerun()

    with col2:
        if os.path.exists("microsoft_logo.png"):
            st.image("microsoft_logo.png", width=25)
        if st.button("Login with Microsoft", key="microsoft"):
            st.session_state["user"] = "microsoft_user"
            st.success("Logged in with Microsoft")
            st.experimental_rerun()

def check_login():
    if "user" not in st.session_state:
        login_screen()
        st.stop()
