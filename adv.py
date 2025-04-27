import random

numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego Adivina el Número!")
print("Estoy pensando en un número entre 1 y 10.")

adivinado = False
intentos = 0

while not adivinado:
   
    try:
        intento = int(input("Adivina el número: "))
        intentos += 1
        

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            adivinado = True
        elif intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        else:
            print("Demasiado alto. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")