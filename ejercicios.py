#5


def suma_digitos(num):

    if num <= 0:
        return 0
    else:
         digito_anterior = num % 10
       
         
         return  digito_anterior +  suma_digitos(num//10) 



print(suma_digitos(240))
    


