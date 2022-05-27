import streamlit as st

HOME_LOGO = 'assets/images/bioinf_image.png'
HOME_INFO = open('assets/info/home_info.md').read()


def app():
    col_image, col_text = st.columns([1, 3])
    with col_image:
        st.image(HOME_LOGO)
    with col_text:
        st.write(HOME_INFO)
