import os
import streamlit as st
import webbrowser

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.environ.get("GOOGLE_OAUTH_REDIRECT_URI")

MS_CLIENT_ID = os.environ.get("MS_CLIENT_ID")
MS_CLIENT_SECRET = os.environ.get("MS_CLIENT_SECRET")
MS_REDIRECT_URI = os.environ.get("MS_REDIRECT_URI")
MS_TENANT_ID = os.environ.get("MS_TENANT_ID")

def get_google_login_url():
    if not GOOGLE_CLIENT_ID or not GOOGLE_REDIRECT_URI:
        return None

    return (
        f"https://accounts.google.com/o/oauth2/auth"
        f"?response_type=code"
        f"&client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={GOOGLE_REDIRECT_URI}"
        f"&scope=openid email profile"
        f"&access_type=offline"
        f"&prompt=consent"
    )

def get_microsoft_login_url():
    if not MS_CLIENT_ID or not MS_TENANT_ID or not MS_REDIRECT_URI:
        return None

    return (
        f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize"
        f"?client_id={MS_CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={MS_REDIRECT_URI}"
        f"&response_mode=query"
        f"&scope=openid email profile offline_access"
        f"&prompt=select_account"
    )
