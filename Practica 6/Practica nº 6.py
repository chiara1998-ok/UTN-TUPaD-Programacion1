
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