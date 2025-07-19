
import os
import streamlit as st
import webbrowser
from urllib.parse import urlencode

# Environment variables
GOOGLE_CLIENT_ID = os.environ.get("google_oauth_client_id", "")
GOOGLE_CLIENT_SECRET = os.environ.get("google_oauth_client_secret", "")
GOOGLE_REDIRECT_URI = os.environ.get("google_oauth_redirect_uri", "")
MS_CLIENT_ID = os.environ.get("ms_client_id", "")
MS_CLIENT_SECRET = os.environ.get("ms_client_secret", "")
MS_TENANT_ID = os.environ.get("ms_tenant_id", "")
MS_REDIRECT_URI = os.environ.get("ms_redirect_uri", "")

def login_with_google():
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth?"
        + urlencode({
            "response_type": "code",
            "client_id": GOOGLE_CLIENT_ID,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent"
        })
    )
    st.markdown(f"[Click here to complete Google login]({auth_url})")

def login_with_microsoft():
    auth_url = (
        f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize?"
        + urlencode({
            "client_id": MS_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": MS_REDIRECT_URI,
            "response_mode": "query",
            "scope": "openid email profile offline_access",
            "prompt": "select_account"
        })
    )
    st.markdown(f"[Click here to complete Microsoft login]({auth_url})")

def handle_google_auth_callback():
    if "code" in st.query_params:
        st.success("Google login successful! (Simulated)")

def handle_microsoft_auth_callback():
    if "code" in st.query_params:
        st.success("Microsoft login successful! (Simulated)")
