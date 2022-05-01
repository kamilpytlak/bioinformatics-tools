import streamlit as st
from streamlit_option_menu import option_menu

from apps import home, sequence_summary

MAIN_INFO = open('assets/info/main_info.md').read()


def main():
    # Sidebar menu
    with st.sidebar:
        menu_option = option_menu(
            menu_title='Main Menu',
            options=[
                'Home',
                'Sequence Summary',
                'Two Sequence Alignment'
            ],
            icons=['house', 'list-columns', 'justify'],
            default_index=0,
            menu_icon='tools'
        )

    st.sidebar.info(MAIN_INFO)

    if menu_option == 'Home':
        home.app()
    elif menu_option == "Sequence Summary":
        sequence_summary.app()


if __name__ == '__main__':
    main()
