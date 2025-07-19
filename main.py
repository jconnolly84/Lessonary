
import streamlit as st
from auth_utils import login_with_google, login_with_microsoft, handle_oauth_callback

def show_login():
    st.title("Login to Lessonary")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login with Google"):
            login_with_google()
    with col2:
        if st.button("Login with Microsoft"):
            login_with_microsoft()

def main_dashboard():
    user = st.session_state.get('user', {})
    st.write(f"Welcome, {user.get('name', user.get('email', 'User'))}!")
    # Main Lessonary dashboard here...

if __name__ == "__main__":
    if 'user' in st.session_state:
        main_dashboard()
    elif 'code' in st.query_params:
        handle_oauth_callback()
        st.rerun()
    else:
        show_login()
