# Bioinformatics Tools (BioT)

<p align="center">
  <img src="https://i.imgur.com/fP0SQMW.png" />
</p>

## Table of Contents
1. [General info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)


## General info
Bioinformatics Tools (BioT) is a web application created using the Streamlit module in Python that allows for nucleotide/amino acid sequence analysis. It includes the tools necessary to perform descriptive statistics on sequences (substrate counts, verification of the hypothesis of sequence homogeneity), as well as the construction of a comparison matrix of the two nucleotide sequences (dotplot).

## Technologies
The application was written in Python 3.9.12. `Streamlit 1.9.1` was used to create the user interface. `streamlit-option-menu 0.3.2` was used to divide the application into tabs (multipage structure). The data analysis used `pandas 1.4.2`, `SciPy 1.8.1`, `Biopython 1.79` and `plotly 5.8.0`.

## Installation
The project was uploaded to the web using Streamlit Cloud. You can use it online at the following link: https://share.streamlit.io/kamilpytlak/bioinformatics-tools/app.py. If you want to use this app on your local machine, install `pipenv`, copy the application to the target directory and run `pipenv shell` and `pipenv install` respectively.
1.  Install the packages according to the configuration file `Pipfile`.
```
pipenv shell
pipenv install
```

2.  Ensure that the `streamlit` package was installed successfully. To test it, run the following command:
```
streamlit hello
```
If the example application was launched in the browser tab, everything went well. You can also specify a port if the default doesn't respond:
```
streamlit hello --server.port port_number
```
Where `port_number` is a port number (8889, for example).

3.  To start the app, type:
```
streamlit run app.py
```
