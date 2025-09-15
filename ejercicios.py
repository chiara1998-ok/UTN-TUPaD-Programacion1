#10

num= int(input("Ingrese un numero entero "))
invertido = 0

while(num > 0):
    digito = num % 10

    invertido = (invertido * 10) + digito

    num = num // 10
    
print(invertido)    