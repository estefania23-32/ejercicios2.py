for tabla in range(1, 6):
    print(f"\nTabla del {tabla}:")
    print("-" * 15)
    
    for multiplicador in range(1, 11):
        resultado = tabla * multiplicador
        print(f"{tabla} x {multiplicador} = {resultado}")