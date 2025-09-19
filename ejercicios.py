#3



import random
listPares = []
listImpares = []
contPares = 0
contImpares = 0

for i in range(15):
    numAleatorio = random.randint(0, 100)
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
