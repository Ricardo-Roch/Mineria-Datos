import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

if not os.path.exists('imagenes/Graficas'):
    os.makedirs('imagenes/Graficas')

df = pd.read_csv('Actualizacion-Nacimientos2020-2023.csv', nrows=185000)#Modificar este parametro para ver mas datos en la grafica o si tu compu tiene mucha galleta
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])

#fecha de inicio para calcular los días transcurridos
fecha_inicio =  df['fecha_nacimiento'].iloc[0]
df['dias_transcurridos'] = (df['fecha_nacimiento'] - fecha_inicio).dt.days

#prom edades
df_promedio = df.groupby('dias_transcurridos')['tutora_1_edad'].mean().reset_index()

#regresión lineal
X = sm.add_constant(df_promedio['dias_transcurridos'])
Y = df_promedio['tutora_1_edad']

#modelo de regresion
modelo = sm.OLS(Y, X).fit()

print(modelo.summary())

plt.figure(figsize=(10, 6))
plt.scatter(df_promedio['dias_transcurridos'], df_promedio['tutora_1_edad'], label='Promedios por Día')
plt.plot(df_promedio['dias_transcurridos'], modelo.predict(X), color='red', label='Recta de Regresión')
plt.xlabel('Días Transcurridos desde {}'.format(fecha_inicio.date()))
plt.ylabel('Promedio de Edad del Tutor 1')
plt.title('Regresion lineal: dias transcurridos vs. promedio de edad del tutor')
plt.legend()

#para que sean enteros
plt.yticks(range(int(min(Y)), int(max(Y))+1))
plt.savefig(os.path.join('imagenes/Graficas', 'Regresion lineal.png'))

plt.tight_layout()
plt.show()
#merge
