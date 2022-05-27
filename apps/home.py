import streamlit as st

BIOINF_IMG = 'assets/images/monitor.png'
DNA_IMG = 'assets/images/dna-strand.png'
HOME_INFO = open('assets/info/home-info.md').read()


def app():
    col_image, col_text = st.columns([1, 3])
    with col_image:
        st.image(BIOINF_IMG)
        st.image(DNA_IMG)
    with col_text:
        st.write(HOME_INFO)
