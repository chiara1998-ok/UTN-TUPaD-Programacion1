#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.


num = int(input("Ingrese un numero entero"))
cantDigito = 0

while(num > 0):
        
        digito = num % 10

        cantDigito += 1

        num = num//10


print(f"La cantidad de digitos que contiene el numero ingresado es {cantDigito}")