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

## ToDo

### Repo Contribution Policies

clone Repo and cd into the directory

    git pull origin
    git checkout -b {branch_type}/{branch_name}
    ## Make and review changes or add new modules
    git add -A
    git commit -m "commit msg"
    git push {branch_type}/{branch_name}

Create a Pull Request in the github GUI, and add reviewers    

### Data Preprocessing

Add a detailed Data Scrapping ToDo list in docs/data_scrapping.md

### Data Science Module

Add a detailed Data Science ToDo list in docs/data_science.md
