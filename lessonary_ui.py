
import streamlit as st

def render_lessonary_ui():
    user_info = st.session_state.get("user", {})
    name = user_info.get("name", "there")
    picture = user_info.get("picture")
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
