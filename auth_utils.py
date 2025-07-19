
import streamlit as st
import urllib.parse

GOOGLE_CLIENT_ID = st.secrets["google_oauth_client_id"]
GOOGLE_CLIENT_SECRET = st.secrets["google_oauth_client_secret"]
GOOGLE_REDIRECT_URI = st.secrets["google_oauth_redirect_uri"]

MS_CLIENT_ID = st.secrets["ms_client_id"]
MS_CLIENT_SECRET = st.secrets["ms_client_secret"]
MS_TENANT_ID = st.secrets["ms_tenant_id"]
MS_REDIRECT_URI = st.secrets["ms_redirect_uri"]

def login_with_google():
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={urllib.parse.quote(GOOGLE_CLIENT_ID)}"
        f"&redirect_uri={urllib.parse.quote(GOOGLE_REDIRECT_URI)}"
        "&scope=openid email profile"
        "&access_type=offline&prompt=consent"
    )
    st.markdown(f"[Click here to login with Google]({auth_url})")

def login_with_microsoft():
    auth_url = (
        f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize"
        f"?client_id={MS_CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={urllib.parse.quote(MS_REDIRECT_URI)}"
        "&response_mode=query"
        "&scope=openid email profile offline_access"
        "&prompt=select_account"
    )
    st.markdown(f"[Click here to login with Microsoft]({auth_url})")
