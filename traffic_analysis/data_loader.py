import pandas as pd

class DataLoader:
    def __init__(self):
        self.raw_data_path = 'data/raw/Indian_Traffic_Violations.csv'

    def load_raw_data(self):
        """Load raw data from CSV file"""
        return pd.read_csv(self.raw_data_path)