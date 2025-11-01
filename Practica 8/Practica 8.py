#1

with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt","w") as archivo:
    archivo.write("Nombre,Precio,Cantidad\n")
    archivo.write("Manzana,1500,100\n")
    archivo.write("Naranja,6000,80\n")
    archivo.write("Plátano,1500,150\n")
    archivo.write("Uva,3000,60\n")
    archivo.write("Fresa,2000,40\n")





#2


with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt","r") as archivo:



    for linea in archivo:

        contenido = linea.strip()
        partes = contenido.split(",")
        print(f"Producto: {partes[0]} | Precio: {partes[1]} | Cantidad: {partes[2]}")




#3


with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt","a") as archivo:

    print(archivo)
    producto_agregar = input("Ingrese el nombre del producto a agregar: ")
    precio_agregar = input("Ingrese el precio del producto a agregar: ")
    cantidad_agregar = input("Ingrese la cantidad del producto a agregar: ")
    archivo.write(f"{producto_agregar},{precio_agregar},{cantidad_agregar}\n")




#4

with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt","r") as archivo:



    contenido = archivo.readlines()
    productos = []
    for linea in contenido:
        linea = linea.strip()
        parte = linea.split(",")
        producto = {"nombre": parte[0], "precio": parte[1], "cantidad": parte[2]}

        productos.append(producto)

print(productos)   



#5

with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt","r") as archivo:

    contenido = archivo.readlines()
    producto = input("Ingrese el nombre del producto a buscar: ")


    for linea in contenido:

        if producto in linea:
            producto_encontrado = linea.strip().split(",")
            print(f"Producto encontrado: {producto_encontrado[0]} | Precio: {producto_encontrado[1]} | Cantidad: {producto_encontrado[2]}")
            break
        else:
            producto_encontrado = None

    if producto_encontrado is None:
        print("Producto no encontrado.")








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




        
  


