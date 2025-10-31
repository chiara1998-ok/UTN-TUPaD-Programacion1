
#1

#Definir la función
def imprimir_hola_mundo():
    print("Hola Mundo")
#Programa principal
imprimir_hola_mundo()


#2

#Definir la función
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

#Programa principal
nombre_usuario = input("Ingresa tu nombre: ")
saludar_usuario(nombre_usuario)


#3

#Definir la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)




#4
import math
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


#Programa principal
radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")




#5

def segundos_a_horas(segundos):
    hora = segundos / 3600

    return hora


segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} horas.")



#6


def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")
        
            

    return resultado




#Programa principal
num = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)


#7


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    
    return suma, resta, multiplicacion, division




#Programa principal
num1 = int(input("Ingresa el primer número entero distinto de 0: "))
num2 = int(input("Ingresa el segundo número entero distinto de 0: "))
suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#8


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc



#Programa principal
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")



#9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



#Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")




#10


def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    return promedio




#Programa principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los numeros ingresados es: {promedio}")