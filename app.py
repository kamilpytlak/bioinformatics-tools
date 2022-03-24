import streamlit as st
from streamlit_option_menu import option_menu


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


if __name__ == '__main__':
    main()
