import unittest
import pandas as pd
from traffic_analysis.data_cleaner import  DataCleaner

class TestDataCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = DataCleaner()
        self.df = pd.DataFrame({
            'Violation_ID': [1, 2, 3, 4, None],
            'Violation_Type': ['Speeding', 'Red Light', None, 'Parking Violation', 'Speeding'],
            'Date': ['2023-11-19', '2023-11-20', '2023-11-21', None, '2023-11-22'],
            'Location': ['Delhi', 'Unknown', 'Maharashtra', 'Karnataka', None],
            'Comments': [None, 'No seatbelt', 'Over speed', None, None],
            'Previous_Violations': [2, None, 1, 0, None],
            'Vehicle_Type': ['Bike', 'Scooter', None, 'Car', 'Auto Rickshaw'],
            'Driver_Gender': ['Male', 'Female', 'Unknown', None, 'Other']
        })

    def test_clean_data(self):
        cleaned_df = self.cleaner.clean_data(self.df)
        self.assertEqual(len(cleaned_df), 2)
        self.assertTrue(all(cleaned_df['Comments'].notnull()))
        self.assertTrue(all(cleaned_df['Previous_Violations'].notnull()))
        self.assertTrue(all(cleaned_df['Violation_Type'].str.istitle()))


    def test_standardize_text(self):
        cleaned_df = self.cleaner.clean_data(self.df)
        self.assertTrue(all(cleaned_df['Violation_Type'].str.istitle()))
        self.assertTrue(all(cleaned_df['Location'].str.istitle()))

    def test_get_cleaning_report(self):
        cleaned_df = self.cleaner.clean_data(self.df)
        report = self.cleaner.get_cleaning_report(self.df, cleaned_df)

        self.assertEqual(report['original_rows'], len(self.df))
        self.assertEqual(report['cleaned_rows'], len(cleaned_df))
        self.assertEqual(report['rows_removed'], len(self.df) - len(cleaned_df))
        self.assertIn('Violation_Type', report['columns_processed'])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.cleaner.clean_data("invalid input")

if __name__ == '__main__':
    unittest.main()
