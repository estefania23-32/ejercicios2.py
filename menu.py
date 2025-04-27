print("---- MENÚ DE OPCIONES ----")
print("1. Saludar")
print("2. Mostrar fecha actual")
print("3. mostrar en que mes estas")

opcion = int(input("Elige una opción (1-3): "))

match opcion:
    case 1:
        print("¡Hola! Bienvenido al programa.")
    case 2:
        print("Hoy es 26 de abril de 2025.")
    case 3:
        print("Abril")
    case _:
        print("Opción no válida.")