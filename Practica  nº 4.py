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
