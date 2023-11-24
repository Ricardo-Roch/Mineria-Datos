import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

def cargar_datos(ruta_archivo, nrows=None):
    df = pd.read_csv(ruta_archivo, nrows=nrows)
    return df

def procesar_datos(df):
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])
    return df

def aplicar_kmeans(df, num_clusters=3):
    # Eliminar filas con valores NaN
    df = df.dropna(subset=['tutora_1_edad'])

    # Seleccionar las características para el clustering
    X = df[['tutora_1_edad']]

    # Crear el modelo K-Means
    kmeans = KMeans(n_clusters=num_clusters, random_state=3, n_init=10)

    # Ajustar el modelo a las características
    kmeans.fit(X)

    # Crear una copia del DataFrame para evitar SettingWithCopyWarning
    df = df.copy()

    # Asignar los valores de los clústeres en la nueva copia del DataFrame
    df.loc[:, 'Cluster'] = kmeans.labels_

    return df, kmeans.cluster_centers_



def asignar_colores_por_cluster(df):
    return df['Cluster'].tolist()

def graficar_dispersion(df, colores, save_path=None):
    plt.figure(figsize=(15, 6))

    scatter = plt.scatter(df.index, df['tutora_1_edad'], c=colores, cmap='viridis', marker='o', alpha=0.7, edgecolors='w')

    plt.title('Gráfica de Dispersión de las Edades y Agrupación con K-Means')
    plt.xlabel('Índice de Filas')
    plt.ylabel('Edad de Tutora 1')
    plt.colorbar(scatter, label='Cluster')

    plt.xticks([])

    if save_path:
        plt.savefig(save_path)
        print(f"La gráfica ha sido guardada en: {save_path}")
    else:
        plt.show()

def visualizar_centros_de_masa(centros_de_masa, cmap, save_path=None):
    plt.figure(figsize=(10, 4))
    plt.scatter(np.random.rand(len(centros_de_masa)), centros_de_masa, c=range(len(centros_de_masa)), cmap=cmap, marker='x', s=100)
    plt.title('Centros de Masa de los Clusters')
    plt.xlabel('Aleatorio')

    if save_path:
        plt.savefig(save_path)
        print(f"La gráfica ha sido guardada en: {save_path}")
    else:
        plt.show()

def main():
    df = cargar_datos('Actualizacion-Nacimientos2020-2023.csv', nrows=1500)
    df = procesar_datos(df)

    # Aplicar K-Means
    df, centros_de_masa = aplicar_kmeans(df)

    # Asignar colores por el número de cluster
    colores = asignar_colores_por_cluster(df)

    # Visualizar los resultados de K-Means y guardar la gráfica
    graficar_dispersion(df, colores, save_path='imagenes/Graficas/P8scatter_centrodemasa.png')

    # Visualizar los centros de masa y guardar la gráfica
    visualizar_centros_de_masa(centros_de_masa, 'viridis', save_path='imagenes/Graficas/P8centros_de_masa.png')

if __name__ == "__main__":
    main()
#pm
