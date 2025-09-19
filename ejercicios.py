#2



list = []

for i in range(5):
    producto = input("Ingrese un producto: ")

    list.append(producto)
    

list.sort()   
print(list[0:len(list)])     

eliminar = input("Ingrese un producto a eliminar: ")
if eliminar in list:
    list.remove(eliminar)
    print(f"Producto {eliminar} eliminado.")
    print(f"Lista actualizada: {list[0:len(list)]}")
else:
    print(f"Producto {eliminar} no encontrado.")
