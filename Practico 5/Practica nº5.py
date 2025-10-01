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



#7

diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
listTemperatura = [
    [18,37],
    [20,38],                        
    [19,35],
    [17,34],
    [15,33],
    [14,32],
    [13,31],
]

sumMaximas = 0
sumMinimas = 0
mayorAmplitud = -1
indiceMayor = -1

for i in range(7):
    sumMinimas += listTemperatura[i][0]
    sumMaximas += listTemperatura[i][1]



promMax = sumMaximas / 7
promMin = sumMinimas / 7


for i in range(7):
    min_dia = listTemperatura[i][0]
    max_dia = listTemperatura[i][1]

    amplitud = max_dia - min_dia

    if amplitud > mayorAmplitud:
        mayorAmplitud = amplitud
        indiceMayor = i

print(f"La mayor amplitud térmica de la semana fue de {mayorAmplitud} el día {diasSemana[indiceMayor]}")
print(f"La temperatura media mínima de la semana fue de {round(promMin,2)}")
print(f"La temperatura media máxima de la semana fue de {round(promMax,2)}")



#8


materias = ["Matematica","Fisica","Quimica"]
estudiantes = ["Juan","Maria","Pedro","Ana","Luis"]
notas = [
    [8, 9, 7],  # Notas de Juan
    [8, 9, 8],  # Notas de Maria
    [7, 8, 8],  # Notas de Pedro
    [9, 9, 8],  # Notas de Ana
    [7, 7, 8]   # Notas de Luis
]
sum = 0
promedio = 0



for i in range(5):
        sum = notas[i][0] + notas[i][1] + notas[i][2]
        promedio = (sum / 3)
        print(f"El promedio de {estudiantes[i]} es: {promedio}")#1


for j in range(3):
        sum = 0
        for i in range(5):
                sum += notas[i][j]
        promedio = sum / 5
        print(f"El promedio de {materias[j]} es: {promedio}")#2 



#9
lista = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

while True:
    
    
        fila = int(input("Fila (0,1,2): "))
        columna = int(input("Columna (0,1,2): "))
   

        opcion = input("Símbolo (X/O): ").strip().upper()
        if opcion not in ("X", "O"):
            print("Usa X u O.")
            continue

        if fila not in (0,1,2) or columna not in (0,1,2):
            print("Fuera de rango (0,1,2).")
            continue

        if lista[fila][columna] != "-":
            print("Ese lugar está ocupado.")
            continue

        # colocar jugada
        lista[fila][columna] = opcion

        # mostrar tablero
        for r in lista:
            print(r)

        # ---- comprobar FILA ----
        completa_fila = True
        j = 0
        while j < 3:
            if lista[fila][j] != opcion:
                completa_fila = False
                break
            j += 1

        # ---- comprobar COLUMNA ----
        completa_columna = True
        i = 0
        while i < 3:
            if lista[i][columna] != opcion:
                completa_columna = False
                break
            i += 1

        # finalizar si hay fila o columna completa
        if completa_fila or completa_columna:
            if completa_fila:
                print(f"¡{opcion} completó una fila! Fin del juego.")
            else:
                print(f"¡{opcion} completó una columna! Fin del juego.")
            break
