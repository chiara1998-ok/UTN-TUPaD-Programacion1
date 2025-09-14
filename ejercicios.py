

num1 = int(input("Ingrese un numero entero"))
num2 = int(input("Ingrese otro numero entero"))

sum = 0

for i in range(num1 + 1,num2, 1):
    sum += i

print(f"La suma de los numeros enteros entre {num1} y {num2} es {sum}")
