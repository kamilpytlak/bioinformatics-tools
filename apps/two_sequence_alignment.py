import plotly.express as px
import pandas as pd
import streamlit as st


def create_dotplot(record1, record2, window):
    dict_one, dict_two = {}, {}
    for (seq, section_dict) in [
        (str(record1.seq), dict_one),
        (str(record2.seq), dict_two)
    ]:
        for i in range(len(seq) - window):
            section = seq[i : i + window]
            try:
                section_dict[section].append(i)
            except KeyError:
                section_dict[section] = [i]

    matches = set(dict_one).intersection(dict_two)
    st.write(f"{len(matches)} unique matches")

    x, y = [], []
    for section in matches:
        for i in dict_one[section]:
            for j in dict_two[section]:
                x.append(i)
                y.append(j)
    fig_dotplot = px.scatter(x=x, y=y, template="simple_white",
                             labels={
                                 "x": f"{record1.id} (length {len(record1)} bp)",
                                 "y": f"{record2.id} (length {len(record2)} bp)"
                             })
    st.plotly_chart(fig_dotplot)


def app(dna_record):
    if dna_record:
        seqs = dna_record.keys()
        first_seq = st.selectbox("Select the first sequence", seqs)
        second_seq = st.selectbox("Select the second sequence", seqs)
        window = st.number_input(label="Enter the window value", value=10, step=1, min_value=5)
        ok_button_alignment = st.button(label="Generate dotplot", key="ok_button_alignment")
        if first_seq and second_seq and window and ok_button_alignment:
            record1 = dna_record[first_seq]
            record2 = dna_record[second_seq]
            create_dotplot(record1, record2, window=window)
        else:
            st.write("Not enough data")
    else:
        st.error("No cached data. Upload a file.")
