Some scripts for web scrapping filing and financial data from sec.

get_cik_num.py allow us to create a new file with companies and their cik number from two files; 
    - liste_cik_complete.txt which repertories all companies with their cik number,
    - liste_NASDAQ.txt which repertories all companies who belong to NASDAQ index

get_filing_data.ipynb :
    - inputs : liste_cik, filing type (10-k, 10-q, 8-k..)
    - ouputs exemple : {'filing_aapl': [{'file_type': '10-Q',
                        'file_number': '001-36743231141522',
                        'file_date': '2023-08-04',
                        'links': {'documents': 'https://www.sec.gov/Archives/edgar/data/320193/000032019323000077/0000320193-23-000077-index.htm',
                            'documents_xml': 'https://www.sec.gov/Archives/edgar/data/320193/000032019323000077/FilingSummary.xml',
                            'interactive_data': 'https://www.sec.gov/cgi-bin/viewer?action=view&cik=320193&accession_number=0000320193-23-000077&xbrl_type=v',
                            'filing_number': 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&filenum=001-36743&owner=exclude&count=100'}}, 

get_financial_data.ipynb allow us to access financial data from sec filing