import streamlit as st

HOME_LOGO = 'assets/images/bioinf_image.png'
HOME_INFO = open('assets/info/home_info.md').read()

def app():
    col_1, col_2 = st.columns([1, 3])

    with col_1:
        st.image(HOME_LOGO)
    with col_2:
        st.write(HOME_INFO)

