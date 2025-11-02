


import os
RUTA = r"C:\Users\ks249\OneDrive\Desktop\facultad\CLASES\PROGRAMACION\archivos\catalogo.csv"

if not os.path.exists(RUTA):
    with open(RUTA, "w") as archivo:
        archivo.write("TITULO,CANTIDAD\n")



catalogo = []
with open(RUTA,"r") as archivo: 

        
    contenido = archivo.readlines()
    for linea in contenido:
        linea = linea.strip()
        partes = linea.split(",")


        catalogo = [{"TITULO: ": partes[0], "CANTIDAD: ": partes[1]}]

        

with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\catalogo.csv","a") as archivo:     
    while True:
        opcion = int(input("Ingrese un numero segun la opcion elegida: 1. Ingresar titulos, 2.Ingresar ejemplares, 3.Mostrar catalogo, 4.Consultar disponibilidad, 5.Listar agotados, 6.Agregar titulo, 7.Actualizar ejemplares, 8.Salir   "  ))


        match opcion:
            case 1:
                cantidad_elegida= int(input("Ingrese la cantidad de libros que desea ingresar: "))
                for i in range (cantidad_elegida):
                    titulo_ingresado = input("Ingrese el titulo que desea ingresar: ").lower().strip()
                    while True:
                        cantidad_ingresada = int(input("Ingrese la cantidad que desea ingresar: "))
                        if titulo_ingresado not in catalogo and titulo_ingresado != "":
                            if cantidad_ingresada >= 0:
                                archivo.write(f"{titulo_ingresado},{cantidad_ingresada}\n")
                                print("Datos ingresados correctamente")
                                print(f"Se ha ingresado : Titulo: {titulo_ingresado}, Cantidad: {cantidad_ingresada}")
                                break

                    
            case 2:
                titulo_elegido = input("Ingrese el titulo que desea agregar ejemplares: ").lower().strip()
                
                cantidad_a_ingresar = int(input("Ingrese la cantidad que desea ingresar"))
                for fila in catalogo:
                    t = titulo_elegido.strip().lower()
                    if fila["TITULO"] == t:
                        
                        if cantidad_a_ingresar >= 0:

                            suma = catalogo[titulo_elegido] + cantidad_a_ingresar
                            catalogo[titulo_elegido] = suma
                            print("La operacion fue exitosa")
                            with open(RUTA,"a") as archivo:
                                archivo.write(f"TITULO,CANTIDAD\n")
                                for fila in catalogo:
                                    archivo.write(f"{fila['TITULO']}, {fila['CANTIDAD']}\n")
                        
                    else: 
                        print("La cantidad debe ser positiva")
                else:
                    print("Ese titulo no existeen el catologo")                






                        

            case 8:
                print("Usted ha salido del programa")
                break
            case _:
                print("Opcion no valida")