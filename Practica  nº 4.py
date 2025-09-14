# Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.



for cont in range(0,101,1):

    print(cont)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.


num = int(input("Ingrese un numero entero"))
cantDigito = 0

while(num > 0):
        
        digito = num % 10

        cantDigito += 1

        num = num//10


print(f"La cantidad de digitos que contiene el numero ingresado es {cantDigito}")    



#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero entero"))
num2 = int(input("Ingrese otro numero entero"))

sum = 0

for i in range(num1 + 1,num2, 1):
    sum += i

print(f"La suma de los numeros enteros entre {num1} y {num2} es {sum}")



#4

sum = 0
num = int(input("Ingrese un numero o aprete 0 para salir: "))
while(num != 0):
    sum += num
    num = int(input("Ingrese un numero o aprete 0 para salir: "))

    


print(f"El total acumulado es {sum}")


# 5
import random

intentos = 1

num_aleatorio = random.randint(0, 10) 


numIngresado = int(input("Ingrese un numero entre 0 y 9: "))

while(numIngresado != num_aleatorio):

    intentos += 1
    numIngresado = int(input("Numero incorrecto, ingrese otro numero entre 0 y 9: "))


print(f"Felicidades, ha adivinado el numero {num_aleatorio} en {intentos} intentos")    




#6 

for i in range(100,-1,-2):
    print(i)



#7


num = int(input("Ingreseun numero positivo"))

sum = 0
if num < 0:
    num = int(input("Incorrecto. Vuelva a ingresar un numero positivo. "))
else:
    for i in range(0,num + 1 ,1):
        sum += i
    print(f"La suma de los numeros enteros positivos hasta {num} es {sum}")            