# Crypto Analysis

CryptoAnalysis is a python library which lets users easily manage their
crypto-currency portfolio using Machine Learning on various data sources

## INSTALL INSTRUCTIONS
Type the following in the terminal:

    git clone https://github.com/ashuthoshgowda/CryptoAnalysis.git
    cd CryptoAnalysis
    python setup.py install


## LOAD DATA INSTRUCTIONS

    from crypto_analysis import load_data
    analysis_jan = load_data.load_data()
    analysis_jan.get_top_n_crypto_tickers()
    analysis_jan.get_data_from_yahoo()


(Note the double-colon and 4-space indent formatting above.)

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.


A Section
=========

Lists look like this:

* First

* Second. Can be multiple lines
  but must be indented properly.

A Sub-Section
-------------

Numbered lists look like you'd expect:

1. hi there

2. must be going

Urls are http://like.this and links can be
written `like this <http://www.example.com/foo/bar>`_.
