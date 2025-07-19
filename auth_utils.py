
import streamlit as st
from requests_oauthlib import OAuth2Session

GOOGLE_CLIENT_ID = st.secrets["google_oauth_client_id"]
GOOGLE_CLIENT_SECRET = st.secrets["google_oauth_client_secret"]
GOOGLE_REDIRECT_URI = "https://less-onary.streamlit.app"
GOOGLE_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_SCOPE = ['openid', 'email', 'profile']

MS_CLIENT_ID = st.secrets["ms_client_id"]
MS_CLIENT_SECRET = st.secrets["ms_client_secret"]
MS_TENANT_ID = st.secrets["ms_tenant_id"]
MS_REDIRECT_URI = GOOGLE_REDIRECT_URI
MS_AUTH_URI = f'https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/authorize'
MS_SCOPE = ['User.Read']

def get_google_auth_url():
    google = OAuth2Session(GOOGLE_CLIENT_ID, scope=GOOGLE_SCOPE, redirect_uri=GOOGLE_REDIRECT_URI)
    auth_url, _ = google.authorization_url(GOOGLE_AUTH_URI, access_type='offline', prompt='consent')
    return auth_url

def get_microsoft_auth_url():
    ms = OAuth2Session(MS_CLIENT_ID, scope=MS_SCOPE, redirect_uri=MS_REDIRECT_URI)
    auth_url, _ = ms.authorization_url(MS_AUTH_URI, response_mode='query')
    return auth_url

def handle_google_callback(code):
    google = OAuth2Session(GOOGLE_CLIENT_ID, redirect_uri=GOOGLE_REDIRECT_URI)
    token = google.fetch_token(
        'https://oauth2.googleapis.com/token',
        client_secret=GOOGLE_CLIENT_SECRET,
        code=code
    )
    user_info = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    st.session_state['user_info'] = user_info
    st.session_state['token'] = token
    st.session_state['auth_provider'] = 'google'

def handle_microsoft_callback(code):
    ms = OAuth2Session(MS_CLIENT_ID, redirect_uri=MS_REDIRECT_URI)
    token = ms.fetch_token(
        f'https://login.microsoftonline.com/{MS_TENANT_ID}/oauth2/v2.0/token',
        client_secret=MS_CLIENT_SECRET,
        code=code
    )
    user_info = ms.get('https://graph.microsoft.com/v1.0/me').json()
    st.session_state['user_info'] = user_info
    st.session_state['token'] = token
    st.session_state['auth_provider'] = 'microsoft'

def login_with_google():
    st.session_state['auth_provider'] = 'google'
    auth_url = get_google_auth_url()
    st.session_state['auth_url'] = auth_url
    st.experimental_rerun()

def login_with_microsoft():
    st.session_state['auth_provider'] = 'microsoft'
    auth_url = get_microsoft_auth_url()
    st.session_state['auth_url'] = auth_url
    st.experimental_rerun()

def handle_callback():
    query_params = st.experimental_get_query_params()
    if 'code' in query_params:
        code = query_params['code'][0]
        if st.session_state.get('auth_provider') == 'google':
            handle_google_callback(code)
        elif st.session_state.get('auth_provider') == 'microsoft':
            handle_microsoft_callback(code)
