# Castañeda Esquivel Jorge Leonardo
# 0202114002

import pandas
datos = {
    'Estudiante': ['Ana','Luis','María','Juan','Carla'],
    'Horas_Usadas': [3,5,2,4,1]
}
df = pandas.DataFrame(datos)
df['Costo_Total'] = df['Horas_Usadas'] * 2.0
print(df.head())
print(df['Costo_Total'].describe())

print(df[df['Costo_Total']>6.0])

print("El gasto promedio fue de",df['Costo_Total'].mean())
print("los estudiantes que gastaron más de 6.00 son: \n",df[df['Costo_Total']>6.0])