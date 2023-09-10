class DataProcessor:
    def __init__(self, file_path_1, file_path_2, output_file):

        """
        Initialize the DataProcessor class.

        Args:
            file_path_1 (str): Path to the first input file.
            file_path_2 (str): Path to the second input file.
            output_file (str): Path to the output file where results will be saved.
        """

        self.file_path_1 = file_path_1
        self.file_path_2 = file_path_2
        self.output_file = output_file
        self.data_1 = {} # Dictionary to store data from the first file.
        self.data_2 = {} # Dictionary to store data from the second file.
        self.results = {} # Dictionary to store the matching results.

    def read_data_from_files(self):

        """
        Read data from the input files and populate data_1 and data_2 dictionaries.
        """

        with open(self.file_path_1, 'r') as file1, open(self.file_path_2, 'r') as file2:
            for line in file1:
                symbol = line.strip().split('|')[0]
                self.data_1[symbol] = line.strip()

            for line in file2:
                symbol, number = line.strip().split('\t')
                self.data_2[symbol.lower()] = number

    def process_data(self):

        """
        Process the data to find matching symbols and store them in the results dictionary.
        """

        for symbol in self.data_1:
            if symbol.lower() in self.data_2:
                self.results[symbol] = self.data_2[symbol.lower()]

    def save_data_to_txt(self):

        """
        Save the matching results to the output file.
        """
        
        with open(self.output_file, 'w') as file:
            for symbol, number in self.results.items():
                file.write(f"{symbol} {number}\n")

    def main(self):
        
        """
        The main function that orchestrates the entire data processing pipeline.
        """

        self.read_data_from_files()
        self.process_data()
        self.save_data_to_txt()

if __name__ == "__main__":
    file_path_1 = 'NASDAQ_list.txt'  # Replace with the path to your first data file, it should contain the SYMBOLS
    file_path_2 = 'liste_CIK_FULL.txt'  # Replace with the path to your second data file, it should contain the CIK numbers
    output_file = 'NASDAQ_CIK.txt'  # Replace with the desired name for the output file, it will contain the symbol with their associated CIK number
    
    data_processor = DataProcessor(file_path_1, file_path_2, output_file)
    data_processor.main()
