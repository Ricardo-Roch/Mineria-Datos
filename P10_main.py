import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def cargar_datos(csv_path, columna):
    df = pd.read_csv(csv_path)
    textos = df[columna].dropna().astype(str)
    return textos

def limpiar_texto(texto, palabras_no_deseadas):
    for palabra in palabras_no_deseadas:
        texto = texto.replace(palabra, '')
    return texto

def contar_palabras(texto):
    texto_completo = ' '.join(texto)
    return Counter(texto_completo.split())

def generar_nube_palabras(conteo_palabras, nombre_archivo, titulo):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(conteo_palabras)
    ruta_guardado = f'imagenes/Graficas/{nombre_archivo}.png'
    wordcloud.to_file(ruta_guardado)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Añade un título a la nube de palabras
    plt.title(titulo)

    plt.show()

csv_path = 'Actualizacion-Nacimientos2020-2023.csv'
columna_interes = 'alcaldia_nacimiento'
palabras_no_deseadas = ['La', 'A.', 'Alta']
textos = cargar_datos(csv_path, columna_interes)
textos_limpios = textos.apply(lambda x: limpiar_texto(x, palabras_no_deseadas))
conteo_palabras = contar_palabras(textos_limpios)
nombre_archivo = 'P10_Nube-palabras'
titulo_nube = 'Nube de Palabras - Alcaldías de Nacimiento'
generar_nube_palabras(conteo_palabras, nombre_archivo, titulo_nube)
