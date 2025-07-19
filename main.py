
import streamlit as st
from auth_real_oauth import check_login

check_login()

st.success("✅ You are logged in!")

st.title("🎯 Choose Your Next Step")

option = st.radio("What would you like to do?", [
    "Upload a PowerPoint to uplift",
    "Import from Google Drive or OneDrive",
    "Start a lesson from a Key Objective"
])

if option == "Upload a PowerPoint to uplift":
    st.info("You selected: Upload a PowerPoint.")
elif option == "Import from Google Drive or OneDrive":
    st.info("You selected: Import from Drive.")
else:
    st.info("You selected: Start from a Key Objective.")
