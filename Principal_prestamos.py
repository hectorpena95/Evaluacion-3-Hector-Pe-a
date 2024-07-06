from prestamos import registrar_prestamo, listar_prestamos, imprimir_recibo_prestamo

while True:
    print("=== Sistema de Gestión de Préstamos de Libros ===")
    print("1. Registrar préstamo")
    print("2. Listar todos los préstamos")
    print("3. Imprimir recibo de préstamo")
    print("4. Salir del programa")
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        registrar_prestamo()
    elif opcion == '2':
        listar_prestamos()
    elif opcion == '3':
        imprimir_recibo_prestamo()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-4).")

 