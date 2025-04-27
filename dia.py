dia = input("Introduce un día de la semana: ").lower()

match dia:
    case "lunes" | "martes" | "miércoles" | "miercoles" | "jueves":
        print(f"{dia.capitalize()} es un día laboral.")
    case "viernes":
        print("¡Viernes! Último día laboral de la semana.")
    case "sábado" | "sabado" | "domingo":
        print(f"{dia.capitalize()} es fin de semana.")
    case _:
        print(f"'{dia}' no es un día de la semana válido.")
