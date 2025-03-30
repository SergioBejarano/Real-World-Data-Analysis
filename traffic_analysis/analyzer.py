import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, Union, Optional

class TrafficAnalyzer:
    def __init__(self, clean_df: pd.DataFrame):
        """Initialize with cleaned DataFrame and validate input"""
        self._validate_input(clean_df)
        self.df = clean_df.copy()
        self._add_derived_columns()

    def _validate_input(self, df: pd.DataFrame) -> None:
        """Validate input DataFrame"""
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        if len(df) == 0:
            raise ValueError("DataFrame is empty")
        required_cols = ['Violation_Type', 'Date', 'Location']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

    def _add_derived_columns(self) -> None:
        """Add useful derived columns for analysis"""
        # Temporal features
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
        self.df['Year'] = self.df['Date'].dt.year
        self.df['Month'] = self.df['Date'].dt.month
        self.df['MonthName'] = self.df['Date'].dt.month_name()
        self.df['DayOfWeek'] = self.df['Date'].dt.day_name()
        self.df['DayOfWeekNum'] = self.df['Date'].dt.dayofweek
        self.df['Quarter'] = self.df['Date'].dt.quarter

        # Time features
        if 'Time' in self.df.columns:
            self.df['Hour'] = pd.to_datetime(self.df['Time'], format='%H:%M').dt.hour
            self.df['TimeOfDay'] = pd.cut(self.df['Hour'],
                                          bins=[0, 6, 12, 18, 24],
                                          labels=['Night', 'Morning', 'Afternoon', 'Evening'],
                                          right=False)

        # Fine amount categories
        if 'Fine_Amount' in self.df.columns:
            bins = [0, 1000, 2000, 3000, 4000, 5000, np.inf]
            labels = ['<1K', '1K-2K', '2K-3K', '3K-4K', '4K-5K', '5K+']
            self.df['Fine_Category'] = pd.cut(self.df['Fine_Amount'], bins=bins, labels=labels)

    def get_violation_types_distribution(self, top_n: int = 10) -> pd.Series:
        """Get distribution of violation types"""
        return (self.df['Violation_Type'].value_counts(normalize=True)
                .mul(100).round(2).head(top_n))

    def get_temporal_trends(self, frequency: str = 'M') -> pd.Series:
        """Analyze violations by time period"""
        valid_frequencies = {'D': 'Daily', 'W': 'Weekly', 'M': 'Monthly',
                             'Q': 'Quarterly', 'Y': 'Yearly'}
        if frequency not in valid_frequencies:
            raise ValueError(f"Frequency must be one of {list(valid_frequencies.keys())}")
        return self.df.groupby(self.df['Date'].dt.to_period(frequency)).size()

    def get_geographical_distribution(self, top_n: int = 10) -> pd.Series:
        """Analyze violations by location"""
        return self.df['Location'].value_counts().head(top_n)

    def get_violation_by_vehicle_type(self) -> pd.DataFrame:
        """Analyze violations by vehicle type"""
        if 'Vehicle_Type' not in self.df.columns:
            raise ValueError("Vehicle_Type column not found")
        return (self.df.groupby('Vehicle_Type')['Violation_Type']
                .value_counts(normalize=True)
                .mul(100).round(2)
                .unstack().fillna(0))

    def get_time_of_day_analysis(self) -> pd.Series:
        """Analyze violations by time of day"""
        if 'TimeOfDay' not in self.df.columns:
            raise ValueError("TimeOfDay column not found - check if Time column exists")
        return (self.df['TimeOfDay'].value_counts(normalize=True)
                .mul(100).round(2).sort_index())

    def get_driver_demographics(self, by: str = 'Gender') -> pd.Series:
        """Analyze violations by driver demographics"""
        if by == 'Gender' and 'Driver_Gender' in self.df.columns:
            return (self.df['Driver_Gender'].value_counts(normalize=True)
                    .mul(100).round(2))
        elif by == 'Age' and 'Driver_Age' in self.df.columns:
            age_bins = [0, 20, 30, 40, 50, 60, 70, 100]
            age_labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
            return (pd.cut(self.df['Driver_Age'], bins=age_bins, labels=age_labels)
                    .value_counts(normalize=True).mul(100).round(2).sort_index())
        else:
            raise ValueError(f"Invalid demographic option or column not found: {by}")

    def get_fine_amount_analysis(self) -> Dict[str, float]:
        """Get statistics about fine amounts"""
        if 'Fine_Amount' not in self.df.columns:
            raise ValueError("Fine_Amount column not found")
        stats = self.df['Fine_Amount'].describe().to_dict()
        return {k: round(v, 2) for k, v in stats.items()}

