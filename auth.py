import streamlit as st
import extra_streamlit_components as stx
from urllib.parse import urlencode
import base64

def login_screen():
    st.markdown("## 🔐 Login to Lessonary")
    
    st.image("LOGO_Lessonary_Enhanced.png", width=200)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login with Google"):
            google_auth_url = (
                "https://accounts.google.com/o/oauth2/v2/auth?"
                + urlencode({
                    "client_id": st.secrets.google_oauth_client_id,
                    "redirect_uri": st.secrets.google_oauth_redirect_uri,
                    "response_type": "code",
                    "scope": "openid email profile",
                    "access_type": "offline",
                    "prompt": "consent"
                })
            )
            st.markdown(f'<meta http-equiv="refresh" content="0;URL='{google_auth_url}'" />', unsafe_allow_html=True)
    
    with col2:
        if st.button("Login with Microsoft"):
            microsoft_auth_url = (
                f"https://login.microsoftonline.com/{st.secrets.ms_tenant_id}/oauth2/v2.0/authorize?"
                + urlencode({
                    "client_id": st.secrets.ms_client_id,
                    "response_type": "code",
                    "redirect_uri": st.secrets.ms_redirect_uri,
                    "response_mode": "query",
                    "scope": "openid profile email offline_access User.Read"
                })
            )
            st.markdown(f'<meta http-equiv="refresh" content="0;URL='{microsoft_auth_url}'" />', unsafe_allow_html=True)

def check_login():
    if "user" not in st.session_state:
        login_screen()
        st.stop()