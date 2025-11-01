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
    contenido = archivo.readline()
    linea1 = contenido.strip()
    partes = linea1.split(",")
    linea2 = archivo.readline()
    linea2 = linea2.strip()
    partes2 = linea2.split(",")
    linea3 = archivo.readline()
    linea3 = linea3.strip()
    partes3 = linea3.split(",")
    linea4 = archivo.readline()
    linea4 = linea4.strip()
    partes4 = linea4.split(",")
    linea5 = archivo.readline()
    linea5 = linea5.strip()
    partes5 = linea5.split(",")
    linea6 = archivo.readline()
    linea6 = linea6.strip()
    partes6 = linea6.split(",")




    print(f"Producto: {partes2[0]} | Precio: {partes2[1]} | Cantidad: {partes2[2]}")
    print(f"Producto: {partes3[0]} | Precio: {partes3[1]} | Cantidad: {partes3[2]}")
    print(f"Producto: {partes4[0]} | Precio: {partes4[1]} | Cantidad: {partes4[2]}")
    print(f"Producto: {partes5[0]} | Precio: {partes5[1]} | Cantidad: {partes5[2]}")
    print(f"Producto: {partes6[0]} | Precio: {partes6[1]} | Cantidad: {partes6[2]}")
