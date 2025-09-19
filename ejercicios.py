list = [7,8,9,10,5,7,8]
print(list[0:len(list)])
#Guardamos la cantidad de elementos de la lista
cantElementos = len(list)

ultimo = list[cantElementos - 1]

for i in range(cantElementos - 1, 0, -1):
    list[i] = list[i - 1]


list[0] = ultimo                        
print(list[0:len(list)])        #Imprimimos la lista rotada