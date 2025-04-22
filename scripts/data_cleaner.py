import pandas as pd

def clean_data(data):
    """
    Cleans and prepares the data for analysis.
    :param data: DataFrame with the original data.
    :return: Cleaned DataFrame.
    """

    data = data.dropna(subset=['FECHA ACCIDENTE', 'GRAVEDAD', 'CLASE ACCIDENTE', 'MUNICIPIO']).copy()

    if 'ESTADO CLIMA' in data.columns:
        data['ESTADO CLIMA'] = data['ESTADO CLIMA'].str.upper()


    numeric_columns = [
        'NUMERO VICTIMA PEATÓN', 'NUMERO VICTIMA ACOMPAÑANTE', 'NUMERO VICTIMA PASAJERO',
        'NUMERO VICTIMA CONDUCTOR', 'NUMERO VICTIMA HERIDO', 'NUMERO VICTIMA MUERTO'
    ]
    for col in numeric_columns:
        data.loc[:, col] = pd.to_numeric(data[col], errors='coerce').fillna(0)

  
    data['TOTAL VICTIMAS'] = (
        data['NUMERO VICTIMA PEATÓN'] + data['NUMERO VICTIMA ACOMPAÑANTE'] +
        data['NUMERO VICTIMA PASAJERO'] + data['NUMERO VICTIMA CONDUCTOR'] +
        data['NUMERO VICTIMA HERIDO'] + data['NUMERO VICTIMA MUERTO']
    )


    return data