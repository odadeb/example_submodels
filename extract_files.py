class Extract_files():
    """
    For use this class you need 4 values file_path, separator, file name and encoding
    """
    def __init__(self, file_path, filename, encoding):
        self.extract_path = file_path
        self.extract_filename = filename
        self.extract_encoding = extract_filename   
    
    def extract_csv_file(separator):

        dataframe = pd.read_csv(f'{self.extract_path}/{self.extract_filename}.csv',
                           enconding = self.extract_encoding, sep=separator )    
        return dataframe
    
    def extract_xlsx_file():

        dataframe = pd.read_excel(f'{self.extract_path}/{self.extract_filename}.xlsx')
        return dataframe