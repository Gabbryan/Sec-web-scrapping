class DataProcessor:
    def __init__(self, file_path_1, file_path_2, output_file):
        self.file_path_1 = file_path_1
        self.file_path_2 = file_path_2
        self.output_file = output_file
        self.data_1 = {}
        self.data_2 = {}
        self.results = {}

    def read_data_from_files(self):
        with open(self.file_path_1, 'r') as file1, open(self.file_path_2, 'r') as file2:
            for line in file1:
                symbol = line.strip().split('|')[0]
                self.data_1[symbol] = line.strip()

            for line in file2:
                symbol, number = line.strip().split('\t')
                self.data_2[symbol.lower()] = number

    def process_data(self):
        for symbol in self.data_1:
            if symbol.lower() in self.data_2:
                self.results[symbol] = self.data_2[symbol.lower()]

    def save_data_to_txt(self):
        with open(self.output_file, 'w') as file:
            for symbol, number in self.results.items():
                file.write(f"{symbol} {number}\n")

    def main(self):
        self.read_data_from_files()
        self.process_data()
        self.save_data_to_txt()

if __name__ == "__main__":
    file_path_1 = 'liste_NASDAQ.txt'  # Remplacez par le chemin vers le premier fichier
    file_path_2 = 'liste_CIK_FULL.txt'  # Remplacez par le chemin vers le deuxième fichier
    output_file = 'NASDAQ_CIK.txt'  # Remplacez par le chemin où vous souhaitez enregistrer le fichier de sortie
    
    data_processor = DataProcessor(file_path_1, file_path_2, output_file)
    data_processor.main()
