#7


num = int(input("Ingreseun numero positivo"))

sum = 0
if num < 0:
    num = int(input("Incorrecto. Vuelva a ingresar un numero positivo. "))
else:
    for i in range(0,num + 1 ,1):
        sum += i
    print(f"La suma de los numeros enteros positivos hasta {num} es {sum}")        