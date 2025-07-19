
import streamlit as st
import webbrowser

try:
    GOOGLE_CLIENT_ID = st.secrets["google_oauth_client_id"]
    GOOGLE_CLIENT_SECRET = st.secrets["google_oauth_client_secret"]
    GOOGLE_REDIRECT_URI = st.secrets["google_oauth_redirect_uri"]
except Exception as e:
    st.error(f"❌ Google secrets missing: {e}")

try:
    MS_CLIENT_ID = st.secrets["ms_client_id"]
    MS_CLIENT_SECRET = st.secrets["ms_client_secret"]
    MS_TENANT_ID = st.secrets["ms_tenant_id"]
    MS_REDIRECT_URI = st.secrets["ms_redirect_uri"]
except Exception as e:
    st.error(f"❌ Microsoft secrets missing: {e}")

def login_with_google():
    auth_url = f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid email profile&access_type=offline&prompt=consent"
    webbrowser.open(auth_url)

def login_with_microsoft():
    auth_url = f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize?client_id={MS_CLIENT_ID}&response_type=code&redirect_uri={MS_REDIRECT_URI}&response_mode=query&scope=openid email profile offline_access&prompt=select_account"
    webbrowser.open(auth_url)

def handle_google_auth_callback():
    st.caption("🔁 Google callback handled")

def handle_microsoft_auth_callback():
    st.caption("🔁 Microsoft callback handled")
