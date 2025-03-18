contador = 1 # Inicializacion el contador
while contador <= 5: # Mientras el contador sea menor o igual a 5
    print(contador) #Imprime el numero natural
    contador += 1 # Incrementa el contador a 2

    #Juego de adivinanzas
import random

secret_number = random.randint(1,100)
guess = 0
attempts = 0
print("¡Bienvenido al juego Adivina el Numero!")
while guess!= secret_number:
    guess =int(input("Adivina el numero entre 1 y 100:"))
    attempts += 1
        
    if guess < secret_number:
    elif guess > secret_number:
     print("¡Demasiado alto!")

     print(f"¡Felicidades! Adivinaste el numero en {attempts}intentos.")

     
# Inicializa la variable suma
suma = 0
# Itera sobre los numeros del 1 al 10
for i in range(1, 11):
   # Sums el numero actual a la variable suma
   suma += i
   # Imprime el resultado de la suma 
print("La suma de los primeros 10 numeros enteros positivos es:",suma)







