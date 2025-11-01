
#6







with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt","r") as archivo:

    contenido = archivo.readlines()

 

    
    for linea in contenido:
        linea = linea.strip()
        parte = linea.split(",")
    

        print(parte)


opcion = input("Desea agregar un nuevo producto? (s/n): ").lower()
lista_productos = []

while opcion != 'n':
    nombre_nuevo = input("Ingrese el nombre del producto: ")
    precio_nuevo = float(input("Ingrese el precio del producto: "))
    cantidad_nueva = int(input("Ingrese la cantidad del producto: "))
    lista_productos.append(f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n")

    
    

    opcion = input("Desea agregar otro producto? (s/n): ").lower()

    

with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt", "w") as archivo:

    for producto in lista_productos:
        archivo.write(producto)

print("Productos agregados correctamente.")

for producto in lista_productos:
    print(f"Producto agregado: {producto.strip()}")




        
  