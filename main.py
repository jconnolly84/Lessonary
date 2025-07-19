
import streamlit as st
from auth import check_login

check_login()

st.title("Welcome to the Lessonary App!")
st.write("Choose an option:")
