
import streamlit as st
from auth_utils import login_with_google, login_with_microsoft

st.set_page_config(page_title="Lessonary Login", page_icon="favicon.png")

st.image("LOGO_Lessonary_WhiteBG.png", width=200)
st.title("Login to Lessonary")

login_method = st.radio("Select login method", ["google", "microsoft"], horizontal=True, label_visibility="collapsed")

if login_method == "google":
    google_url = login_with_google()
    st.markdown(
        f'''
        <a href="{google_url}">
            <button style="background-color:#DB4437;color:white;border:none;padding:10px 20px;border-radius:5px;font-size:16px;">
                🔴 Login with Google
            </button>
        </a>
        ''',
        unsafe_allow_html=True
    )

elif login_method == "microsoft":
    if st.button("🔵 Login with Microsoft"):
        login_with_microsoft()
