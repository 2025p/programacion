# Datos de temperaturas (ejemplo)
temperaturas = {
    " Guayaquil":[
        [35, 36, 37, 39, 38, 40, 37],  # Semana 1
        [30, 31, 32, 30, 33, 32, 31],  # Semana 2
        [28, 29, 30, 32, 31, 34, 32],  # Semana 3
        [31, 32, 33, 35, 34, 32, 31],  # Semana 4

    ],
    " Quevedo":[
        [30, 31, 32, 35, 34, 32, 33],  # Semana 1
        [28, 29, 30, 31, 32, 29, 28],  # Semana 2
        [34, 35, 36, 38, 37, 33, 34],  # Semana 3
        [36, 37, 38, 39, 38, 37, 35],  # Semana 4


    ],
    " Santo Domingo":[
        [32, 33, 34, 35, 34, 33, 32],  # Semana 1
        [27, 28, 30, 31, 32, 28, 29],  # Semana 2
        [32, 33, 34, 36, 37, 35, 34],  # Semana 3
        [37, 38, 39, 40, 38, 37, 35],  # Semana 4
    ],
    
}

# Funcion para calcular el promedio
def calcular_promedio(lista):
    return sum (lista) / len(lista) 

# Calcular y mostrar promedios
for ciudad,semanas in temperaturas.items():
    for i, semana in enumerate(semanas):
      promedio = calcular_promedio(semana)
      print(f"Promedio de temperaturas en la ciudad de {ciudad}, Semana {i+1}: {promedio:.2f} °C (Grados celsius)")
