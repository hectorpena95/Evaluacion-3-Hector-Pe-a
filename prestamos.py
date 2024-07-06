# Lista para almacenar los préstamos
prestamos = []

def registrar_prestamo():
    #Función para registrar un préstamo.
    print("== Registrar préstamo ==")
    nombre = input("Nombre del usuario: ")
    apellido = input("Apellido del usuario: ")
    id_libro = input("Identificación del libro (ID): ")
    fecha_prestamo = input("Fecha de préstamo (dia-mes-año): ")
    fecha_devolucion = input("Fecha de devolución (dia-mes-año): ")

    # Validación de entrada
    if nombre.strip() == '' or apellido.strip() == '' or id_libro.strip() == '' or fecha_prestamo.strip() == '' or fecha_devolucion.strip() == '':
        print("Todos los campos son obligatorios.")
        return

    # Registro del préstamo en diccionario
    prestamo = {
        'nombre': nombre,
        'apellido': apellido,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'fecha_devolucion': fecha_devolucion
    }
    prestamos.append(prestamo)
    print("Préstamo registrado correctamente.")
    print("")

def listar_prestamos():
    #Función para listar todos los préstamos
    print("== Listado de préstamos ==")
    if not prestamos:
        print("No hay registro de prestamos.") 
    else:
        for index, prestamo in enumerate(prestamos, start=1):
            print(f"Préstamo {index}:", {prestamo['nombre']}, {prestamo['apellido']}, "ID del libro:", {prestamo['id_libro']}, "Fecha de préstamo:", {prestamo['fecha_prestamo']}, "Fecha de devolución:", {prestamo['fecha_devolucion']})
            print("")

def imprimir_recibo_prestamo():
    #Función para imprimir el recibo de un préstamo.
    print("== Imprimir recibo de préstamo ==")
    if not prestamos:
        print("No hay préstamos registrados.")
        return
    
    listar_prestamos()
    try:
        seleccion = int(input("Seleccione el número de préstamo para imprimir el recibo: "))
        if seleccion < 1 or seleccion > len(prestamos):
            print("Selección inválida.")
            return
        
        # Generar archivo de recibo
        prestamo_seleccionado = prestamos[seleccion - 1]
        nombre_archivo = f"recibo_prestamo_{seleccion}.txt"
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Recibo de préstamo\n")
            archivo.write(f"Nombre: {prestamo_seleccionado['nombre']} {prestamo_seleccionado['apellido']}\n")
            archivo.write(f"ID del libro: {prestamo_seleccionado['id_libro']}\n")
            archivo.write(f"Fecha de préstamo: {prestamo_seleccionado['fecha_prestamo']}\n")
            archivo.write(f"Fecha de devolución: {prestamo_seleccionado['fecha_devolucion']}\n")
        
        print(f"Recibo generado correctamente: {nombre_archivo}")
    
    except:
        print("Debes ingresar un número válido.")

