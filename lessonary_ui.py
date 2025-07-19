import streamlit as st

def render_lessonary_ui():
    user_info = st.session_state["user_info"]
    st.image(user_info["picture"], width=80)
    st.markdown(f"## Welcome to Lessonary, **{user_info['given_name']}**!")
    st.write("---")

    st.markdown("### Choose how you'd like to create your lesson:")
    input_method = st.radio(
        "Select input method:",
        ["Upload PowerPoint file", "Import from Google Drive", "Import from OneDrive", "Enter Key Objective"]
    )

    if input_method == "Upload PowerPoint file":
        st.file_uploader("Upload PPT/PPTX file", type=["ppt", "pptx"])
    else:
        st.info("This feature will be available soon.")
