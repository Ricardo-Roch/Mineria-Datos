import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap

def cargar_datos(ruta_archivo, nrows=None):
    df = pd.read_csv(ruta_archivo, nrows=nrows)
    return df

def procesar_datos(df):
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

    bins = [0, 18, 25, 35, 45, 55, 65, 100]
    labels = ['0-18', '18-25', '26-35', '36-45', '46-55', '56-65', '66+']
    df['grupo_edad_tutora_1'] = pd.cut(df['tutora_1_edad'], bins=bins, labels=labels, right=False)

    df = df.dropna(subset=['tutora_1_edad', 'grupo_edad_tutora_1'])

    return df

def dividir_datos(df):
    X = df.index.values.reshape(-1, 1)
    y = df['tutora_1_edad']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def entrenar_modelo(X_train, y_train):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    return knn

def evaluar_modelo(modelo, X_test, y_test):
    accuracy = modelo.score(X_test, y_test)
    print(f"Precisión del modelo KNN: {accuracy * 100:.2f}%")

def graficar_dispersion(X_test, y_test, cmap, save_path=None):
    plt.figure(figsize=(15, 6))

    scatter = plt.scatter(X_test, y_test, c=y_test, cmap=cmap, marker='o', alpha=0.7, edgecolors='w')

    plt.title('Gráfica de Dispersión de las Edades y Predicciones')
    plt.xlabel('Índice de Filas')
    plt.ylabel('Edad de Tutora 1')
    plt.colorbar(scatter, label='Edad de Tutora 1')

    plt.xticks([])

    if save_path:
        plt.savefig(save_path)
        print(f"La gráfica ha sido guardada en: {save_path}")
    else:
        plt.show()

def main():
    df = cargar_datos('Actualizacion-Nacimientos2020-2023.csv', nrows=5000)
    df = procesar_datos(df)
    X_train, X_test, y_train, y_test = dividir_datos(df)
    modelo = entrenar_modelo(X_train, y_train)
    evaluar_modelo(modelo, X_test, y_test)
    save_path = 'imagenes/Graficas/P7scatter_dispersion_agrupado.png'
    cmap = ListedColormap(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'])
    graficar_dispersion(X_test, y_test, cmap, save_path)

if __name__ == "__main__":
    main()
#pm
