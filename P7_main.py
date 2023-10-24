from statistics import mode
from typing import Tuple, List
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate

df = pd.read_csv('Actualizacion-Nacimientos2020-2023.csv')

def imprime_tabla(df: pd.DataFrame):
    print(tabulate(df, headers='keys', tablefmt="orgtbl"))

def normalize_distribution(dist: np.array, n: int) -> np.array:
    b = dist - min(dist) + 0.000001
    c = (b / np.sum(b)) * n
    return np.round(c)

def create_distribution(mean: float, size: int) -> pd.Series:
    return pd.Series(normalize_distribution(np.random.standard_normal(size), mean * size))

def generate_df(edades: List[int], etiquetas: List[str], n: int) -> pd.DataFrame:
    groups = [(np.random.uniform(edades[i], edades[i + 1]), np.random.uniform(edades[i], edades[i + 1]), etiquetas[i]) for i in range(len(edades) - 1)]
    lists = [
        (create_distribution(_x, n), create_distribution(_y, n), np.repeat(_l, n))
        for _x, _y, _l in groups
    ]
    x = np.array([])
    y = np.array([])
    labels = np.array([])
    for _x, _y, _l in lists:
        x = np.concatenate((x, _x), axis=None)
        y = np.concatenate((y, _y))
        labels = np.concatenate((labels, _l))
    return pd.DataFrame({"x": x, "y": y, "label": labels})

def scatter_group_by(file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = plt.get_cmap("hsv", len(labels) + 1)

    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))

    ax.legend()
    plt.xlabel("Eje X")  # Etiqueta del eje X
    plt.ylabel("Eje Y")  # Etiqueta del eje Y
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neightbors(points: np.array, labels: np.array, input_data: List[np.array], k: int):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]

    predicted_labels = [
        np.argmax(np.bincount([label_to_number[labels[index]] for index in point_nearest]))
        for point_nearest in points_k_nearest
    ]

    return predicted_labels


edades = [0, 18, 30, 50, 100]
etiquetas = ['0-18', '19-30', '31-50', '51-100']

#columna "GrupoEdad" que contendrá las etiquetas de los grupos
df['GrupoEdad'] = pd.cut(df['tutora_2_edad'], bins=edades, labels=etiquetas)

#dataFrame basado en las edades y etiquetas definidas
df_grupos = generate_df(edades, etiquetas, 50)

#diccionario que asigna etiquetas a números
label_to_number = {label: i for i, label in enumerate(df_grupos['label'].unique())}
number_to_label = {i: label for i, label in enumerate(df_grupos['label'].unique())}

scatter_group_by("imagenes/Graficas/grafico_dispersion_agrupado.png", df_grupos, "x", "y", "label")

input_data = [np.array([100, 150]), np.array([1, 1]), np.array([1, 300]), np.array([80, 40])]
k = 5
predicted_labels = k_nearest_neightbors(df_grupos[['x', 'y']].to_numpy(), df_grupos['label'].to_numpy(), input_data, k)

print(predicted_labels)
