
import os
import streamlit as st

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")

MS_CLIENT_ID = os.getenv("MS_CLIENT_ID")
MS_CLIENT_SECRET = os.getenv("MS_CLIENT_SECRET")
MS_TENANT_ID = os.getenv("MS_TENANT_ID")
MS_REDIRECT_URI = os.getenv("MS_REDIRECT_URI")

def login_with_google():
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth?"
        f"response_type=code&client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={GOOGLE_REDIRECT_URI}"
        "&scope=openid email profile&access_type=offline&prompt=consent"
    )
    st.markdown(f"[Click here to login with Google]({auth_url})")

def login_with_microsoft():
    auth_url = (
        f"https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize?"
        f"client_id={MS_CLIENT_ID}&response_type=code&redirect_uri={MS_REDIRECT_URI}"
        "&response_mode=query&scope=openid email profile offline_access&prompt=select_account"
    )
    st.markdown(f"[Click here to login with Microsoft]({auth_url})")
