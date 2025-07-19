
import toml
import streamlit as st
import urllib.parse

# Load secrets manually from /etc/secrets/secrets.toml
secrets = toml.load("/etc/secrets/secrets.toml")

GOOGLE_CLIENT_ID = secrets["google_oauth_client_id"]
GOOGLE_CLIENT_SECRET = secrets["google_oauth_client_secret"]
GOOGLE_REDIRECT_URI = secrets["google_oauth_redirect_uri"]

MS_CLIENT_ID = secrets["ms_client_id"]
MS_CLIENT_SECRET = secrets["ms_client_secret"]
MS_TENANT_ID = secrets["ms_tenant_id"]
MS_REDIRECT_URI = secrets["ms_redirect_uri"]

OPENAI_API_KEY = secrets["OPENAI_API_KEY"]
PIXABAY_API_KEY = secrets["PIXABAY_API_KEY"]
PEXELS_API_KEY = secrets["PEXELS_API_KEY"]
GOOGLE_API_KEY = secrets["google_api_key"]
GOOGLE_CSE_ID = secrets["google_cse_id"]

def login_with_google():
    auth_url = (
        f"https://accounts.google.com/o/oauth2/auth"
        f"?response_type=code"
        f"&client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={urllib.parse.quote(GOOGLE_REDIRECT_URI, safe='')}"
        f"&scope=openid email profile"
        f"&access_type=offline"
        f"&prompt=consent"
    )
    st.markdown(f"[Click here to login with Google]({auth_url})", unsafe_allow_html=True)

def login_with_microsoft():
    auth_url = (
        f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize"
        f"?client_id={MS_CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={urllib.parse.quote(MS_REDIRECT_URI, safe='')}"
        f"&response_mode=query"
        f"&scope=openid email profile offline_access"
        f"&prompt=select_account"
    )
    st.markdown(f"[Click here to login with Microsoft]({auth_url})", unsafe_allow_html=True)
