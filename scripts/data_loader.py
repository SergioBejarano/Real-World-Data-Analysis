import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    :param file_path: Path of the CSV file.
    :return: DataFrame with the loaded data.
    """
    try:
        data = pd.read_csv(file_path, encoding='utf-8', parse_dates=['FECHA ACCIDENTE'], dayfirst=True)
        return data
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None