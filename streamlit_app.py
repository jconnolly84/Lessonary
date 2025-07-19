import streamlit as st
from auth_utils import get_google_login_url, get_ms_login_url

st.set_page_config(page_title="Lessonary Login", page_icon="📘")
st.image("assets/lessonary_logo.png", width=200)
st.title("Login to Lessonary")

# Capture which button was pressed and perform redirect using HTML
if "redirect" not in st.session_state:
    st.session_state["redirect"] = None

if st.button("Login with Google"):
    st.session_state["redirect"] = get_google_login_url()

if st.button("Login with Microsoft"):
    st.session_state["redirect"] = get_ms_login_url()

# Trigger redirect with HTML if redirect URL is set
if st.session_state["redirect"]:
    redirect_script = f"""
    <meta http-equiv="refresh" content="0; url={st.session_state['redirect']}" />
    If you are not redirected, <a href="{st.session_state['redirect']}">click here</a>.
    """
    st.markdown(redirect_script, unsafe_allow_html=True)