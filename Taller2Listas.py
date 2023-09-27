paises = ["colombia", "venezuela", "peru", "ecuador","chile","uruguay"]

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
        agregar_pais = lambda pais: paises.append(pais)
        pais = input("Que país deseas agregar a la lista? ")
        agregar_pais(pais)
        print(paises)
        pass
    elif opcion == '2':
        # Actualizar
        paises_mayusculas = list(map(lambda pais: pais.upper(), paises))
        print(paises_mayusculas)
        pass
    elif opcion == '3':
        buscar_pais = lambda lista, pais: f"{pais} encontrado en la lista." if pais in lista else f"{pais} no encontrado en la lista."
        pais_buscado = input("Ingresa el nombre de un país: ")
        resultado = buscar_pais(paises, pais_buscado)
        print(resultado)
        pass
    elif opcion == '4':
        # Eliminar
        eliminar_lista = lambda lista: lista.clear()
        eliminar_lista(paises)
        print(paises)
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
