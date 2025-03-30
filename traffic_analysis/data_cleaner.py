import pandas as pd
from datetime import datetime

class DataCleaner:
    def clean_data(self, df):
        """Clean and preprocess the raw traffic violations data"""
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")

        if len(df) == 0:
            return df

        df_clean = df.copy()

        critical_columns = ['Violation_ID', 'Violation_Type', 'Date', 'Location']
        df_clean = df_clean.dropna(subset=critical_columns)

        df_clean['Comments'] = df_clean['Comments'].fillna('No comments')
        df_clean['Previous_Violations'] = df_clean['Previous_Violations'].fillna(0)

        categorical_cols = ['Vehicle_Type', 'Driver_Gender', 'Weather_Condition']
        for col in categorical_cols:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].fillna('Unknown')


        text_columns = ['Violation_Type', 'Location', 'Vehicle_Type', 'Driver_Gender']
        for col in text_columns:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].str.strip().str.title()

        if 'Driver_Gender' in df_clean.columns:
            valid_genders = ['Male', 'Female', 'Other']
            df_clean['Driver_Gender'] = df_clean['Driver_Gender'].apply(
                lambda x: x if x in valid_genders else 'Other'
            )


        df_clean = df_clean.drop_duplicates(subset=['Violation_ID'], keep='first')

        if 'Location' in df_clean.columns:
            valid_states = ['Karnataka', 'Punjab', 'Maharashtra', 'Uttar Pradesh',
                            'West Bengal', 'Delhi', 'Gujarat', 'Tamil Nadu']
            df_clean['Location'] = df_clean['Location'].apply(
                lambda x: x if x in valid_states else 'Unknown'
            )
        df_clean = df_clean.dropna(subset=['Violation_ID'])
        df_clean = df_clean.drop_duplicates(subset=['Violation_ID'])

        return df_clean

    def get_cleaning_report(self, original_df, cleaned_df):
        """Generate a report of cleaning operations performed"""
        report = {
            'original_rows': len(original_df),
            'cleaned_rows': len(cleaned_df),
            'rows_removed': len(original_df) - len(cleaned_df),
            'columns_processed': list(cleaned_df.columns),
            'missing_values': cleaned_df.isnull().sum().to_dict(),
            'data_types': cleaned_df.dtypes.to_dict()
        }
        return report