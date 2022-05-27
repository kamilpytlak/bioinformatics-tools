from collections import Counter

import pandas as pd
from scipy.stats import chisquare
import plotly.express as px
import plotly.figure_factory as ff
from Bio.SeqUtils import GC

import streamlit as st

SEQUENCE_SUMMARY_INFO = open('assets/info/sequence_summary_info.md').read()
SEQUENCE_SUMMARY_ICON = 'assets/images/summary_icon.png'


def check_seq_dist(seq_count: pd.Series):
    df = len(seq_count) - 1
    chi_stat, p_value = chisquare(seq_count)
    chi_stat, p_value = chi_stat.round(2), p_value.round(2)
    if p_value > 0.05:
        st.write(rf'''
        No basis for rejecting the hypothesis of sequence homogeneity
        ($\chi^2_{df} \approx {chi_stat}; p \approx {p_value}$)
        ''')
    else:
        st.write(rf'''
        The sequence is not homogeneous
        ($\chi^2_{df} \approx {chi_stat}; p \approx {p_value}$)
        ''')


def summary(record):
    seq = record.seq
    seq_name = record.name
    seq_len = len(seq)
    seq_freq = pd.DataFrame.from_dict(Counter(seq), orient='index').reset_index()
    seq_freq.columns = ['Nucleotide', 'Count']
    seq_freq['Frequency'] = (seq_freq['Count'] / seq_freq['Count'].sum()).round(2)

    st.write(f'**Record name:** {seq_name}')

    st.write(f'**Overall record length:** {seq_len} nucleotides')

    st.write(f'**Nucleotide distribution:**')
    fig_table = ff.create_table(seq_freq)
    fig_dist = px.bar(seq_freq, x='Nucleotide', y='Count')
    st.plotly_chart(fig_table)
    st.plotly_chart(fig_dist)
    st.write(f'**GC content:** {round(GC(seq), 2)}%')
    check_seq_dist(seq_freq['Count'])

    st.markdown('---')


def app(dna_record):
    col_image, col_text = st.columns([1, 3])
    with col_image:
        st.image(SEQUENCE_SUMMARY_ICON)
    with col_text:
        st.write(SEQUENCE_SUMMARY_INFO)

    if dna_record:
        seq_names = st.multiselect('Select one or more sequences for analysis', dna_record.keys())
        for seq_name in seq_names:
            record = dna_record[seq_name]
            summary(record)
    else:
        st.error('No cached data. Upload a file.')
