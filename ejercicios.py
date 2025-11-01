
#4

with open("C:\\Users\\ks249\\OneDrive\\Desktop\\facultad\\CLASES\\PROGRAMACION\\archivos\\productos.txt","r") as archivo:



    for producto in archivo:
        
        parte = producto.strip().split(",")
        productos_lista = {}

        
        productos_lista["nombre"] = parte[0]
        productos_lista["precio"] = float(parte[1])
        productos_lista["cantidad"] = int(parte[2])
        print(productos_lista)        