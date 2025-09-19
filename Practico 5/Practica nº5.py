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



#3



import random
listPares = []
listImpares = []
contPares = 0
contImpares = 0

for i in range(15):
    numAleatorio = random.randint(1, 100)
    if(numAleatorio % 2 == 0):
        listPares.append(numAleatorio)
        contPares += 1
    else:
        listImpares.append(numAleatorio)
        contImpares += 1

print(f"Números pares: {listPares}")
print(f"Números impares: {listImpares}")
print(f"Cantidad de números pares: {contPares}")
print(f"Cantidad de números impares: {contImpares}")


#4


datos = [1,3,5,3,7,1,9,5,3]




sinRepetidos = list(set(datos))
sinRepetidos.sort()
print(sinRepetidos)



#5


list = ["CHIARA", "JUAN", "MATEO", "ANA", "LUIS", "SOFIA", "CARLA", "DIEGO", "PABLO", "MARIO"]

opcion = int(input("Ingrese 1 para agregar un nombre a la lista o 2 para eliminar un nombre de la lista: "))

if opcion == 1:
    nuevoNombre = input("Ingrese el nombre que desea agregar: ").upper()
    list.append(nuevoNombre)
    list.sort()
    print(f"Lista actualizada: {list[0:len(list)]}")
elif opcion == 2:
    eliminarNombre = input("Ingrese el nombre que desea eliminar: ").upper()
    if eliminarNombre in list:
        list.remove(eliminarNombre)
        print(f"Lista actualizada: {list[0:len(list)]}")
    else:
        print(f"El nombre {eliminarNombre} no se encuentra en la lista.")   


#6


#Creamos e inicializamos las listas con valores
list = [7,8,9,10,5,7,8]
print(list[0:len(list)])
#Guardamos la cantidad de elementos de la lista
cantElementos = len(list)

ultimo = list[cantElementos - 1]

for i in range(cantElementos - 1, 0, -1):
    list[i] = list[i - 1]


list[0] = ultimo                        
print(list[0:len(list)])        #Imprimimos la lista rotada