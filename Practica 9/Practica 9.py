
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


#3


def potencia(n,m):
    
    if m==0:
        return 1
    else:
        return n * potencia(n, m-1)



num_ingresado = int(input("Ingrese la base: "))
exponente_ingresado = int(input("Ingrese el exponente: "))
resultado = potencia(num_ingresado, exponente_ingresado)
print(f"{num_ingresado} elevado a la {exponente_ingresado} es {resultado}")



#4


def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return  decimal_a_binario(n // 2) + str(n % 2)
    



print(decimal_a_binario(10))


#5


def es_palindromo(palabra):
    # Caso base: una palabra vacía o de un solo carácter es palíndroma
    if len(palabra) <= 1:
        return True
    # Si el primer y el último carácter son distintos, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin el primer y último carácter
    return es_palindromo(palabra[1:-1])


# Programa principal
palabra_ingresada = input("Ingrese una palabra para verificar si es un palíndromo: ").lower()
print(es_palindromo(palabra_ingresada))



#6


def suma_digitos(num):

    if num <= 0:
        return 0
    else:
         digito_anterior = num % 10
       
         
         return  digito_anterior +  suma_digitos(num//10) 



print(suma_digitos(240))



#7



def contar_bloques(n):

    if n == 0:
        return 0
    else:
        return contar_bloques(n-1) + n



numero_bloque = int(input("Ingrese la cantidad de bloques: "))
print(f"Total de bloques que necesita para construir toda la piramide : {contar_bloques(numero_bloque)}")



#8



def contar_digito(num, digito):

    contador = 0

    if num == 0:
        return 0
    else:
        digito_anterior = num % 10
        
        if digito == digito_anterior:  
                
            return 1 + contar_digito(num//10,digito)
        else:
                
            return contar_digito(num//10, digito)
    


print(contar_digito(5555,5))    
    



