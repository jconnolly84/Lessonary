
import streamlit as st

def login_screen():
    st.image("LOGO_Lessonary.png", width=250)
    st.title("👋 Welcome to Lessonary")
    st.subheader("🔐 Login to continue")

    col1, col2 = st.columns(2)

    with col1:
        st.image("google_logo.png", width=30)
        if st.button("Login with Google"):
            st.session_state['user'] = 'google_user'
            st.rerun()

    with col2:
        st.image("microsoft_logo.png", width=30)
        if st.button("Login with Microsoft"):
            st.session_state['user'] = 'microsoft_user'
            st.rerun()

def check_login():
    if 'user' not in st.session_state:
        login_screen()
        st.stop()
