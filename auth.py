
import streamlit as st
import urllib.parse

def login_screen():
    st.image("LOGO_Lessonary_Enhanced.png", width=250)
    st.title("👋 Welcome to Lessonary")
    st.subheader("🔐 Please log in")

    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        + urllib.parse.urlencode({
            'client_id': st.secrets.google_oauth_client_id,
            'redirect_uri': st.secrets.google_oauth_redirect_uri,
            'response_type': 'code',
            'scope': 'openid email profile',
            'access_type': 'offline',
            'prompt': 'consent'
        })
    )

    microsoft_auth_url = (
        f"https://login.microsoftonline.com/{st.secrets.ms_tenant_id}/oauth2/v2.0/authorize?"
        + urllib.parse.urlencode({
            'client_id': st.secrets.ms_client_id,
            'response_type': 'code',
            'redirect_uri': st.secrets.ms_redirect_uri,
            'response_mode': 'query',
            'scope': 'openid profile email offline_access',
        })
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'''
            <a href="{google_auth_url}" target="_self">
                <button style="padding:10px;border:none;background-color:#fff;border-radius:5px;">
                    <img src="google_logo.png" width="24" style="vertical-align:middle;margin-right:10px;">Login with Google
                </button>
            </a>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown(f'''
            <a href="{microsoft_auth_url}" target="_self">
                <button style="padding:10px;border:none;background-color:#fff;border-radius:5px;">
                    <img src="microsoft_logo.png" width="24" style="vertical-align:middle;margin-right:10px;">Login with Microsoft
                </button>
            </a>
        ''', unsafe_allow_html=True)

    st.stop()

def check_login():
    if "user" not in st.session_state:
        login_screen()
