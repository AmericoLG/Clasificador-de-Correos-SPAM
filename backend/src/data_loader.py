import pandas as pd

class DataLoader:
    def __init__(self):
        self.csv_data = None

    def load_file(self, path):
        """Importación de datasets [cite: 41, 70]"""
        self.csv_data = pd.read_csv(path)
        return self.csv_data

    def clean_nulls(self):
        """Limpieza de datos nulos [cite: 42, 71]"""
        if self.csv_data is not None:
            self.csv_data.dropna(inplace=True)
            print("Datos nulos eliminados.")