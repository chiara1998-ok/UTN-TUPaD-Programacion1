
#1



def fact(num):

   return 1 if num == 0 else num * fact(num-1)
    

print(fact(5))



num_ingresado = int(input("Ingrese un número para calcular su factorial: "))
resultado = fact(num_ingresado)
print(f"El factorial de {num_ingresado} es {resultado}")