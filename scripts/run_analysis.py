from data_loader import load_data
from data_cleaner import clean_data
from data_visualizer import (
    plot_accidents_by_month,
    plot_accidents_by_gravity,
    plot_victims_by_municipality,
    plot_accidents_by_class,
    plot_weather_conditions,
    plot_gravity_vs_class,
    plot_victims_by_hour
)
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent.parent  
    data_file = base_dir / 'data' / 'Accidentes_de_tr_nsito_reportados_en_los_municipios_que_tienen_convenio_con_la_Gerencia_de_Seguridad_Vial_de_Antioquia_20250421.csv'
    if not data_file.exists():
        print(f"Error: El archivo de datos no se encuentra en la ruta: {data_file}")
        return
    output_dir = base_dir / 'plots'
    data = load_data(data_file)
    if data is None:
        print("Error: No se pudieron cargar los datos.")
        return
    clean_data_df = clean_data(data)
    plot_gravity_vs_class(data, output_dir)
    plot_accidents_by_month(clean_data_df, output_dir)
    plot_accidents_by_gravity(clean_data_df, output_dir)
    plot_victims_by_municipality(clean_data_df, output_dir)
    plot_accidents_by_class(clean_data_df, output_dir)
    plot_weather_conditions(clean_data_df, output_dir)
    plot_victims_by_hour(clean_data_df, output_dir)

if __name__ == '__main__':
    main()