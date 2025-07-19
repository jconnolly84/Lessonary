
import streamlit as st

def login_screen():
    st.markdown("### 🔐 Login to Lessonary")
    login_button_clicked = st.button("Login with Google")
    if login_button_clicked:
        st.session_state["authenticated"] = True
        st.rerun()

def check_login():
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        login_screen()
        st.stop()
