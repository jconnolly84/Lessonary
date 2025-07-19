
import streamlit as st
from auth import authenticate_user, handle_google_auth, handle_ms_auth

handle_google_auth()
handle_ms_auth()

if "user" not in st.session_state:
    user = authenticate_user()
    st.stop()

user = st.session_state["user"]
st.success(f"Welcome {user['name']} ({user['email']})")

# App will continue from here...
