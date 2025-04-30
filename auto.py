# PARTE 1: BÁSICO

# Crear un diccionario llamado auto
auto = {"Marca":"Toyota", 
        "Referencia": "Corolla", 
        "Año": 2022}
# Cambiar el modelo del auto a otro diferente
auto["Marca"] = "Audi"
print(auto)

# Agregar una nueva clave color al diccionario

auto["color"] = "Rojo"
print(auto)

# Eliminar la clave año
del auto["Año"]
print(auto)
# Imprimir todas las claves del diccionario usando un bucle for
for claves in auto:
  print(claves)

# Imprimir todos los valores del diccionario usando un bucle for
for valor in auto.values():
 print(valor)