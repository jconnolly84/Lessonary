import streamlit as st
from auth import authenticate_user, handle_google_auth, handle_ms_auth
from pathlib import Path

# Configure page
st.set_page_config(
    page_title="Lessonary",
    page_icon="favicon.png",
    layout="wide"
)

# Show logo
logo_path = Path("LOGO_Lessonary_Enhanced.png")
if logo_path.exists():
    st.image(str(logo_path), width=300)
else:
    st.title("Lessonary")

# Handle authentication
handle_google_auth()
handle_ms_auth()

# Check login state
if "user" not in st.session_state:
    st.markdown("### 👋 Welcome to Lessonary")
    st.markdown("Please login to continue.")
    authenticate_user()
    st.stop()

# Show user info
user = st.session_state["user"]
st.success(f"✅ Logged in as **{user['name']}** ({user['email']})")

# --- Main Dashboard UI ---
st.markdown("## What would you like to do today?")
st.markdown("Choose one of the options below to get started:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📂 Choose a presentation")
    st.markdown("Import a .pptx from your **Google Drive** or **OneDrive**.")
    if st.button("Connect to Cloud Storage"):
        st.info("🔧 This will allow you to browse files from Google Drive or OneDrive. (Coming soon)")

with col2:
    st.markdown("### ⬆️ Upload a PowerPoint")
    st.markdown("Let us uplift and analyse your existing lesson.")
    uploaded_file = st.file_uploader("Upload a PowerPoint (.pptx)", type=["pptx"])
    if uploaded_file:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        st.info("🚧 Uplift pipeline will run here.")

with col3:
    st.markdown("### 🧠 Create from Key Objective")
    st.markdown("We'll build a TLC-aligned lesson from your input.")
    with st.form("create_lesson_form"):
        key_objective = st.text_input("Key Objective")
        subject = st.text_input("Subject")
        age_group = st.selectbox("Age Group", ["KS1", "KS2", "KS3", "KS4", "KS5"])
        submitted = st.form_submit_button("Generate Lesson")
        if submitted:
            st.success("🚀 Lesson generation triggered with your inputs.")
            st.write(f"**Objective:** {key_objective}")
            st.write(f"**Subject:** {subject}")
            st.write(f"**Age Group:** {age_group}")
