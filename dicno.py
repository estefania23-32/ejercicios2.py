# Crear un diccionario de estudiantes con sus notas
estudiantes = {
    "Juan": 8,
    "María": 9,
    "Pedro": 5,
    "Ana": 7,
    "Luis": 4
}

# Imprimir los nombres de los estudiantes que aprobaron (nota >= 6)
print("Estudiantes que aprobaron:")
for nombre, nota in estudiantes.items():
    if nota >= 6:
        print(f"{nombre} - Nota: {nota}")