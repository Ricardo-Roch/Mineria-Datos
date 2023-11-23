import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os  # Importar el módulo os para manejar directorios

df = pd.read_csv('Actualizacion-Nacimientos2020-2023.csv')
output_dir = 'imagenes/Graficas'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def grafica_conteo_sexo(df):
    #Cuenta registros por género
    conteo_sexo = df['sexo'].value_counts()
    #Gráfica de barras
    plt.bar(conteo_sexo.index, conteo_sexo.values)
    #Cosas Grafica
    plt.xlabel('Género')
    plt.ylabel('Cantidad de Registros')
    plt.title('Cantidad de Registros por Género')
    plt.savefig(os.path.join(output_dir, 'grafica_conteo_sexo.png'))

    #muestra la gráfica
    plt.show()

def grafica_histograma_combinaciones_sexo_tutoras(df):
    plt.figure(figsize=(12, 6))  # Ajustar el tamaño
    # Filtrar por combinaciones de tutoras
    mujer_mujer = df[(df['tutora_1_sexo'] == 'Mujer') & (df['tutora_2_sexo'] == 'Mujer')]
    hombre_hombre = df[(df['tutora_1_sexo'] == 'Hombre') & (df['tutora_2_sexo'] == 'Hombre')]

    # Crear histograma
    plt.hist([mujer_mujer['tutora_1_edad'], hombre_hombre['tutora_1_edad']], bins=20, alpha=0.7, label=['Mujer-Mujer', 'Hombre-Hombre'])

    # Etiquetas y título
    plt.xlabel('Edad del Tutor 1 y Tutor 2')
    plt.ylabel('Cantidad de Personas')
    plt.title('Histograma de Edades de los Tutores 1 y 2 por Combinación de Tutoras')

    # Establecer las edades en el eje X
    edades = sorted(set(mujer_mujer['tutora_1_edad']).union(set(hombre_hombre['tutora_1_edad'])))
    plt.xticks(edades)

    # Mostrar leyenda
    plt.legend()

    # Ajustar diseño y guardar la gráfica
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_histograma_combinaciones_sexo_tutoras.png'))

    # Mostrar la gráfica
    plt.show()

def grafica_nacimientos_por_mes(df):
    #'fecha_nacimiento' al tipo de dato datetime
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])
    # el mes de la fecha de nacimiento y crear una nueva columna 'mes'
    df['mes'] = df['fecha_nacimiento'].dt.strftime('%Y-%m')
    #filtrar por niños
    niños_df = df[df['sexo'] == 'Hombre']
    conteo_nacimientos_niños = niños_df['mes'].value_counts().sort_index()
    #filtrar por niñas
    niñas_df = df[df['sexo'] == 'Mujer']
    conteo_nacimientos_niñas = niñas_df['mes'].value_counts().sort_index()
    #gráficas de puntos para niños y niñas
    plt.figure(figsize=(12, 6))  # Ajusta el tamaño de la figura
    #Gráfica  niños
    plt.scatter(conteo_nacimientos_niños.index, conteo_nacimientos_niños.values, marker='o', s=50, label='Niños (Hombres)')
    #Gráfica niñas
    plt.scatter(conteo_nacimientos_niñas.index, conteo_nacimientos_niñas.values, marker='o', s=50, label='Niñas (Mujeres)')
    plt.xlabel('Mes de Nacimiento')
    plt.ylabel('Cantidad de Nacimientos')
    plt.title('Cantidad de Nacimientos por Mes (Niños vs. Niñas)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_nacimientos_por_mes.png'))
    plt.show()

def grafica_histograma_edad_tutora(df):
    plt.figure(figsize=(10, 6))  # Ajustar el tamaño
    #cosas del histograma
    plt.hist(df['tutora_1_edad'], bins=20, edgecolor='k', alpha=0.7)
    #etiquetas
    plt.xlabel('Edad del Tutor 1')
    plt.ylabel('Cantidad de Personas')
    plt.title('Histograma de Edades del Tutor 1')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_histograma_edad_tutora.png'))
    plt.show()

def grafica_distribucion_nacimientos_por_estado(df):
    #filtrar por niños
    niños_df = df[df['sexo'] == 'Hombre']
    pivot_table = pd.pivot_table(niños_df, values='sexo', index='estado_nacimiento', aggfunc='count')
    pivot_table = pivot_table.sort_values(by='sexo', ascending=False)
    #aplico escala logarítmica a los valores
    pivot_table['log_sexo'] = pivot_table['sexo'].apply(lambda x: max(1, x))  # Evitar log(0)
    plt.figure(figsize=(12, 6))
    ax = plt.gca()
    ax.set_yscale('log')
    pivot_table.plot(kind='area', y='log_sexo', colormap='Set3', legend=False, ax=ax)
    #etiquetas
    plt.xlabel('Estado de Nacimiento')
    plt.ylabel('Cantidad de Niños Nacidos (en escala logarítmica)')
    plt.title('Distribución de Niños Nacidos por Estado de Nacimiento')
    etiquetas_a_mostrar = 10
    etiquetas = pivot_table.index[::len(pivot_table) // etiquetas_a_mostrar]
    ax.set_xticks(pivot_table.index.get_indexer(etiquetas))
    ax.set_xticklabels(etiquetas, rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_distribucion_nacimientos_por_estado.png'))
    plt.show()

def grafica_tutores_ededad_nacionalidad(df):
    df['fecha'] = pd.to_datetime(df['fecha_nacimiento'])
    tutora_1_hombre = df[df['tutora_1_sexo'] == 'Hombre']
    tutora_1_mujer = df[df['tutora_1_sexo'] == 'Mujer']
    tutora_2_hombre = df[df['tutora_2_sexo'] == 'Hombre']
    tutora_2_mujer = df[df['tutora_2_sexo'] == 'Mujer']
    intervalo = '3M'
    tutora_1_hombre = tutora_1_hombre.resample(intervalo, on='fecha')['tutora_1_sexo'].count()
    tutora_1_mujer = tutora_1_mujer.resample(intervalo, on='fecha')['tutora_1_sexo'].count()
    tutora_2_hombre = tutora_2_hombre.resample(intervalo, on='fecha')['tutora_2_sexo'].count()
    tutora_2_mujer = tutora_2_mujer.resample(intervalo, on='fecha')['tutora_2_sexo'].count()
    # Aplicar escala logarítmica a los valores en el eje y
    tutora_1_hombre = np.log1p(tutora_1_hombre)
    tutora_1_mujer = np.log1p(tutora_1_mujer)
    tutora_2_hombre = np.log1p(tutora_2_hombre)
    tutora_2_mujer = np.log1p(tutora_2_mujer)
    plt.figure(figsize=(12, 6))
    # Trazar las líneas para cada categoría
    plt.plot(tutora_1_hombre.index, tutora_1_hombre.values, label='Tutora 1 - Hombre')
    plt.plot(tutora_1_mujer.index, tutora_1_mujer.values, label='Tutora 1 - Mujer')
    plt.plot(tutora_2_hombre.index, tutora_2_hombre.values, label='Tutora 2 - Hombre')
    plt.plot(tutora_2_mujer.index, tutora_2_mujer.values, label='Tutora 2 - Mujer')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad (en escala Logarítmica)')
    plt.title('Géneros de Tutores (Agrupado por cada 3 Meses)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_tutores_ededad_nacionalidad.png'))
    plt.show()



# Llamar a las funciones con tu DataFrame 'df'
grafica_conteo_sexo(df)
grafica_nacimientos_por_mes(df)
grafica_histograma_edad_tutora(df)
grafica_distribucion_nacimientos_por_estado(df)
grafica_tutores_ededad_nacionalidad(df)
grafica_histograma_combinaciones_sexo_tutoras(df)
