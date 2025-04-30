# PARTE 2: INTERMEDIO

# Crear un diccionario paises
paises = { "España": "Madrid", "Francia": "París", "Italia": "Roma", "Alemania": "Berlín", "Portugal": "Lisboa"}

# Programa que pregunte al usuario un país y devuelva su capital
usuario = input("ingrese el pais para ver su capital:")
if usuario in paises:
    print(f"La capital de {usuario} es {paises[usuario]}")
else:
 print(f"No tengo informacion sobre la capital {usuario}")
 
# Invertir el diccionario paises
paises_invertido = {}
for pais, capital in paises.items():
    paises_invertido[capital] = pais
print(paises_invertido)


