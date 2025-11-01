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