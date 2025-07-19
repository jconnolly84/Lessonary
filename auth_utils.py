
import streamlit as st
from requests_oauthlib import OAuth2Session

GOOGLE_CLIENT_ID = st.secrets["google_oauth_client_id"]
GOOGLE_CLIENT_SECRET = st.secrets["google_oauth_client_secret"]
GOOGLE_REDIRECT_URI = st.secrets["google_oauth_redirect_uri"]
GOOGLE_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URI = 'https://oauth2.googleapis.com/token'
GOOGLE_SCOPE = ['openid', 'email', 'profile']

MS_CLIENT_ID = st.secrets["ms_client_id"]
MS_CLIENT_SECRET = st.secrets["ms_client_secret"]
MS_TENANT_ID = st.secrets["ms_tenant_id"]
MS_REDIRECT_URI = GOOGLE_REDIRECT_URI
MS_AUTH_URI = f'https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize'
MS_TOKEN_URI = f'https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/token'
MS_SCOPE = ['User.Read']

def login_with_google():
    google = OAuth2Session(GOOGLE_CLIENT_ID, scope=GOOGLE_SCOPE, redirect_uri=GOOGLE_REDIRECT_URI)
    auth_url, _ = google.authorization_url(GOOGLE_AUTH_URI, access_type='offline', prompt='consent')
    st.session_state['oauth_provider'] = 'google'
    st.switch_page(auth_url)

def login_with_microsoft():
    ms = OAuth2Session(MS_CLIENT_ID, scope=MS_SCOPE, redirect_uri=MS_REDIRECT_URI)
    auth_url, _ = ms.authorization_url(MS_AUTH_URI, response_mode='query')
    st.session_state['oauth_provider'] = 'microsoft'
    st.switch_page(auth_url)

def handle_oauth_callback():
    provider = st.session_state.get('oauth_provider', None)
    if provider == 'google':
        oauth_session = OAuth2Session(GOOGLE_CLIENT_ID, redirect_uri=GOOGLE_REDIRECT_URI)
        token = oauth_session.fetch_token(
            GOOGLE_TOKEN_URI,
            client_secret=GOOGLE_CLIENT_SECRET,
            authorization_response=st.query_params
        )
        user_info = oauth_session.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    elif provider == 'microsoft':
        oauth_session = OAuth2Session(MS_CLIENT_ID, redirect_uri=MS_REDIRECT_URI)
        token = oauth_session.fetch_token(
            MS_TOKEN_URI,
            client_secret=MS_CLIENT_SECRET,
            authorization_response=st.query_params
        )
        user_info = oauth_session.get('https://graph.microsoft.com/v1.0/me').json()
    else:
        st.error("No OAuth provider found.")
        return

    st.session_state['user'] = user_info
    st.session_state['token'] = token
