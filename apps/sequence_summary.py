import io

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import GC

import streamlit as st


def app():
    seq_file = st.file_uploader("Upload a FASTA file", type=["fasta", "fa", "txt"])

    if st.button("OK") and seq_file:
        byte_str = seq_file.read()
        text_obj = byte_str.decode("UTF-8")

        dna_record = SeqIO.read(io.StringIO(text_obj), "fasta")
        st.write(dna_record.id)
