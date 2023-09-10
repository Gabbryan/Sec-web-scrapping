<span style="font-size:24px;">EDGAR Data Fetcher</span>

The **'EDGAR Data Fetcher'**, is a Python script designed to retrieve and organize financial filings from the U.S. Securities and Exchange Commission's Electronic Data Gathering, Analysis, and Retrieval (EDGAR) system. It can be particularly useful for financial analysts, researchers, or investors who need to access and process financial documents filed by publicly traded companies.

<span style="font-size:18px;">Features</span>

* Fetches financial filings (e.g., 10-Q reports) for a list of companies using their Central Index Key (CIK).
* Retrieves various details for each filing, including filing type, date, and links to relevant documents.
* Saves the retrieved data in CSV files for further analysis and research.

<span style="font-size:18px;">Usage</span>

1. Ensure you have Python 3.x installed on your system.
2. Clone this repo or download the **'EDGAR_Data_Fetcher.ipynb'** script.
3. Prepare a list of CIK numbers for the companies you want to retrieve filings for and save it in a text file (e.g., liste_cik.txt). Each line of the file should contain a company name followed by its CIK number, separated by a space or tab.
4. Customize the script by specifying the path to your CIK file (cik_file_path) and the type of filing you're interested in (e.g., "10-q" for quarterly reports).
5. Run the script
6. The script will fetch the filings, process the data, and save the results in CSV files organized by filing type.

<span style="font-size:18px;">Example</span>

* __'list_cik.txt'__ (sample CIK file):

``` 
Apple Inc. 0000320193
Microsoft Corporation 0000789019
Alphabet Inc. 0001652044

```

* Output (CSV files):

* __'filing_type/filing_Apple Inc.csv'__:
``` 
    file_type,file_number,file_date,documents,documents_xml,interactive_data,filing_number
10-Q,12345,2023-08-01,https://www.sec.gov/edgar/...
```

* Similar CSV files for other companies and filing types.

<span style="font-size:18px;">License</span>

This project is licensed under the MIT License. See the LICENSE file for details.
