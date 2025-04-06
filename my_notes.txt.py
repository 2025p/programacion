# escribimos las notas de texto
# Abrimos (o creemos si no existe) las notas "my_notes.txt" en modo escritura
leer_notas = open("my_note.txt", "w")

# Escribimos cinco lineas personales de notas 
leer_notas.write("1. Este proyecto de Python lo tengo que terminar antes del domingo.\n")
leer_notas.write("2. Esta semana se termina las clases del primer nivel.\n")
leer_notas.write("3. La proxima semana empezaran las evaluaciones finales.\n")
leer_notas.write("4. Desde el lunes tengo que repasar antes de realizar cada evaluacion.\n")
leer_notas.write("5. Mi objetivo esta en seguir avanzando de niveles.\n")

leer_notas.close()
print(" Se ha escrito un archivo my_notes.txt'")

# Lectura del archivo de texto
# Abrimos el archivo en forma de lectura ("r")
leer_notas_lectura = open("my_notes.txt","r")

# Leemos el contenido linea por linea usando readline()
Linea = leer_notas_lectura.readline()
print("linea.rstrip('/n'") 
while Linea: # Mientras haya lineas por leer
     Linea = leer_notas_lectura.readline() # mostramos la linea sin el salto final
     if Linea: # No imprimir lineas vacias al final del archivo
        print (Linea.rstrip('\n'))

leer_notas_lectura.close() # Cerramos las notas despues de leer
print("fin de la lectura")


