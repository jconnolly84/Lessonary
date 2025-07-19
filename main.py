
import streamlit as st
from auth import check_login

# Ensure user is logged in before proceeding
check_login()

st.markdown("### 🎯 Choose Your Next Step")
st.radio("What would you like to do?", [
    "Upload a PowerPoint to uplift",
    "Import from Google Drive or OneDrive",
    "Start a lesson from a Key Objective"
], key="lesson_choice")

if st.session_state.lesson_choice:
    st.info(f"You selected: {st.session_state.lesson_choice}")
