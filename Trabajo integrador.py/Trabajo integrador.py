from operaciones import agregar_pais, actualizar_datos, buscar_pais, min_p, max_p, promedio_p, promedio_s,contar_paises_por_continente,filtrar_paises_por_continente,filtrar_paises_por_rango_poblacion,filtrar_paises_por_rango_superficie,ordenar_paises_por_nombre,ordenar_paises_por_poblacion,ordenar_paises_por_superficie
import os

RUTA = r"C:\Users\ks249\OneDrive\Desktop\facultad\CLASES\PROGRAMACION\archivos\paises.csv"

if not os.path.exists(RUTA):
    with open(RUTA, "w", encoding="utf-8") as archivo:
        archivo.write("NOMBRE,POBLACION,SUPERFICIE,CONTINENTE\n")

paises = []

with open(RUTA, "r", encoding="utf-8") as archivo:
    contenido = archivo.readlines()

for i, linea in enumerate(contenido):
    linea = linea.strip()
    if not linea:
        continue  # salta líneas vacías

    partes = [p.strip() for p in linea.split(",")]

    # Saltar encabezado
    if i == 0 and partes[1].upper() == "POBLACION":
        continue

    if len(partes) < 4:
        print("Línea inválida en el CSV:", linea)
        continue

    paises.append({
        "nombre": partes[0].lower(),
        "poblacion": int(partes[1]),
        "superficie": int(partes[2]),
        "continente": partes[3]
    })


with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\paises.csv","a") as archivo:   
       while True:
        print(" 1. Agregar un pais" )
        print(" 2. Actualizar los datos de Población y Superfice de un Pais" )
        print(" 3. Buscar un país" )
        print(" 4. Filtrar paises" )
        print(" 5. Ordenar paises" )
        print(" 6. Mostrar estdisticas" )
        print(" 7- Salir" )
        
        opcion = int(input("Ingrese un numero segun la opcion elegida: "))
    


        match opcion:
            case 1:


                cantidad_elegida= int(input("Ingrese la cantidad de paises que desea ingresar: "))
                if cantidad_elegida != 0:
                    
                    for i in range (cantidad_elegida):
                            nombre_ingresado = input("Ingrese el pais que desea ingresar: ").lower().strip()
                            while True:
                                if nombre_ingresado in paises or nombre_ingresado!= "":
                                     print("Error el pais ya existe o esta vacio")
                                break
                            poblacion = int(input("Ingrese la poblacion: "))
                            superficie = int(input("Ingrese la superficie en km2: "))
                            continente = input("Ingrese el continente del pais ingresado: ")
                                        
                            if poblacion == 0 or superficie == 0 or continente == "":
                                        
                                        print("Error numero  invalido")
                                        break
                       
                                            
                                

                                
                                    
                                    

                            else:

                                nuevo_pais = agregar_pais(nombre_ingresado, poblacion, superficie, continente)

                                paises.append(nuevo_pais)

                                            


                                archivo.write(f"{nombre_ingresado}, {poblacion}, {superficie}, {continente}\n")
                                print(f"Se ha ingresado : {nuevo_pais} \n")
                                            
                                        

                 
            case 2:
                    
                    pais_elegido = input("Ingrese el pais que desea actualizar poblacion y superficie: ").lower()
                    pais_actualizado = False
                    pais_encontrado = False
                    for i, fila in enumerate(paises):
                        if fila["nombre"].lower() == pais_elegido:
                            pais_encontrado = True
                        
                            
                        
                            
                            actualizar_poblacion = int(input("Ingrese la poblacion que desea actualizar: "))
                    
                            actualizar_superficie = int(input("Ingrese la superficie que desea actulizar"))
                            continente_act =  input("Ingrese el continente que se va a mantener")
                            
                            if actualizar_poblacion > 0 and actualizar_poblacion > 0 :

                                actualizado = actualizar_datos(pais_elegido,actualizar_poblacion,actualizar_superficie,continente_act)
                                

                                            

                               
                                paises[i] = actualizado

                                

                                with open(RUTA,"w") as archivo:
                                    archivo.write("NOMBRE,POBLACION,SUPERFICIE,CONTINENTE\n")  
                                    
                                    archivo.write(f"{pais_elegido},{actualizar_poblacion},{actualizar_superficie},{continente_act}\n")
                            
                                

                                print(f"Datos actualizados para {pais_elegido}.")
                                pais_actualizado = True
                                break

                            break               
                             
                                
                                
                                
                               
                            
                         
                        if not pais_encontrado:

                            print("Ese titulo no existeen el catologo")                




            case 3:
                  
                  pais_buscado = input("Ingrese el pais que desea buscar")
                  
                  
                  
                  pais_encontrado =  buscar_pais(paises,pais_buscado)  




                  print(pais_encontrado)

                
            case 4:
                  print("1. Filtrar por continente")
                  print("2. Filtrar por rango de poblacion")
                  print("3. Filtrar por rango de superficie")
                  opcion_filtro = int(input("Ingrese el numero segun el filtro que desea aplicar: "))
                  match opcion_filtro:
                            case 1:
                                continente_filtro = input("Ingrese el continente por el que desea filtrar: ")
                                paises_filtrados = filtrar_paises_por_continente(paises, continente_filtro)
                                print(f"Paises en el continente {continente_filtro}:")
                                for pais in paises_filtrados:
                                    print(pais)

                            case 2:
                                poblacion_min = int(input("Ingrese la poblacion minima: "))
                                poblacion_max = int(input("Ingrese la poblacion maxima: "))
                                paises_filtrados = filtrar_paises_por_rango_poblacion(paises, poblacion_min, poblacion_max)
                                print(f"Paises con poblacion entre {poblacion_min} y {poblacion_max}:")
                                for pais in paises_filtrados:
                                    print(pais)
                            case 3:
                                superficie_min = int(input("Ingrese la superficie minima: "))
                                superficie_max = int(input("Ingrese la superficie maxima: "))
                                paises_filtrados = filtrar_paises_por_rango_superficie(paises, superficie_min, superficie_max)
                                print(f"Paises con superficie entre {superficie_min} y {superficie_max}:")
                                for pais in paises_filtrados:
                                    print(pais)

            case 5:
                  print("1. Ordenar por nombre")    
                  print("2. Ordenar por poblacion")
                  print("3. Ordenar por superficie") 

                  opcion_orden = int(input("Ingrese el numero segun el orden que desea aplicar: "))
                  match opcion_orden:
                                case 1:
                                    paises_ordenados = ordenar_paises_por_nombre(paises)
                                    print("Paises ordenados por nombre:")
                                    for pais in paises_ordenados:
                                        print(pais)
                                case 2:
                                    paises_ordenados = ordenar_paises_por_poblacion(paises)
                                    print("Paises ordenados por poblacion:")
                                    for pais in paises_ordenados:
                                        print(pais)
                                case 3:
                                    paises_ordenados = ordenar_paises_por_superficie(paises)
                                    print("Paises ordenados por superficie:")
                                    for pais in paises_ordenados:
                                        print(pais)
                  

            case 6:
                  
                  
                  
                  opcion_estadisticas = int(input("Ingrese el numero segun la estadistica que desea ver: 1. Pais con mayor poblacion, 2. Promedio de poblacion, 3. Promedio superficie, 4.Cantidad de paises por continente "))

                  match opcion_estadisticas:
                            case 1:

                                # lista de solo las poblaciones
                                poblaciones = [pais["poblacion"] for pais in paises]

                                # usamos tus funciones
                                maxima_poblacion = max_p(poblaciones)
                                menor_poblacion = min_p(poblaciones)

                                # buscamos los países que tienen esas poblaciones
                                pais_max = None
                                pais_min = None

                                for pais in paises:
                                    if pais["poblacion"] == maxima_poblacion:
                                        pais_max = pais
                                    if pais["poblacion"] == menor_poblacion:
                                        pais_min = pais

                                print(f"El país con MAYOR población es: {pais_max['nombre']} ({pais_max['poblacion']})")
                                print(f"El país con MENOR población es: {pais_min['nombre']} ({pais_min['poblacion']})")

                            case 2:
                                promedio = promedio_p(paises)
                                print(f"El promedio de población es: {promedio}")
      
                          
                                    
                                    
                            case 3:
                                promedio_superficie = promedio_s(paises)
                                print(f"El promedio de superficie es: {promedio_superficie}")
                               
                     
                            case 4:
                                conteo = contar_paises_por_continente(paises)
                                for continente, cantidad in conteo.items():
                                    print(f"{continente}: {cantidad} países")

            case 7:
                    print("Usted ha salido del programa")
                    break
            case _:
                    print("Opcion no valida")