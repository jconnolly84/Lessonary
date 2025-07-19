import streamlit as st
import time

def login_screen():
    st.subheader("🔐 Login to Lessonary")
    st.image("google_logo.png", width=40)
    if st.button("Login with Google"):
        st.session_state.logged_in = True
        st.session_state.login_method = "google"
        st.success("Login successful! Redirecting...")
        time.sleep(0.5)
        st.experimental_rerun()

def check_login():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        login_screen()
        st.stop()