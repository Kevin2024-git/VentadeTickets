# Variables globales
eventos = {}  # Diccionario para almacenar eventos con sus detalles

def menu_principal():
    """
    Función que muestra el menú principal y gestiona la navegación del usuario.
    """
    while True:
        print("\n--- Sistema de Venta de Tickets ---")
        print("1. Registrar Evento")
        print("2. Vender Tickets")
        print("3. Mostrar Eventos")
        print("4. Actualizar Evento")  # Nueva opción para actualizar eventos
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            nombre, fecha, hora = obtener_datos_evento()
            if validar_datos_evento(nombre, fecha, hora):
                registrar_evento(nombre, fecha, hora)
            else:
                print("Datos incompletos o incorrectos, por favor intente nuevamente.")
        elif opcion == '2':
            nombre_evento = input("Ingrese el nombre del evento para el que desea comprar tickets: ")
            if evento_existe(nombre_evento):
                cantidad = int(input("¿Cuántos tickets desea comprar?: "))
                print(vender_tickets(nombre_evento, cantidad))
            else:
                print(f"El evento '{nombre_evento}' no está registrado. Regístrelo primero.")
        elif opcion == '3':
            mostrar_eventos()
        elif opcion == '4':  # Llamar a la nueva función de actualización
            nombre_evento = input("Ingrese el nombre del evento que desea actualizar: ")
            if evento_existe(nombre_evento):
                nueva_fecha = input("Ingrese la nueva fecha (DD/MM/AAAA): ")
                nueva_hora = input("Ingrese la nueva hora (HH:MM): ")
                if validar_datos_evento(nombre_evento, nueva_fecha, nueva_hora):
                    actualizar_evento(nombre_evento, nueva_fecha, nueva_hora)
                else:
                    print("Datos inválidos. Inténtelo nuevamente.")
            else:
                print(f"El evento '{nombre_evento}' no está registrado.")
        elif opcion == '5':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def obtener_datos_evento():
    """
    Función que solicita al usuario ingresar los datos del evento.
    Retorna los datos ingresados: nombre, fecha y hora.
    """
    nombre = input("Ingrese el nombre del evento: ")
    fecha = input("Ingrese la fecha del evento (DD/MM/AAAA): ")
    hora = input("Ingrese la hora del evento (HH:MM): ")
    return nombre, fecha, hora

def validar_datos_evento(nombre, fecha, hora):
    """
    Función que valida los datos del evento.
    Retorna True si los datos son válidos, de lo contrario retorna False.
    """
    if nombre and fecha and hora:
        return True
    return False

def registrar_evento(nombre, fecha, hora):
    """
    Función que registra un evento en el diccionario 'eventos'.
    """
    eventos[nombre] = {"fecha": fecha, "hora": hora}
    print(f"Evento '{nombre}' registrado exitosamente.")

def evento_existe(nombre_evento):
    """
    Función que verifica si un evento está registrado.
    """
    return nombre_evento in eventos

def vender_tickets(nombre_evento, cantidad):
    """
    Función que procesa la venta de tickets para un evento registrado.
    """
    return f"{cantidad} tickets vendidos para el evento '{nombre_evento}'."

def mostrar_eventos():
    """
    Función que muestra todos los eventos registrados.
    """
    if eventos:
        print("\n--- Eventos Registrados ---")
        for nombre, detalles in eventos.items():
            print(f"Evento: {nombre} - Fecha: {detalles['fecha']} - Hora: {detalles['hora']}")
    else:
        print("No hay eventos registrados.")

def actualizar_evento(nombre, nueva_fecha, nueva_hora):
    """
    Función que actualiza la fecha y hora de un evento registrado.
    """
    eventos[nombre]["fecha"] = nueva_fecha
    eventos[nombre]["hora"] = nueva_hora
    print(f"Evento '{nombre}' actualizado exitosamente a la nueva fecha {nueva_fecha} y hora {nueva_hora}.")

# Ejecutar el menú principal
menu_principal()
