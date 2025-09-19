1#

list = [7,7,8,9,10,5,7,8,9,6]

notaAlta = max(list)
notaBaja = min(list)
for cont in range(len(list)):

    
        sum(list)
       



print(list[0:len(list)])
print(f"El promedio es {sum(list)/len(list)}")
print(f"La nota mas alta es {notaAlta}")
print(f"La nota mas baja es {notaBaja}")


2#

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
