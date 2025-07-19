
import streamlit as st
from auth_utils import (
    get_google_auth_url,
    get_microsoft_auth_url,
    handle_google_callback,
    handle_microsoft_callback
)

def show_login():
    st.title("Login to Lessonary")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("Login with Google", get_google_auth_url())
    with col2:
        st.link_button("Login with Microsoft", get_microsoft_auth_url())

def lesson_options():
    st.title("Welcome to Lessonary")
    st.write("👤 Logged in user:", st.session_state.get('user'))
    st.write("Choose how you'd like to create your lesson:")
    option = st.radio(
        "Select input method:",
        ("Upload PowerPoint file", "Import from Google Drive", "Import from OneDrive", "Enter Key Objective")
    )
    if option == "Upload PowerPoint file":
        uploaded_file = st.file_uploader("Upload PPT/PPTX file", type=['ppt', 'pptx'])
        if uploaded_file:
            st.success(f"Uploaded {uploaded_file.name}")
    elif option == "Import from Google Drive":
        st.info("Feature for importing from Google Drive coming soon.")
    elif option == "Import from OneDrive":
        st.info("Feature for importing from OneDrive coming soon.")
    elif option == "Enter Key Objective":
        key_objective = st.text_input("Enter Key Objective")
        if key_objective:
            st.success(f"Creating lesson for objective: {key_objective}")

def handle_callback():
    st.write("🔁 Handling OAuth callback...")  # Debug indicator
    query_params = st.query_params
    st.write("Query Params:", query_params)  # Show full query

    if 'code' in query_params:
        provider = st.session_state.get('oauth_provider', 'google')
        code = query_params['code']
        st.write(f"Provider: {provider}")
        st.write(f"Code: {code}")

        if provider == 'google':
            handle_google_callback(code)
        elif provider == 'microsoft':
            handle_microsoft_callback(code)
        else:
            st.error("Unknown provider.")

        st.success("✅ Login callback complete. Reloading app...")
        st.rerun()
    else:
        st.error("❌ No code found in query parameters.")

if __name__ == "__main__":
    if 'user' in st.session_state:
        lesson_options()
    elif 'code' in st.query_params:
        handle_callback()
    else:
        show_login()
