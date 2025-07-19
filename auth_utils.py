
import streamlit as st
import webbrowser

GOOGLE_CLIENT_ID = st.secrets.get("google_oauth_client_id", "")
GOOGLE_CLIENT_SECRET = st.secrets.get("google_oauth_client_secret", "")
GOOGLE_REDIRECT_URI = st.secrets.get("google_oauth_redirect_uri", "")

MS_CLIENT_ID = st.secrets.get("ms_client_id", "")
MS_CLIENT_SECRET = st.secrets.get("ms_client_secret", "")
MS_TENANT_ID = st.secrets.get("ms_tenant_id", "")
MS_REDIRECT_URI = st.secrets.get("ms_redirect_uri", "")

def login_with_google():
    if GOOGLE_CLIENT_ID and GOOGLE_REDIRECT_URI:
        auth_url = f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid email profile&access_type=offline&prompt=consent"
        webbrowser.open(auth_url)
    else:
        st.error("Google login not configured correctly.")

def login_with_microsoft():
    if MS_CLIENT_ID and MS_REDIRECT_URI and MS_TENANT_ID:
        auth_url = f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize?client_id={MS_CLIENT_ID}&response_type=code&redirect_uri={MS_REDIRECT_URI}&response_mode=query&scope=openid email profile offline_access&prompt=select_account"
        webbrowser.open(auth_url)
    else:
        st.error("Microsoft login not configured correctly.")

def handle_google_auth_callback():
    st.caption("🔁 Google callback handled")

def handle_microsoft_auth_callback():
    st.caption("🔁 Microsoft callback handled")
