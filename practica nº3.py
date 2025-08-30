#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese su edad"))

if (edad > 18) :
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”;
#  en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota"))

if (nota >= 6) :
    print("Aprobado")
else:
    print("Desaprobado")    


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”;
#  en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota"))

if (nota >= 6) :
    print("Aprobado")
else:
    print("Desaprobado")    


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 


numPar = int(input("Ingrese un numero par"))



if (numPar % 2 == 0):
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 


edad = int(input("Ingrese su edad"))


if(edad < 12):
    print("Niño/a")
elif(edad >= 12 and edad < 18):
    print("Adolecente")
elif(edad >= 18 and edad < 30):
    print("Adulto/a joven")
else:
    print("Adulto/a")           



#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

contraseña = input("Ingrese una contraseña")

if(len(contraseña) >= 8 and len(contraseña) <= 14):
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 



from statistics import mode, median, mean 

import random 

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(numeros_aleatorios)
if (media > mediana and mediana > moda):
    print("Hay sesgo positivo")
elif (media < mediana and mediana < moda ):
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")    


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.
# 



frase = input("Ingrese una frase o palabra")
length = len(frase)

last = frase[length-1]

if(last == "a"  or last == "e" or last == "i" or last == "u" or last == "o"  ):
    resultante = frase + "!"
    print(resultante)
else:
    print(frase)    


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.


nombre = input("Ingrese su nombre")
opcion = int(input("Ingrese un numero dependiendo la opcion que desee: 1.Si quiere su nombre en mayúsculas" " 2.Si quiere su nombre en minúsculas" " 3. Si quiere su nombre con la primera letra mayúscula "))
if(opcion == 1):
    mayusculas = nombre.upper()
    print(mayusculas)
elif(opcion == 2):
    minusculas = nombre.lower()
    print(minusculas)
else:
    primerLetra = nombre.title() 
    print(primerLetra)         