import plotly.express as px
import streamlit as st

ALIGNMENT_INFO = open('assets/info/two-sequence-alignment-info.md').read()
ALIGNMENT_ICON = 'assets/images/alignment.png'


def create_dotplot(record1, record2, window):
    """
    Constructs a comparison matrix of the two nucleotide sequences.

    :param record1: 1. nucleotide sequence
    :param record2: 2. nucleotide sequence
    :param window: window size
    :return: comparison matrix (dotplot) of the two sequences record1 and record2
    """
    dict_one, dict_two = {}, {}
    for (seq, section_dict) in [
        (str(record1.seq), dict_one),
        (str(record2.seq), dict_two)
    ]:
        for i in range(len(seq) - window):
            section = seq[i:i + window]
            try:
                section_dict[section].append(i)
            except KeyError:
                section_dict[section] = [i]

    matches = set(dict_one).intersection(dict_two)
    st.write(f'{len(matches)} unique matches')

    x, y = [], []
    for section in matches:
        for i in dict_one[section]:
            for j in dict_two[section]:
                x.append(i)
                y.append(j)
    fig_dotplot = px.scatter(x=x, y=y, template='simple_white',
                             labels={
                                 'x': f'{record1.id} (length {len(record1)} bp)',
                                 'y': f'{record2.id} (length {len(record2)} bp)'
                             })
    st.plotly_chart(fig_dotplot)


def app(dna_record):
    """
    The main executive function of the tool "Two Sequence Alignment"

    :param dna_record: sequence file saved as FASTA
    """
    col_image, col_text = st.columns([1, 3])
    with col_image:
        st.image(ALIGNMENT_ICON)
    with col_text:
        st.write(ALIGNMENT_INFO)

    if dna_record:
        seqs = dna_record.keys()
        first_seq = st.selectbox('Select the first sequence', seqs)
        second_seq = st.selectbox('Select the second sequence', seqs)
        window = st.number_input(label='Enter the window value', value=10, step=1, min_value=5)
        ok_button_alignment = st.button(label='Generate dotplot', key='ok_button_alignment')
        if all((first_seq,  second_seq,  window, ok_button_alignment)):
            record1 = dna_record[first_seq]
            record2 = dna_record[second_seq]
            dna_valid = set('ACTG')
            dna_sample = set(record1 + record2)
            # Matrix construction if nucleotide sequences are provided
            if dna_sample.issubset(dna_valid):
                create_dotplot(record1, record2, window=window)
            else:
                st.error('''
                The nucleotide sequence was not introduced.
                Construction of a comparison matrix is not possible.
                ''')
        else:
            st.write('Not enough data')
    else:
        st.error('No cached data. Upload a file.')
