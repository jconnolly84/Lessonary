import streamlit as st
from auth_utils import get_google_login_url, get_microsoft_login_url

st.set_page_config(page_title="Lessonary", page_icon="📘")

st.image("assets/lessonary_logo.png", width=200)
st.title("Welcome to Lessonary")

# Google login
google_url = get_google_login_url()
if st.button("Login with Google") and google_url:
    st.markdown(f'<meta http-equiv="refresh" content="0;URL={google_url}">', unsafe_allow_html=True)

# Microsoft login
ms_url = get_microsoft_login_url()
if st.button("Login with Microsoft") and ms_url:
    st.markdown(f'<meta http-equiv="refresh" content="0;URL={ms_url}">', unsafe_allow_html=True)
