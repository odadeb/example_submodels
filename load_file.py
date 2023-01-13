class Load_files():
    """
    For use this class you need 2 values file_path and file name /  need dataframe
    """
    def __init__(self, file_path, filename, dataframe):
        self.load_path = file_path
        self.load_filename = filename
        self.load_dataframe = dataframe    
    
    def load_csv_file():

        self.dataframe.to_csv(f'{self.load_path}/{self.load_filename}.csv', sep=',' )    
        return dataframe
    
    def load_xlsx_file():

        self.dataframe.to_excel(f'{self.load_path}/{self.load_filename}.xlsx')
        return dataframe
