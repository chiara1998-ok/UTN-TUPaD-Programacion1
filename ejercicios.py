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