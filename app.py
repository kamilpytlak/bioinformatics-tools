import os

import streamlit as st
from streamlit_option_menu import option_menu

from apps import home, sequence_summary, two_sequence_alignment
from apps.sequence_upload import upload_file, process_file


MAIN_INFO = open('assets/info/main_info.md').read()
DATA_EXAMPLES = [f for f in os.listdir('data') if f.endswith(('fasta', 'fa', 'txt'))]


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

        uploaded_seq = st.file_uploader('Upload a FASTA file', type=['fasta', 'fa', 'txt'])
        ok_button_file = st.button(label='Upload a file', key='ok_button_file')
        example_file = st.selectbox(label='Or choose an example', key='example_files',
                                    options=DATA_EXAMPLES)
        ok_button_example = st.button(label='Upload an example file', key='ok_button_example')

        if ok_button_file and uploaded_seq:
            dna_record = upload_file(file_or_path=uploaded_seq, is_uploaded=True)
            process_file(uploaded_seq, dna_record)
        elif ok_button_example and example_file:
            dna_record = upload_file(file_or_path=f'data/{example_file}', is_uploaded=False)
            process_file(example_file, dna_record)
        elif ok_button_file and not uploaded_seq:
            st.error('No file selected.')

        if 'file_cached' not in st.session_state:
            st.session_state['file_cached'] = None
        if 'file_name' not in st.session_state:
            st.session_state['file_name'] = None

        file_name = st.session_state['file_name']
        st.warning(f'File currently cached: {file_name}')

        st.info(MAIN_INFO)

    dna_record = st.session_state['file_cached']

    if menu_option == 'Home':
        home.app()
    elif menu_option == 'Sequence Summary':
        sequence_summary.app(dna_record)
    elif menu_option == 'Two Sequence Alignment':
        two_sequence_alignment.app(dna_record)


if __name__ == '__main__':
    main()
