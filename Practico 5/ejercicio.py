#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 

producto = ["CAFE", "LECHE", "SERVILLETA", "JABON"]
dias_semana = [ "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] 
ventas = [
    [110, 120, 130, 140, 120, 130, 140],
    [101, 144, 120, 130, 100, 110, 120],
    [120, 120, 140, 150, 182, 190, 200],
    [8000, 150, 40000, 170, 800, 500, 1000]
    
    
]

suma = 0
ventas_totales_dia = 0
ventas_dia_anterior = 0
mayor_ventas_prod = -1



for i in range(4):
    sum = 0
    for j in range(7):
        
        sum += ventas[i][j]
       

    print(f"El total por cada {producto[i]} es {sum}")   


    if sum > mayor_ventas_prod:
         mayor_ventas_prod = sum
         prod_mas_vendido = producto[i]

mayor_ventas_dia = -1       


for j in range(7):
    ventas_totales_dia  = 0
    for i in range(4):
        ventas_totales_dia += ventas[i][j]
        
        
     
     
    if ventas_totales_dia > ventas_dia_anterior:
        dia_Mayor_Venta = dias_semana[j]
        ventas_dia_anterior = ventas_totales_dia

print(f"El dia con mayores ventas totales fue {dia_Mayor_Venta}, por un importe de {ventas_dia_anterior}")

print(f"El producto mas vendido de la semana fue {prod_mas_vendido} por un importe de {mayor_ventas_prod} ")

