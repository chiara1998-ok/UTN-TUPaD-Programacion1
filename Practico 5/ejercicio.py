#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 

producto = ["CAFE", "LECHE", "SERVILLETA", "JABON"]
ventas = [
    [110, 120, 130, 140],
    [101, 144, 120, 130],
    [120, 120, 140, 150],
    [150, 150, 160, 170],
    [182, 190, 200, 210],
    [100, 110, 120, 130],
    [120, 130, 140, 150]
]

suma = 0


for j in range(4):
    for i in range(7):
        ventas[j] += suma
