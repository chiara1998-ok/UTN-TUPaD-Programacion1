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



   