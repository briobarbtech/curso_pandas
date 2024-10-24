import pandas as pd

### Imprimimos una serie
# print(pd.Series([1,3,5,7,12]))
### Definimos un dicciionario
datos = {
    'nombres':["Ana","José","Mar","Ramón"],
    'edades':[12,16,65,23]
}
### imprimimos un dataframe
# print(pd.DataFrame(datos))

### Para leer un archivo csv usamos read_csv
df = pd.read_csv('datos.csv')
### Para ver los primeros 5 elementos usamos el método head()
"""
print(df.head())
"""

### Para ver las dimensiones de la tabla usamos shape
"""
print(df.shape)
"""
### Para ordenar la tabla usamos sort_values()
""" 
print(df.sort_values('Goles',ascending=False))
"""
### Para filtrar valores usamos 
""" 
print(df[df['Goles'] > 100])
"""
### Filtramos por tipo de datos
""" 
print(df.select_dtypes(include='int64'))
"""
### Para ver el nombre de las columnas usamos
""" 
print(df.columns) 
"""
### Para agregar/quitar una columna a un dataframe
""" 
df['Nacionalidad'] = ['Argentina', 'Italia', 'Brasil', 'Alemania', 'Países Bajos', 'Brasil', 'Francia', 'Italia', 'Argentina', 'Gales']
print(df.head())
df = df.drop('Nacionalidad',axis=1)
print(df.head()) 
"""
### Delimitar cuántas columnas quiero ver

"""
print(df.iloc[:3,:4])
"""

### Filtrar Columna según un dato
"""
comienza_c_r = df.loc[:,df.columns.str.startswith('N')]
print(comienza_c_r) 
"""
### Filtrar Valores según un dato
""" 
comienza_c_r = df[df['Nombre'].str.startswith('R')]
print(comienza_c_r)
"""
### Para mostrar una fila según un indice
"""
print(df.iloc[0])
"""
### Para agregar una nueva fila
"""
nueva_fila = pd.DataFrame({"Nombre": "Ronaldinho", "Equipo": "Barcelona", "Posición": "Delantero", "Goles": 70, "Partidos": 145}, index=[df.shape[0]])
print(pd.concat([df,nueva_fila]))
"""
### Para reordenar las columnas
""" 
df['Nacionalidad'] = ['Argentina', 'Italia', 'Brasil', 'Alemania', 'Países Bajos', 'Brasil', 'Francia', 'Italia', 'Argentina', 'Gales']
df = df[['Nombre','Nacionalidad','Posición','Equipo','Goles','Partidos']]
print(df.head()) 
"""
### Crear un dataframe desde numpy
"""
import numpy as np

datos = np.array([[1,2,3,5],[2,3,4,5]])

print(pd.DataFrame(datos))

"""