
import streamlit as st
from auth_utils import (
    login_with_google,
    login_with_microsoft,
)

st.image("assets/lessonary_logo.png", width=200)
st.title("Login to Lessonary")

if st.button("Login with Google", key="login_google"):
    login_with_google()

if st.button("Login with Microsoft", key="login_microsoft"):
    login_with_microsoft()
