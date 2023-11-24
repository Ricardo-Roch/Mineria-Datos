import pandas as pd

df = pd.read_csv('Actualizacion-Nacimientos2020-2023.csv')

edad_promedio_tutora1 = df['tutora_1_edad'].mean()
conteo_sexo = df['sexo'].value_counts()
estado_nacimiento_mas_comun = df['estado_nacimiento'].mode()[0]
min_tutora_1_edad = int(df['tutora_1_edad'].min())
max_tutora_2_edad = int(df['tutora_2_edad'].max())
sumatoria_tutora_1_edad = df['tutora_1_edad'].sum()
varianza_tutora_2_edad = df['tutora_2_edad'].var()
desviacion_estandar_tutora_2_edad = df['tutora_2_edad'].std()
asimetria_tutora_1_edad = df['tutora_1_edad'].skew()
kurtosis_tutora_2_edad = df['tutora_2_edad'].kurtosis()

print('Edad Promedio tutor 1:', edad_promedio_tutora1)                                      #Media
print('Conteo de niños:\n',conteo_sexo)                                                     #Conteo
print('Ncionalidad mas comun tutor 2:',estado_nacimiento_mas_comun)                         #Moda
print('Edad mínima del tutor 1:', min_tutora_1_edad)                                        #Mínimo
print('Edad máxima del tutor 2 edad:', max_tutora_2_edad)                                   #Máximo
print('Sumatoria del tutor 1 edad:', sumatoria_tutora_1_edad)                               #Sumatoria
print('Varianza del tutor 2:', varianza_tutora_2_edad)                                      #Varianza
print('Desviación estándar del tutor 2:', desviacion_estandar_tutora_2_edad)                #DsvEst
print('Asimetria del tutor 1:', asimetria_tutora_1_edad)                                    #Asimetria
print('Kurtosis del tutor 2:', kurtosis_tutora_2_edad)                                      #Kurtosis



mujer_mujer = df[(df['tutora_1_sexo'] == 'Mujer') & (df['tutora_2_sexo'] == 'Mujer')]
hombre_hombre = df[(df['tutora_1_sexo'] == 'Hombre') & (df['tutora_2_sexo'] == 'Hombre')]
conteo_mujer_mujer = len(mujer_mujer)
conteo_hombre_hombre = len(hombre_hombre)

hm=conteo_mujer_mujer+conteo_hombre_hombre
print(f"Cantidad de combinaciones mujer-mujer: {conteo_mujer_mujer}")
print(f"Cantidad de combinaciones hombre-hombre: {conteo_hombre_hombre}")
print(f"Cantidad de combinaciones: {hm}")



# Contar cuántos tutores tienen la edad mínima
tutores_minima_edad = df[df['tutora_1_edad'] == min_tutora_1_edad]
conteo_tutores_minima_edad = len(tutores_minima_edad)

#tutores_maxima_edad = df[df['tutora_2_edad'] == max_tutora_2_edad]
#conteo_tutores_maxima_edad = len(tutores_maxima_edad)

# Imprimir los resultados
print(f"Cantidad de tutores con la edad mínima: {conteo_tutores_minima_edad}")
#print(f"Cantidad de tutores con la edad máxima: {conteo_tutores_maxima_edad}")
