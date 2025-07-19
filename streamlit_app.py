
import streamlit as st
from auth_utils import (
    get_google_auth_url,
    get_microsoft_auth_url,
    handle_google_callback,
    handle_microsoft_callback
)

def show_login():
    st.title("Login to Lessonary")
    st.write("👋 Welcome! Please log in to start creating or uplifting a lesson.")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("Login with Google", get_google_auth_url())
    with col2:
        st.link_button("Login with Microsoft", get_microsoft_auth_url())

def lesson_options():
    user = st.session_state.get('user', {})
    name = user.get("name", "there")
    picture = user.get("picture")

    st.title(f"Welcome, {name} 👋")

    if picture:
        st.image(picture, width=100)

    st.subheader("How would you like to create your lesson?")
    option = st.radio(
        "Select input method:",
        ("Upload PowerPoint file", "Import from Google Drive", "Import from OneDrive", "Enter Key Objective")
    )

    if option == "Upload PowerPoint file":
        uploaded_file = st.file_uploader("Upload PPT/PPTX file", type=['ppt', 'pptx'])
        if uploaded_file:
            st.success(f"Uploaded {uploaded_file.name}")
    elif option == "Import from Google Drive":
        st.info("🚧 Coming soon: Import from Google Drive.")
    elif option == "Import from OneDrive":
        st.info("🚧 Coming soon: Import from OneDrive.")
    elif option == "Enter Key Objective":
        key_objective = st.text_input("Enter Key Objective")
        if key_objective:
            st.success(f"📘 Building lesson for: {key_objective}")

def handle_callback():
    query_params = st.query_params
    if 'code' in query_params:
        provider = st.session_state.get('oauth_provider', 'google')
        code = query_params['code']
        if provider == 'google':
            handle_google_callback(code)
        elif provider == 'microsoft':
            handle_microsoft_callback(code)
        st.rerun()

if __name__ == "__main__":
    if 'user' in st.session_state:
        lesson_options()
    elif 'code' in st.query_params:
        handle_callback()
    else:
        show_login()
