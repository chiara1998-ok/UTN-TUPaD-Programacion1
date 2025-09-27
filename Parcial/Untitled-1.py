# Biblioteca
# Autor: Chiara Silvana Diaz






titulos = []
ejemplares = []


while True:
    menu = int(input("Ingrese una opcion (1-8): \n1. Opcion 1) Ingresar Titulos\n2. Opcion 2) Ingresar Ejemplares\n3. Opcion 3) Mostrar catalogo\n4. Opcion 4) Consultar disponibilidad\n5. Opcion 5) Listar agotados\n6. Opcion 6) Agregar titulo\n7. Opcion 7) Actualizar ejemplares(prestamo/devolucion)\n8. Opcion 8) Salir\n"))

 

    match menu:
            case 1:

                nuevo_titulo = input("Ingrese el nuevo titulo: ")
                cantidad_inicial = int(input("Ingrese la cantidad inicial: "))
                if nuevo_titulo == " ":
                    print(f"Error, el titulo no puede estar vacio")
                elif cantidad_inicial <= 0:
                    print(f"Error, la cantidad inicial no puede ser negativa ni cero")
                else:
                    titulos.append(nuevo_titulo)
                    ejemplares.append(cantidad_inicial)
                    print(f"Usted ha ingresado un nuevo titulo, es el siguiente: {nuevo_titulo} con {cantidad_inicial} ejemplares")
                
            case 2:

                titulo_actualizar = input("Ingrese el titulo que desea actualizar: ")
                if titulo_actualizar in titulos:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad de ejemplares: "))
                    for i in range(len(titulos)):
                        if titulos[i] == titulo_actualizar:
                            ejemplares[i] += nueva_cantidad
                    if nueva_cantidad < 0:
                        print(f"Error, la cantidad de ejemplares no puede ser negativa")
                        continue
                    
                    print(f"Usted ha actualizado la cantidad de ejemplares del titulo {titulo_actualizar} a {nueva_cantidad}")
                else:
                    print(f"El titulo {titulo_actualizar} no se encuentra en el catalogo.")
                
            case 3:
                print("Catalogo de la biblioteca:")
                for i in range(len(titulos)):
                    print(f"{titulos[i]}: {ejemplares[i]} ejemplares")
            
            case 4:
                titulo_buscar = input("Ingrese el titulo que desea consultar: ")
                if titulo_buscar in titulos:
                    for i in range(len(titulos)):
                        if titulos[i] == titulo_buscar:
                            print(f"El titulo {titulo_buscar} tiene {ejemplares[i]} ejemplares disponibles")
                            break
                else:
                    print(f"El titulo {titulo_buscar} no se encuentra en el catalogo.")            
            case 5:
                    print("Titulos agotados:")
                    for i in range(len(titulos)):
                        if ejemplares[i] == 0:
                            print(f"{titulos[i]}")
            case 6:
                if len(titulos) <= 0:
                    
                        print("Debe ingresar al menos un titulo inicial antes de agregar otro. Vuelva al menu principal e ingrese la opcion 1")
                        
                else:
                    nuevo_libro = input("Ingrese un nuevo libro: ")

                    nuevo_ejemplar = int(input("Ingrese la cantidad de ejemplares: "))
                    if nuevo_libro == "":
                         print(f"Error, el titulo no puede estar vacio")
                    elif nuevo_ejemplar < 0:
                         print(f"Error, la cantidad inicial no puede ser negativa")

                    titulos.append(nuevo_libro)
                    ejemplares.append(nuevo_ejemplar)
                    

            case 7:
                opcionActualizar = int(input("Ingrese 1 para prestamo o 2 para devolucion: "))
                if opcionActualizar == 1:
                    titulo_prestamo = input("Ingrese el titulo que desea tomar en prestamo: ")
                    cant_prestamo = int(input("Ingrese la cantidad de ejemplares que desea tomar en prestamo: "))
                    if cant_prestamo <= 0 and cant_prestamo > 100:
                        print(f"Error, la cantidad de ejemplares a prestar debe ser mayor a 0 y menor que 100")
                    if titulo_prestamo in titulos:
                        for i in range(len(titulos)):
                            if titulos[i] == titulo_prestamo:
                                if ejemplares[i] >= cant_prestamo:
                                    ejemplares[i] -= cant_prestamo
                                    print(f"Usted ha prestado el titulo {titulo_prestamo}. Quedan {ejemplares[i]} ejemplares disponibles.")
                                else:
                                    print(f"No hay ejemplares disponibles para el titulo {titulo_prestamo}.")
                                break
                    else:
                        print(f"El titulo {titulo_prestamo} no se encuentra en el catalogo.")
                elif opcionActualizar == 2:
                    titulo_devolucion = input("Ingrese el titulo que desea devolver: ")
                    cant_devolucion = int(input("Ingrese la cantidad de ejemplares que desea devolver: "))
                    if cant_devolucion <= 0:
                        print(f"Error, la cantidad de ejemplares a devolver debe ser mayor a 0")
                    if titulo_devolucion in titulos:
                        for i in range(len(titulos)):
                            if titulos[i] == titulo_devolucion:
                                ejemplares[i] += cant_devolucion
                                print(f"Usted ha devuelto el titulo {titulo_devolucion}. Ahora hay {ejemplares[i]} ejemplares disponibles.")
                                break
                    else:
                        print(f"El titulo {titulo_devolucion} no se encuentra en el catalogo.")
                else:
                    print("Opcion no valida. Debe ingresar 1 para prestamo o 2 para devolucion.")
            case 8:
                print("Usted ha salido del programa")
                break
            case _:
                print("Opcion no valida")