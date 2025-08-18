#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo!")



#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando  el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre = input("Ingrese su nombre :")


print(f"Hola {nombre}!" )



#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla. 



nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido")
edad = int(input("Ingrese su edad:"))
residencia = input("Ingrese su lugar de residencia")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")




#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.






radio =float(input("Ingrese el radio del circulo"))

pi = 3.1415926535897932

area = float((radio**2)* pi)

perimetro = float(2 * pi * radio)


print(f"El area del circulo es {area} y el perimetro es {perimetro}")




#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.




segundos =int(input("Ingrese los segundos"))

hora = 3600 #cantidad de segundos que tiene una hora



horas = float((segundos *1 ) / hora )

print(f"Los segundos ingresados equivalena a {horas} horas")


# 6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 


numero = int(input("Ingrese un numero"))


print(f"{numero} * 1 es igual a: {numero * 1} ")
print(f"{numero} * 2 es igual a: {numero * 2} ")
print(f"{numero} * 3 es igual a: {numero * 3} ")
print(f"{numero} * 4 es igual a: {numero * 4} ")
print(f"{numero} * 5 es igual a: {numero * 5} ")
print(f"{numero} * 6 es igual a: {numero * 6} ")
print(f"{numero} * 7 es igual a: {numero * 7} ")
print(f"{numero} * 8 es igual a: {numero * 8} ")
print(f"{numero} * 9 es igual a: {numero * 9} ")
print(f"{numero} * 10 es igual a: {numero * 10} ")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


numero1 = int(input("Ingrese el primer numero entero distinto del 0"))

numero2 = int(input("Ingrese el segundo numero entero distinto del 0"))


suma = numero1 + numero2
division = float(numero1 / numero2)
multiplicacion = numero1 * numero2
resta = numero1 - numero2

print(f"El resultado de sumar el primero numero con el segundo es {suma}")
print(f"El resultado de dividir el primer numero con el segundo es {division}")
print(f"El resultado de multiplicar el primero numero con el segundo es {multiplicacion}")
print(f"El resultado de restar el primer numero con el segundo es {resta}")




#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 
#  𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2


altura = float(input("Ingrese su altura en metros"))

peso = float(input("Ingrese su peso en kg"))

mc = (peso) / (altura ** 2)

print(f"El MC segun su peso y altura es {mc}")




# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia: 
# T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 / 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32



celsius = int(input("Ingrese la temperatura en grado Celsius"))

fahrenheit = ((9/5)*celsius) + 32

print(f"{celsius} grados Celsius equivale a {fahrenheit} grados Fahrenheit")



# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de  dichos números. 


numero1 = float(input("Ingrese el primer numero"))
numero2 = float(input("Ingrese el segundo numero"))
numero3 = float(input("Ingrese el tercer numero"))



promedio = (numero1 + numero2 + numero3) / 3


print(f"El promedio de los tres numeros ingresados es {promedio}")



