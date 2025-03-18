def temperaturas_promedio(ciudades_temperaturas):
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len (temperaturas)
        temperaturas_promedio[ciudad] = promedio

        return temperaturas_promedio
    
    ciudades_temperaturas = {
        "Quito" [25,28,24,26],
        "Guayaquil" [21,23,22,24],
        "Cuenca" [28,26,27,225],
        "Salinas" [24,23,25,27]
    }

    temperaturas_promedio = temperaturas_promedio(ciudades_temperaturas)

    print("Temperaturas Promediopor Ciudades:")
    for ciudad, promedio in temperaturas_promedio.items():
        print(f"{ciudad}: {promedio: .2f}°C")


        

def calcular_temperatura_promedio(datos_temperaturas):
    ""
    #Calcula la temperatura promedio de ciudades durante varias semanas.

    
    datos_temperaturas (dict):
     # Un diccionario donde las claves son nombres de ciudades y los valores son listas de listas, representando temperaturas semanales. Ejemplo:
{
        "Ciudad A": [[25, 28, 30, 27, 26, 24, 25], [23, 26, 29, 28, 27, 25, 24]],
        "Ciudad B": [[20, 22, 24, 23, 21, 20, 19], [18, 21, 23, 22, 20, 19, 18]]
                                    }

    returns:
        dict: # Un diccionario donde las claves son nombres de ciudades y los valores son las temperaturas promedio calculadas.
    

    promedios_ciudades = {}
    for ciudad, temperaturas_semanales in datos_temperaturas.items():
        temperaturas_totales = []
        for temperaturas_semana in temperaturas_semanales:
            temperaturas_totales.extend(temperaturas_semana)
        promedio = sum(temperaturas_totales) / len(temperaturas_totales)
        promedios_ciudades[ciudad] = promedio 

     return promedios_ciudades

# Ejemplo de uso
datos_temperaturas = {
    "Quevedo": [[28, 30, 32, 31, 29, 28, 29], [27, 29, 31, 30, 28, 27, 28]],
    "Guayaquil": [[30, 32, 34, 33, 31, 30, 31], [29, 31, 33, 32, 30, 29, 30]],
    "Quito": [[18, 20, 22, 21, 19, 18, 19], [17, 19, 21, 20, 18, 17, 18]]
}

    
promedios = calcular_temperatura_promedio(datos_temperaturas)
print(promedios)
