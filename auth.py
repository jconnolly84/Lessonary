
import streamlit as st
import requests
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from msal import ConfidentialClientApplication

def authenticate_user():
    st.title("🔐 Login to Lessonary")
    st.markdown("Choose a login method to continue.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login with Google"):
            google_auth_url = (
                "https://accounts.google.com/o/oauth2/v2/auth"
                "?response_type=code"
                f"&client_id={st.secrets['google_oauth_client_id']}"
                f"&redirect_uri={st.secrets['google_oauth_redirect_uri']}"
                "&scope=email profile openid https://www.googleapis.com/auth/drive.file"
            )
            st.markdown(f"[Click here to authenticate]({google_auth_url})")

    with col2:
        if st.button("Login with Microsoft"):
            ms_auth_url = (
                f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
                f"?client_id={st.secrets['ms_client_id']}"
                f"&response_type=code"
                f"&redirect_uri={st.secrets['ms_redirect_uri']}"
                f"&response_mode=query"
                f"&scope=openid profile User.Read Files.ReadWrite.All"
            )
            st.markdown(f"[Click here to authenticate]({ms_auth_url})")

def handle_google_auth():
    params = st.query_params
    if "code" in params:
        code = params["code"][0]

        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": st.secrets["google_oauth_client_id"],
            "client_secret": st.secrets["google_oauth_client_secret"],
            "redirect_uri": st.secrets["google_oauth_redirect_uri"],
            "grant_type": "authorization_code",
        }

        response = requests.post(token_url, data=data)
        token_data = response.json()

        try:
            idinfo = id_token.verify_oauth2_token(
                token_data["id_token"],
                google_requests.Request(),
                st.secrets["google_oauth_client_id"]
            )

            st.session_state["user"] = {
                "name": idinfo["name"],
                "email": idinfo["email"],
                "provider": "Google",
                "access_token": token_data["access_token"],
                "refresh_token": token_data.get("refresh_token", None),
            }
            st.success(f"✅ Logged in as {idinfo['email']}")
        except Exception as e:
            st.error("Google authentication failed.")
            st.exception(e)

def handle_ms_auth():
    params = st.query_params
    if "code" in params:
        code = params["code"][0]

        app = ConfidentialClientApplication(
            st.secrets["ms_client_id"],
            authority=f"https://login.microsoftonline.com/{st.secrets['ms_tenant_id']}",
            client_credential=st.secrets["ms_client_secret"]
        )

        result = app.acquire_token_by_authorization_code(
            code,
            scopes=["User.Read", "Files.ReadWrite.All"],
            redirect_uri=st.secrets["ms_redirect_uri"]
        )

        if "id_token_claims" in result:
            st.session_state["user"] = {
                "name": result["id_token_claims"].get("name", "User"),
                "email": result["id_token_claims"].get("preferred_username"),
                "provider": "Microsoft",
                "access_token": result["access_token"]
            }
            st.success(f"✅ Logged in as {result['id_token_claims']['preferred_username']}")
        else:
            st.error("Microsoft authentication failed.")
            st.json(result)
