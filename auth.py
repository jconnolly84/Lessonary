
import streamlit as st
from PIL import Image

def check_login():
    if "user" not in st.session_state:
        login_screen()
        st.stop()

def login_screen():
    st.image("LOGO_Lessonary.png", width=250)
    st.title("👋 Welcome to Lessonary")
    st.subheader("🔐 Login to Lessonary")
    st.write("Please login to continue.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login with Google"):
            st.session_state["user"] = "google_user"

    with col2:
        if st.button("Login with Microsoft"):
            st.session_state["user"] = "microsoft_user"

    st.stop()
