import matplotlib.pyplot as plt
import os
import seaborn as sns
import pandas as pd

def plot_accidents_by_month(data, output_dir):
    """
    Graph of the number of accidents per month.
    """
    data['MES'] = data['FECHA ACCIDENTE'].dt.month
    accidents_by_month = data.groupby('MES').size()

    plt.figure(figsize=(10, 6))
    accidents_by_month.plot(kind='bar', color='skyblue')
    plt.title('Número de Accidentes por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Número de Accidentes')
    plt.xticks(range(12), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'], rotation=45)
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'accidents_by_month.png'))
    plt.close()

def plot_accidents_by_gravity(data, output_dir):
    """
    Graph of the number of accidents by severity.
    """
    accidents_by_gravity = data['GRAVEDAD'].value_counts()

    plt.figure(figsize=(8, 6))
    accidents_by_gravity.plot(kind='bar', color='orange')
    plt.title('Número de Accidentes por Gravedad')
    plt.xlabel('Gravedad')
    plt.ylabel('Número de Accidentes')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'accidents_by_gravity.png'))
    plt.close()


def plot_gravity_vs_class(data, output_dir):
    """
    Generates a heatmap showing the relationship between the severity and the class of the accident.
    """
    # Crear una tabla cruzada para la relación entre gravedad y clase de accidente
    pivot_table = data.pivot_table(index='GRAVEDAD', columns='CLASE ACCIDENTE', aggfunc='size', fill_value=0)

    # Crear el heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Relación entre Gravedad y Clase del Accidente')
    plt.xlabel('Clase de Accidente')
    plt.ylabel('Gravedad')
    plt.tight_layout()

    # Guardar la gráfica
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'gravity_vs_class_heatmap.png'))
    plt.close()


def plot_victims_by_municipality(data, output_dir):
    """
    Graph of the total number of victims by municipality.
    """
    victims_by_municipality = data.groupby('MUNICIPIO')['TOTAL VICTIMAS'].sum().sort_values(ascending=False)

    plt.figure(figsize=(12, 8))
    victims_by_municipality.head(10).plot(kind='bar', color='green')
    plt.title('Total de Víctimas por Municipio (Top 10)')
    plt.xlabel('Municipio')
    plt.ylabel('Total de Víctimas')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'victims_by_municipality.png'))
    plt.close()

def plot_accidents_by_class(data, output_dir):
    """
    Graph of the number of accidents by class.
    """
    accidents_by_class = data['CLASE ACCIDENTE'].value_counts()

    plt.figure(figsize=(10, 6))
    accidents_by_class.plot(kind='bar', color='purple')
    plt.title('Número de Accidentes por Clase')
    plt.xlabel('Clase de Accidente')
    plt.ylabel('Número de Accidentes')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'accidents_by_class.png'))
    plt.close()

def plot_weather_conditions(data, output_dir):
    """
    Graph of the number of accidents by weather conditions.
    """
    weather_conditions = data['ESTADO CLIMA'].value_counts()

    plt.figure(figsize=(10, 6))
    weather_conditions.plot(kind='bar', color='red')
    plt.title('Número de Accidentes por Estado del Clima')
    plt.xlabel('Estado del Clima')
    plt.ylabel('Número de Accidentes')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'weather_conditions.png'))
    plt.close()

def plot_victims_by_hour(data, output_dir):
    """
    Graph of the total number of victims by hour of the accident.
    """
    if 'HORA ACCIDENTE' in data.columns:
        data['HORA ACCIDENTE'] = pd.to_datetime(data['HORA ACCIDENTE'], format='%H:%M', errors='coerce').dt.hour

    victims_by_hour = data.groupby('HORA ACCIDENTE')['TOTAL VICTIMAS'].sum()

    plt.figure(figsize=(12, 6))
    victims_by_hour.plot(kind='line', marker='o', color='blue')
    plt.title('Total de Víctimas por Hora del Accidente')
    plt.xlabel('Hora del Día')
    plt.ylabel('Total de Víctimas')
    plt.xticks(range(0, 24), [f'{h}:00' for h in range(0, 24)], rotation=45)
    plt.grid(True)
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'victims_by_hour.png'))
    plt.close()