
import streamlit as st

def login_with_google():
    # Simulate successful login with Google
    st.session_state["user"] = {"name": "Google User", "email": "google_user@example.com"}

def login_with_microsoft():
    # Simulate successful login with Microsoft
    st.session_state["user"] = {"name": "Microsoft User", "email": "ms_user@example.com"}

def login_screen():
    st.image("LOGO_Lessonary.png", width=200)
    st.markdown("## 👋 Welcome to Lessonary")
    st.write("Please login to continue.")
    st.markdown("### 🔐 Login to Lessonary")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login with Google"):
            login_with_google()
            st.experimental_rerun()
    with col2:
        if st.button("Login with Microsoft"):
            login_with_microsoft()
            st.experimental_rerun()

def check_login():
    if "user" not in st.session_state:
        login_screen()
        st.stop()
