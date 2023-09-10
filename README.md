# Data Processor

This Python script, **'data_processor.py'**, is a simple utility for processing data from two text files and generating an output file with the results. It can be useful for tasks like cross-referencing and merging data from different sources.

## Features

* Reads data from two input files.
* Processes the data based on specified criteria
* Saves the results to an output text file.

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Clone this repo or download the **'data_processor.py'** script.
3. Replace the file paths and names in the script with your own data files and desired output.

```python linenums
file_path_1 = 'file1.txt'  # Replace with the path to your first data file, it should contain the SYMBOLS
file_path_2 = 'file2.txt'  # Replace with the path to your second data file, it should contain the CIK numbers
output_file = 'output.txt'  # Replace with the desired name for the output file, it will contain the symbol with their associated CIK number
```

4. Run the script

``` python linenums
python data_processor.py
```

5. The script will read and process the data from the input files based on your criteria and ssave the results to the specified output file.

## Example

* __'file1.txt'__ (sample data file 1):

``` 
AAPL|Apple Inc.
MSFT|Microsoft Corporation
GOOGL|Alphabet Inc.
```

* __'file2.txt'__ (sample data file 2):

``` 
aapl   12345
msft   67890
googl  54321
jnj	200406
v	1403161
tsm	1046179
xom	34088
wmt	104169
spy	884394
jpm	19617
pg	80424
nvda	1045810
lvmuy	824046
ma	1141391
```

* __'output.txt'__ Output:

``` 
AAPL 12345
MSFT 67890
GOOGL 54321
```

# EDGAR Data Fetcher

The **'EDGAR Data Fetcher'**, is a Python script designed to retrieve and organize financial filings from the U.S. Securities and Exchange Commission's Electronic Data Gathering, Analysis, and Retrieval (EDGAR) system. It can be particularly useful for financial analysts, researchers, or investors who need to access and process financial documents filed by publicly traded companies.

## Features

* Fetches financial filings (e.g., 10-Q reports) for a list of companies using their Central Index Key (CIK).
* Retrieves various details for each filing, including filing type, date, and links to relevant documents.
* Saves the retrieved data in CSV files for further analysis and research.

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Clone this repo or download the **'EDGAR_Data_Fetcher.ipynb'** script.
3. Prepare a list of CIK numbers for the companies you want to retrieve filings for and save it in a text file (e.g., liste_cik.txt). Each line of the file should contain a company name followed by its CIK number, separated by a space or tab.
4. Customize the script by specifying the path to your CIK file (cik_file_path) and the type of filing you're interested in (e.g., "10-q" for quarterly reports).
5. Run the script
6. The script will fetch the filings, process the data, and save the results in CSV files organized by filing type.

## Example

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

# Get Financial Data from SEC EDGAR

This Python script, **Get Financial Data from SEC EDGAR**, is a Python utility designed to extract financial data from the U.S. Securities and Exchange Commission's Electronic Data Gathering, Analysis, and Retrieval (EDGAR) system. It automates the process of fetching filings, extracting financial statements, and organizing the data into Excel files for further analysis.

## Features

* Fetches financial filings (e.g., 10-K reports) for a list of companies using their Central Index Key (CIK).
* Retrieves various details for each filing, including filing type, date, and links to relevant documents.
* Extracts financial statements from the filings, such as balance sheets, income statements, and cash flow statements.
* Organizes the extracted financial data into Excel files for easy access and analysis.

## Usage

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

## License

This project is licensed under the MIT License. See the LICENSE file for details.

