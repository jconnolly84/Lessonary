
import streamlit as st
from auth import check_login

def main():
    st.title("🎯 Choose Your Next Step")

    choice = st.radio("What would you like to do?", [
        "Upload a PowerPoint to uplift",
        "Import from Google Drive or OneDrive",
        "Start a lesson from a Key Objective"
    ])

    st.info(f"You selected: {choice}")

check_login()
main()
