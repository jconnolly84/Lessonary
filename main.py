import streamlit as st
from auth import check_login

check_login()  # Ensure user is logged in

st.success(f"✅ Logged in as: {st.session_state.get('login_method', 'user')}")

st.header("🎯 Choose Your Next Step")
option = st.radio("What would you like to do?", [
    "Upload a PowerPoint to uplift",
    "Import from Google Drive or OneDrive",
    "Start a lesson from a Key Objective"
])

st.info(f"You selected: {option}")