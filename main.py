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

    st.write("Choose how you'd like to create your lesson:")

    option = st.radio(
        "Select input method:",
        ("Upload PowerPoint file", "Import from Google Drive", "Import from OneDrive", "Enter Key Objective")
    )

    if option == "Upload PowerPoint file":
        uploaded_file = st.file_uploader("Upload PPT/PPTX file", type=['ppt', 'pptx'])
        if uploaded_file:
            st.write(f"Uploaded {uploaded_file.name}")
            # Process file here
            
    elif option == "Import from Google Drive":
        st.write("Importing from Google Drive...")
        # Google Drive integration code here
    
    elif option == "Import from OneDrive":
        st.write("Importing from OneDrive...")
        # OneDrive integration code here
    
    elif option == "Enter Key Objective":
        key_objective = st.text_input("Enter Key Objective")
        if key_objective:
            st.write(f"Creating lesson for objective: {key_objective}")
            # Generate lesson from Key Objective

# Main OAuth callback handling
if __name__ == "__main__":
    query_params = st.query_params
    
    if 'code' in query_params:
        # Determine OAuth provider from session or state
        provider = st.session_state.get('oauth_provider', 'google')  # default to Google if not set
        
        if provider == 'google':
            handle_google_callback(query_params['code'])
        elif provider == 'microsoft':
            handle_microsoft_callback(query_params['code'])
        st.rerun()

    elif 'user' in st.session_state:
        lesson_options()
    else:
        show_login()
