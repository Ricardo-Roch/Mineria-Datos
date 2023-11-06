import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el DataFrame con tu archivo CSV
df = pd.read_csv("Actualizacion-Nacimientos2020-2023.csv")

# Función para crear grupos de edades
def create_age_groups(df):
    age_groups = []
    for age in df['tutora_1_edad']:
        if age >= 0 and age <= 18:
            age_group = '0-18'
        elif age >= 19 and age <= 30:
            age_group = '19-30'
        elif age >= 31 and age <= 50:
            age_group = '31-50'
        else:
            age_group = '51-100'
        age_groups.append(age_group)
    df['age_group'] = age_groups

# Llamar a la función para crear grupos de edades
create_age_groups(df)

# Convertir la columna "tutora_1_nacionalidad" a cadenas
df['tutora_1_nacionalidad'] = df['tutora_1_nacionalidad'].astype(str)

# Definir una paleta de colores personalizada para cada rango de edad
colors = {'0-18': 'red', '19-30': 'green', '31-50': 'blue', '51-100': 'purple'}

# Función para realizar el scatter plot de los grupos de edades con colores personalizados y guardar la gráfica
def scatter_age_groups(df, x_column, y_column, label_column, k_neighbors):
    fig, ax = plt.subplots()
    labels = df[label_column].unique()

    for label in labels:
        filter_df = df[df[label_column] == label]
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=colors[label])

    ax.legend()
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Scatter Plot de Grupos de Edades')
    plt.savefig('imagenes/Graficas/scatter_dispersion_agrupado.png')  # Guardar la gráfica en un archivo
    plt.show()

# Llamar a la función para crear el scatter plot de grupos de edades con k=5 y guardar la gráfica
scatter_age_groups(df, 'tutora_1_edad', 'tutora_1_nacionalidad', 'age_group', k_neighbors=5)

# Función para realizar el scatter plot de "tutora_1_nacionalidad" y el promedio de "tutora_2_edad"
def scatter_nationality_avg_age(df, x_column, y_column):
    fig, ax = plt.subplots()

    # Calcular el promedio de "tutora_2_edad" para cada "tutora_1_nacionalidad"
    avg_age_by_nationality = df.groupby(x_column)[y_column].mean()
    unique_nationalities = avg_age_by_nationality.index

    # Definir una paleta de colores para los puntos en el scatter plot
    colors = plt.cm.jet(np.linspace(0, 1, len(unique_nationalities)))

    for i, nationality in enumerate(unique_nationalities):
        avg_age = avg_age_by_nationality[nationality]
        ax.scatter(nationality, avg_age, label=nationality, color=colors[i])

    ax.legend()
    plt.xlabel(x_column)
    plt.ylabel(f'Promedio de {y_column}')
    plt.title(f'Scatter Plot de Nacionalidad de Tutora 1 vs. Promedio de {y_column}')
    plt.xticks(rotation=45)
    plt.savefig('imagenes/Graficas/scatter_nacionalidad_vs_promedio_edad_tutora_2.png')  # Guardar la gráfica en un archivo
    plt.show()

# Llamar a la función para crear el scatter plot de "tutora_1_nacionalidad" y el promedio de "tutora_2_edad"
scatter_nationality_avg_age(df, 'tutora_1_nacionalidad', 'tutora_2_edad')
