import pandas as pd

# Lee el archivo CSV en un DataFrame de pandas
df = pd.read_csv('Nacimientos2020-2023.csv')

#Eliminar columas inecesarias
df = df.drop('anio', axis=1)
df = df.drop('mes', axis=1)
#df = df.drop('tutora_1_edad', axis=1)
#df = df.drop('tutora_1_sexo', axis=1)
#df = df.drop('tutora_1_nacionalidad', axis=1)
#df = df.drop('tutora_2_edad', axis=1)
#df = df.drop('tutora_2_sexo', axis=1)
#df = df.drop('tutora_2_nacionalidad', axis=1)

#Realizo cambios en los nombres de los registros
#Cambios
reemplazos = {
    'Ciudad de México': 'Cdmx',
    'Estado de México': 'Edo. Mex'
}

# Realiza el reemplazo en la columna 'Ciudad'
df['estado_nacimiento'] = df['estado_nacimiento'].replace(reemplazos)
#Guarda el archivo ya normalizado
df.to_csv('Actualizacion-Nacimientos2020-2023.csv', index=False)



#print(df.columns)
#print(df)
#print(df['estado_nacimiento'])