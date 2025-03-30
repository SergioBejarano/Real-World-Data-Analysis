from traffic_analysis.data_loader import DataLoader
from traffic_analysis.data_cleaner import DataCleaner
from traffic_analysis.analyzer import TrafficAnalyzer
from traffic_analysis.visualizer import TrafficVisualizer
import os
import json

def main():
    os.makedirs('plots', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)

    print("Cargando y limpiando datos...")
    loader = DataLoader()
    cleaner = DataCleaner()

    raw_data = loader.load_raw_data()
    clean_data = cleaner.clean_data(raw_data)
    #print(cleaner.get_cleaning_report(raw_data, clean_data))

    clean_data.to_csv('data/processed/clean_traffic_violations.csv', index=False)
    print("Datos limpios guardados en data/processed/clean_traffic_violations.csv")

    print("Analizando datos...")
    analyzer = TrafficAnalyzer(clean_data)


    print("Generando visualizaciones...")

    TrafficVisualizer.plot_violation_types(
        analyzer.get_violation_types_distribution(),
        'plots/violation_types.png'
    )

    TrafficVisualizer.plot_temporal_trends(
        analyzer.get_temporal_trends(),
        'plots/time_analysis.png'
    )

    TrafficVisualizer.plot_geographical_distribution(
        analyzer.get_geographical_distribution(),
        'plots/regional_distribution.png'
    )

    TrafficVisualizer.plot_time_of_day(
        analyzer.get_time_of_day_analysis(),
        'plots/time_of_day_distribution.png'
    )

    if 'Fine_Amount' in clean_data.columns:
        TrafficVisualizer.plot_fine_distribution(
            clean_data,
            'plots/fine_amount_distribution.png'
        )

    if 'Driver_Age' in clean_data.columns:
        TrafficVisualizer.plot_driver_age_distribution(
            analyzer.get_driver_demographics(by='Age'),
            'plots/driver_age_distribution.png'
        )

    if 'Driver_Gender' in clean_data.columns:
        TrafficVisualizer.plot_driver_age_distribution(
            analyzer.get_driver_demographics(by='Gender'),
            'plots/driver_gender_distribution.png'
        )

    print("Proceso completado. Gráficas guardadas en la carpeta plots/")

if __name__ == "__main__":
    main()