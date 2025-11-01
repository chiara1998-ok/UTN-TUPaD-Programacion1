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