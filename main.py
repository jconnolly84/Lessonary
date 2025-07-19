
import streamlit as st
from auth import check_login

check_login()  # Ensure user is logged in before proceeding

# Main app interface
st.title("🎯 Choose Your Next Step")
option = st.radio("What would you like to do?", [
    "Upload a PowerPoint to uplift",
    "Import from Google Drive or OneDrive",
    "Start a lesson from a Key Objective"
])

if option == "Upload a PowerPoint to uplift":
    st.success("Upload chosen.")
elif option == "Import from Google Drive or OneDrive":
    st.info("Drive integration coming soon.")
else:
    st.warning("Lesson generator coming soon.")
