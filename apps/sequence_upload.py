import io

import streamlit as st
from Bio import SeqIO


def upload_file(file_or_path, is_uploaded: bool) -> (None, dict):
    """
    Loads the uploaded/example file

    :param file_or_path: File object or path to sample file
    :param is_uploaded: Boolean object indicating whether the file is uploaded or not
    :return: Dictionary object with sequences if validation was successful; otherwise None
    """
    text_obj = file_or_path.read().decode('UTF-8') if is_uploaded else open(file_or_path, encoding='UTF-8').read()
    dna_record = SeqIO.to_dict(SeqIO.parse(io.StringIO(text_obj), 'fasta'))
    return dna_record if dna_record else None


def process_file(uploaded_file, dna_record):
    """
    Validates the uploaded file with potential sequences based on FASTA format

    :param uploaded_file: File object
    :param dna_record: Dictionary object with sequences
    :return: Sequence object and file name if validation was successful; otherwise None
    """
    if dna_record:
        file_name = uploaded_file if isinstance(uploaded_file, str) else uploaded_file.name
        st.session_state['file_cached'] = dna_record
        st.success('File correctly uploaded. Validation successfully completed.')
    else:
        dna_record, file_name = None, None
        st.error('Error while processing a file. Make sure you have uploaded a FASTA file.')
    st.session_state['file_cached'] = dna_record
    st.session_state['file_name'] = file_name
    return dna_record, file_name
