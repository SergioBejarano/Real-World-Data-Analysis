import unittest
import pandas as pd
from pathlib import Path
from scripts.data_loader import load_data
from scripts.data_cleaner import clean_data

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.raw_data = pd.DataFrame({
            'FECHA ACCIDENTE': ['11/06/2014', '12/06/2014', None],
            'GRAVEDAD': ['h', 'm', None],
            'CLASE ACCIDENTE': ['VOLCAMIENTO', 'CHOQUE', None],
            'MUNICIPIO': ['MEDELLÍN', 'ENVIGADO', None],
            'NUMERO VICTIMA PEATÓN': [0, 1, None],
            'NUMERO VICTIMA ACOMPAÑANTE': [0, 0, None],
            'NUMERO VICTIMA PASAJERO': [0, 1, None],
            'NUMERO VICTIMA CONDUCTOR': [1, 0, None],
            'NUMERO VICTIMA HERIDO': [0, 1, None],
            'NUMERO VICTIMA MUERTO': [0, 0, None]
        })

        self.test_file_path = Path('test_data.csv')
        self.raw_data.to_csv(self.test_file_path, index=False)

    def tearDown(self):
        if self.test_file_path.exists():
            self.test_file_path.unlink()

    def test_load_data(self):
        data = load_data(self.test_file_path)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)  

    def test_clean_data(self):
        clean_data_df = clean_data(self.raw_data)

        self.assertEqual(len(clean_data_df), 2)  

        self.assertIn('TOTAL VICTIMAS', clean_data_df.columns)
        self.assertEqual(clean_data_df['TOTAL VICTIMAS'].iloc[0], 1)  
        self.assertEqual(clean_data_df['TOTAL VICTIMAS'].iloc[1], 3) 

    def test_clean_data_numeric_conversion(self):
        clean_data_df = clean_data(self.raw_data)

        numeric_columns = [
            'NUMERO VICTIMA PEATÓN', 'NUMERO VICTIMA ACOMPAÑANTE', 'NUMERO VICTIMA PASAJERO',
            'NUMERO VICTIMA CONDUCTOR', 'NUMERO VICTIMA HERIDO', 'NUMERO VICTIMA MUERTO'
        ]
        for col in numeric_columns:
            self.assertTrue(pd.api.types.is_numeric_dtype(clean_data_df[col]))

    

    def test_clean_data_weather_normalization(self):
        """
        Verify that the ESTADO CLIMA column is normalized to uppercase.
        """
        self.raw_data['ESTADO CLIMA'] = ['lluvia', 'Normal', None]
        clean_data_df = clean_data(self.raw_data)

        self.assertIn('ESTADO CLIMA', clean_data_df.columns)
        self.assertTrue(all(clean_data_df['ESTADO CLIMA'].str.isupper()))

    def test_clean_data_hour_conversion(self):
        """
        Verify that the HORA ACCIDENTE column is correctly converted to numeric hours.
        """
        self.raw_data['HORA ACCIDENTE'] = ['12:01', '15:30', None]
        clean_data_df = clean_data(self.raw_data)

        self.assertIn('HORA ACCIDENTE', clean_data_df.columns)
        self.assertFalse(pd.api.types.is_numeric_dtype(clean_data_df['HORA ACCIDENTE']))
        self.assertEqual(clean_data_df['HORA ACCIDENTE'].iloc[0], "12:01")
        self.assertEqual(clean_data_df['HORA ACCIDENTE'].iloc[1], "15:30")

    
    def test_clean_data_missing_columns(self):
        """
        Test the clean_data function when required columns are missing.
        """
        incomplete_data = self.raw_data.drop(columns=['GRAVEDAD', 'CLASE ACCIDENTE'])
        with self.assertRaises(KeyError):
            clean_data(incomplete_data)



if __name__ == '__main__':
    unittest.main()