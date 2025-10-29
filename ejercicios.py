
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