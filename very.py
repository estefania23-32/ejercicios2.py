contraseña_correcta = "python123"

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    
    contraseña_ingresada = input("Ingrese la contraseña: ")
    
    if contraseña_ingresada == contraseña_correcta:
        print("¡Acceso concedido!")
        break
    else:
        intentos += 1
        intentos_restantes = max_intentos - intentos
        
        if intentos_restantes > 0:
            print(f"Contraseña incorrecta. Le quedan {intentos_restantes} intentos.")
        else:
            print("Contraseña incorrecta. No quedan más intentos.")

if intentos == max_intentos:
    print("ACCESO BLOQUEADO: Ha excedido el número máximo de intentos.")