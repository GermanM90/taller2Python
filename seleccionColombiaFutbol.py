# Apellidos y Nombres:
# Monroy Rumay German Fernando
# Toro Garzón Yesid

delanterosSeleccionColombiaFutbol = [{
    'nombres': 'Duvan Zapata',
    'salario': 500000,
    'partidos_Jugados': 7,
    'partidos_Ganados': 4,
    'partidos_Perdidos': 2,
    'goles': 3,
},
    {
    'nombres': 'Rafael Borre',
    'salario': 700000,
    'partidos_Jugados': 10,
    'partidos_Ganados': 6,
    'partidos_Perdidos': 2,
    'goles': 5,
},
    {
    'nombres': 'Radamel Falcao',
    'salario': 1000000,
    'partidos_Jugados': 15,
    'partidos_Ganados': 10,
    'partidos_Perdidos': 3,
    'goles': '',
},
    {
    'nombres': 'Jeison Duran',
    'salario': 350000,
    'partidos_Jugados': 3,
    'partidos_Ganados': 1,
    'partidos_Perdidos': 1,
    'goles': 1,
}]

while True:
    print("Seleccione una operación:")
    print("1. Agregar")
    print("2. Actualizar")
    print("3. Buscar")
    print("4. Eliminar")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '1':
        # Agregar
        agregar_jugador = lambda jugador: delanterosSeleccionColombiaFutbol.append(jugador)
        nombres = input("Ingrese el nombre del jugador: ")
        salario = float(input("Ingrese el salario del jugador: "))
        partidos_jugados = int(input("Ingrese la cantidad de partidos jugados: "))
        partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
        partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))
        goles = int(input("Ingrese la cantidad de goles del jugador: "))
        nuevo_jugador = {
            'nombres': nombres,
            'salario': salario,
            'partidos_Jugados': partidos_jugados,
            'partidos_Ganados': partidos_ganados,
            'partidos_Perdidos': partidos_perdidos,
            'goles': goles
        }
        agregar_jugador(nuevo_jugador)
        print("Jugador agregado exitosamente.")
        print(delanterosSeleccionColombiaFutbol)
        pass
    elif opcion == '2':
        # Actualizar
        actualizar_goles = lambda jugador, nuevo_goles: {**jugador, 'goles': nuevo_goles}

        # Nombre del jugador que deseas actualizar
        nombre_jugador = 'Duvan Zapata'

        # Cantidad de goles actualizada
        nuevos_goles = 5

        # Buscar al jugador en la lista y actualizar la cantidad de goles
        delanterosSeleccionColombiaFutbol = list(map(lambda jugador: actualizar_goles(jugador, nuevos_goles) if jugador['nombres'] == nombre_jugador else jugador, delanterosSeleccionColombiaFutbol))
        
        pass
    elif opcion == '3':
        # Buscar
        jugadores_mas_de_3_goles = list(filter(lambda jugador: jugador['goles'] != '' and int(jugador['goles']) > 3, delanterosSeleccionColombiaFutbol))
        print(jugadores_mas_de_3_goles)
        
        pass
    elif opcion == '4':
        #Eliminar
        eliminar_diccionario = lambda dic: dic.clear()
        eliminar_diccionario(delanterosSeleccionColombiaFutbol)
        print(delanterosSeleccionColombiaFutbol)
        
        pass
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    nueva_operacion = input("¿Desea realizar una nueva operación? (S/N): ")
    if nueva_operacion.lower() != 's':
        print("¡Hasta luego!")
        break

