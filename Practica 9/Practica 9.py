
#1



def fact(num):

   return 1 if num == 0 else num * fact(num-1)
    

print(fact(5))



num_ingresado = int(input("Ingrese un número para calcular su factorial: "))
resultado = fact(num_ingresado)
print(f"El factorial de {num_ingresado} es {resultado}")




#2


def fibonacci_recursiva(p):
    if p == 0:
     return 0
    elif p == 1:
       return 1
    else:
       return fibonacci_recursiva(p-1) + fibonacci_recursiva(p-2)
    


print(fibonacci_recursiva(7))


posicion = int(input("Ingrese la posición de la serie Fibonacci que desea calcular: "))

for i in range(posicion+1):
   print(f"Posicion {i}: {fibonacci_recursiva(i)}")