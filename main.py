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
