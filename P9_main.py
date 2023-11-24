import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def generar_grafica(df, nombre_archivo, num_registros):
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

    #fecha de inicio para calcular los días transcurridos
    fecha_inicio = df['fecha_nacimiento'].iloc[0]
    df['dias_transcurridos'] = (df['fecha_nacimiento'] - fecha_inicio).dt.days


    df_promedio = df.groupby('dias_transcurridos')['tutora_1_edad'].mean().reset_index()

    #egresión
    X = sm.add_constant(df_promedio['dias_transcurridos'])
    Y = df_promedio['tutora_1_edad']
    modelo = sm.OLS(Y, X).fit()

    #Intervalo
    confianza_intervalo = modelo.get_prediction(X).conf_int()

    #forecasting
    dias_futuros = pd.DataFrame({'dias_transcurridos': range(df_promedio['dias_transcurridos'].max() + 1, df_promedio['dias_transcurridos'].max() + 100)})
    X_futuro = sm.add_constant(dias_futuros['dias_transcurridos'])
    prediccion_futuro = modelo.predict(X_futuro)

    #grafica
    plt.figure(figsize=(10, 6))
    plt.scatter(df_promedio['dias_transcurridos'], df_promedio['tutora_1_edad'], label='Edades', alpha=0.7)
    plt.plot(df_promedio['dias_transcurridos'], modelo.predict(X), color='red', label='Recta de Regresión')
    plt.plot(dias_futuros['dias_transcurridos'], prediccion_futuro, linestyle='dashed', color='blue', label='Forecasting')


    plt.fill_between(df_promedio['dias_transcurridos'], confianza_intervalo[:, 0], confianza_intervalo[:, 1], color='gray', alpha=0.3, label='Intervalo de Confianza')


    plt.xlabel('Días Transcurridos desde {}'.format(fecha_inicio.date()))
    plt.ylabel('Edad del Tutor 1')
    plt.title('Regresion lineal: días transcurridos vs. promedio de edad del tutor con Forecasting ({} registros)'.format(num_registros))
    plt.legend()
    plt.yticks(range(int(min(Y)), int(max(Y)) + 1))
    plt.savefig(os.path.join('imagenes/Graficas', nombre_archivo))
    plt.tight_layout()
    plt.show()

#Generar gráfica con 5,000 registros
df_5k = pd.read_csv('Actualizacion-Nacimientos2020-2023.csv', nrows=5000)
generar_grafica(df_5k, 'P9_Regresion_lineal_con_Forecasting.png', 5000)

#generar gráfica con 60,000 registros
df_60k = pd.read_csv('Actualizacion-Nacimientos2020-2023.csv', nrows=60000)
generar_grafica(df_60k, 'P9_Regresion_lineal_con_Forecasting2.png', 60000)

#generar gráfica con 175,000 registros
df_175k = pd.read_csv('Actualizacion-Nacimientos2020-2023.csv', nrows=175000)
generar_grafica(df_175k, 'P9_Regresion_lineal_con_Forecasting3.png', 175000)
