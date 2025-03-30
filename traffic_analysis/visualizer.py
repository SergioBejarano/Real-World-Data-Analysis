import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional
import pandas as pd

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class TrafficVisualizer:
    @staticmethod
    def plot_violation_types(data: pd.Series, save_path: Optional[str] = None,
                             figsize: tuple = (12, 6)) -> None:
        """Plot distribution of violation types with enhanced styling"""
        plt.figure(figsize=figsize)
        ax = data.plot(kind='bar', color=sns.color_palette())

        plt.title('Top Traffic Violation Types', fontsize=14, pad=20)
        plt.ylabel('Percentage of Total Violations', labelpad=10)
        plt.xlabel('Violation Type', labelpad=10)
        plt.xticks(rotation=45, ha='right')

        # Add value labels on bars
        for p in ax.patches:
            ax.annotate(f"{p.get_height():.1f}%",
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 5),
                        textcoords='offset points')

        plt.tight_layout()
        TrafficVisualizer._handle_save_show(save_path)

    @staticmethod
    def plot_temporal_trends(data: pd.Series, save_path: Optional[str] = None,
                             figsize: tuple = (14, 6)) -> None:
        """Plot violations over time with enhanced styling"""
        plt.figure(figsize=figsize)
        ax = data.plot(kind='line', marker='o', linewidth=2, markersize=8)

        plt.title('Traffic Violations Trend Over Time', fontsize=14, pad=20)
        plt.ylabel('Number of Violations', labelpad=10)
        plt.xlabel('Time Period', labelpad=10)
        plt.grid(True, linestyle='--', alpha=0.7)

        # Add value labels for last point
        last_val = data.iloc[-1]
        ax.annotate(f'{last_val:,}',
                    xy=(data.index[-1], last_val),
                    xytext=(10, 10), textcoords='offset points',
                    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                    arrowprops=dict(arrowstyle='->'))

        plt.tight_layout()
        TrafficVisualizer._handle_save_show(save_path)

    @staticmethod
    def plot_geographical_distribution(data: pd.Series, save_path: Optional[str] = None,
                                       figsize: tuple = (12, 6)) -> None:
        """Plot violations by location with enhanced styling"""
        plt.figure(figsize=figsize)
        ax = data.plot(kind='barh', color=sns.color_palette("Blues_r", len(data)))

        plt.title('Locations with Most Traffic Violations', fontsize=14, pad=20)
        plt.xlabel('Number of Violations', labelpad=10)
        plt.ylabel('Location', labelpad=10)

        # Add value labels on bars
        for i, v in enumerate(data.values):
            ax.text(v + 3, i, f"{v:,}", color='black', va='center')

        plt.tight_layout()
        TrafficVisualizer._handle_save_show(save_path)

    @staticmethod
    def plot_time_of_day(data: pd.Series, save_path: Optional[str] = None,
                         figsize: tuple = (10, 6)) -> None:
        """Plot violations by time of day"""
        plt.figure(figsize=figsize)
        data.plot(kind='pie', autopct='%1.1f%%', startangle=90,
                  wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

        plt.title('Distribution of Violations by Time of Day', fontsize=14, pad=20)
        plt.ylabel('')
        plt.tight_layout()
        TrafficVisualizer._handle_save_show(save_path)

    @staticmethod
    def plot_fine_distribution(data: pd.DataFrame, save_path: Optional[str] = None,
                               figsize: tuple = (12, 6)) -> None:
        """Plot distribution of fine amounts"""
        plt.figure(figsize=figsize)
        sns.boxplot(x=data['Fine_Amount'], color='skyblue')

        plt.title('Distribution of Fine Amounts', fontsize=14, pad=20)
        plt.xlabel('Fine Amount (INR)', labelpad=10)
        plt.grid(True, axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        TrafficVisualizer._handle_save_show(save_path)

    @staticmethod
    def plot_driver_age_distribution(data: pd.Series, save_path: Optional[str] = None,
                                     figsize: tuple = (12, 6)) -> None:
        """Plot driver age distribution"""
        plt.figure(figsize=figsize)
        data.plot(kind='bar', color=sns.color_palette("viridis", len(data)))

        plt.title('Driver Age Distribution', fontsize=14, pad=20)
        plt.ylabel('Percentage', labelpad=10)
        plt.xlabel('Age Group', labelpad=10)
        plt.xticks(rotation=45)
        plt.tight_layout()
        TrafficVisualizer._handle_save_show(save_path)

    @staticmethod
    def plot_seasonal_trends(data: pd.Series, save_path: Optional[str] = None,
                             figsize: tuple = (12, 6)) -> None:
        """Plot seasonal trends in violations"""
        plt.figure(figsize=figsize)
        data.plot(kind='bar', color=sns.color_palette("Spectral", len(data)))

        plt.title('Seasonal Trends in Traffic Violations', fontsize=14, pad=20)
        plt.ylabel('Percentage', labelpad=10)
        plt.xlabel('Season', labelpad=10)
        plt.tight_layout()
        TrafficVisualizer._handle_save_show(save_path)

    @staticmethod
    def _handle_save_show(save_path: Optional[str] = None) -> None:
        """Handle saving or showing the plot"""
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()
            plt.close()