<span style="font-size:24px;">Data Processor</span>

This Python script, **'data_processor.py'**, is a simple utility for processing data from two text files and generating an output file with the results. It can be useful for tasks like cross-referencing and merging data from different sources.

<span style="font-size:18px;">Features</span>

* Reads data from two input files.
* Processes the data based on specified criteria
* Saves the results to an output text file.

<span style="font-size:18px;">Usage</span>

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

<span style="font-size:18px;">Example</span>

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

<span style="font-size:18px;">License</span>

This project is licensed under the MIT License. See the LICENSE file for details.
