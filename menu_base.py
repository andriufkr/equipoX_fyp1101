def datos_messi():
    print("Mi nombre es Lionel Messi y tengo 38 años.")

# Menú base del programa 
while True: 
    print("\n--- MENÚ PRINCIPAL ---") 
    print("1. Función de integrante 1") 
    print("2. Función de integrante 2")  
    print("0. Salir") 

    op = input("Seleccione opción: ") 
    
    if op == "0": 
        print("Programa finalizado.") 
        break 
    elif op == "1": 
        pass  # Aquí se llamará a la función del integrante 1 
    elif op == "2": 
        datos_messi()  # Aquí se llamará a la función del integrante 2 
    else: 
        print("⚠️ Opción inválida.")
