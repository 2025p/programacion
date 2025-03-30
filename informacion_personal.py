# crear un diccionario con informacion ficticio
Informacion_personal = {
    "nombre": "Roberto Cerna",
    "edad": 35,
    "ciudad": "Quevedo",
    "profesion": "Ingeniero"

}

# Acceder y modificar el valor de "ciudad"
Informacion_personal["ciudad"] = "Guayaquil"

#Agregar una nueva clave-valor para "profesion"
Informacion_personal["profesion"] = "Desarrollador de software"

# verificar si la clave "telefono " existe y agregarla si no esta
if "telefono" not in Informacion_personal:
    Informacion_personal["telefono"] = "0980300103"

    # Elimina la clave "edad
    del Informacion_personal["edad"]
    # Imprimir el dicionario final
    print(Informacion_personal)
    print("-" * 30) # Imprime la lista separadora

    for clave, valor in Informacion_personal . items():
        print(f"{clave:<15}: {valor}") # Formatea la salida en columnas

       


