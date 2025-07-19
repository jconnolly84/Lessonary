import streamlit as st
import os
from urllib.parse import urlencode
from urllib.parse import parse_qs, urlparse
import requests

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "")

MS_CLIENT_ID = os.getenv("MS_CLIENT_ID", "")
MS_CLIENT_SECRET = os.getenv("MS_CLIENT_SECRET", "")
MS_TENANT_ID = os.getenv("MS_TENANT_ID", "")
MS_REDIRECT_URI = os.getenv("MS_REDIRECT_URI", "")

def login_with_google():
    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        + urlencode({
            "response_type": "code",
            "client_id": GOOGLE_CLIENT_ID,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent"
        })
    )
    return auth_url

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
    return auth_url

def handle_google_auth_callback():
    query_params = st.query_params
    if "code" in query_params:
        code = query_params["code"]
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "redirect_uri": GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code"
        }
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            st.success("Google login successful!")
        else:
            st.error("Google login failed.")

def handle_microsoft_auth_callback():
    query_params = st.query_params
    if "code" in query_params:
        code = query_params["code"]
        token_url = f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/token"
        data = {
            "client_id": MS_CLIENT_ID,
            "scope": "openid email profile offline_access",
            "code": code,
            "redirect_uri": MS_REDIRECT_URI,
            "grant_type": "authorization_code",
            "client_secret": MS_CLIENT_SECRET
        }
        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            st.success("Microsoft login successful!")
        else:
            st.error("Microsoft login failed.")