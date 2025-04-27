print("Identificación de números pares e impares del 1 al 10:")

# Recorrer los números del 1 al 10
for numero in range(1, 11):
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")