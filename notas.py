try:
    nota = int(input("Introduce una nota (del 1 al 5): "))
    
    match nota:
        case 1:
            print("Muy deficiente")
        case 2:
            print("Deficiente")
        case 3:
            print("Suficiente")
        case 4:
            print("Notable")
        case 5:
            print("Excelente")
        case _:
            print("Nota no válida. Debes introducir un número del 1 al 5.")
            
except ValueError:
    print("Error: Debes introducir un número entero.")