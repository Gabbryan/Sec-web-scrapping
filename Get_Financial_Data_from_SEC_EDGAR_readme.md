<span style="font-size:24px;">Get Financial Data from SEC EDGAR</span>

This Python script, **Get Financial Data from SEC EDGAR**, is a Python utility designed to extract financial data from the U.S. Securities and Exchange Commission's Electronic Data Gathering, Analysis, and Retrieval (EDGAR) system. It automates the process of fetching filings, extracting financial statements, and organizing the data into Excel files for further analysis.

<span style="font-size:18px;">Features</span>

* Fetches financial filings (e.g., 10-K reports) for a list of companies using their Central Index Key (CIK).
* Retrieves various details for each filing, including filing type, date, and links to relevant documents.
* Extracts financial statements from the filings, such as balance sheets, income statements, and cash flow statements.
* Organizes the extracted financial data into Excel files for easy access and analysis.

<span style="font-size:18px;">Usage</span>

1. Ensure you have Python 3.x installed on your system.
2. Clone this repo or download the **'Get_Financial_Data_from_SEC_EDGAR.ipynb'** script.
3. Prepare a list of CIK numbers for the companies you want to retrieve filings for and save it in a text file (e.g., liste_cik.txt). Each line of the file should contain a company name followed by its CIK number, separated by a space or tab.
4. Customize the script by specifying the path to your CIK file (cik_file_path) and the type of filing you're interested in (e.g., "10-k" for annual reports).
5. Run the script
6. The script will fetch the filings, process the data, extract financial statements, and save the results in Excel files organized by filing date and financial statement type.

<span style="font-size:18px;">Example</span>

* __'liste_cik.txt'__ (sample CIK file):

``` 
Apple Inc. 0000320193
Microsoft Corporation 0000789019
Alphabet Inc. 0001652044
```


* Output (excel files):

* __'financial_information/url_aapl-20160924.xlsx'__:
Contains financial data extracted from Apple Inc.'s 10-K filing for September 24, 2016, including comprehensive income, pre-tax amounts reclassified from AOCI into consolidated statements of operations.
* Similar Excel files for other companies and financial statement types.

<span style="font-size:18px;">License</span>

This project is licensed under the MIT License. See the LICENSE file for details.
