def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        if matriz[i][j]== valor:
            return(i,j) # retorna la posicion (fila,columna)
        return None # retorna none si el valor no se encuentra
    
    # Definir la matriz 3x3
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    # Valor a buscar
    valor_a_buscar = int(input("Ingrese el valor a buscar en la matriz:"))

    # Lamar a la funcion de busqueda
    resultado = buscar_valor(matriz, valor_a_buscar)

    # Mostrar el resultado
    if resultado:
        print(f"El valor {valor_a_buscar} se encuentra en la posicion {resultado}(fila, columna)")
    else:
        print(f"El valor{valor_a_buscar} no se encuentra en la matriz.")
        
       
    