




def agregar_pais(a,b,c,d):

    
    
    return {
        "nombre": a,
        "poblacion": b,
        "superficie": c,
        "continente": d
    }



def actualizar_datos(nombre,nueva_poblacion,nueva_superficie,continente):

  


   return {
            "nombre" : nombre,
            "poblacion" : nueva_poblacion,
            "superficie" : nueva_superficie,
            "continente" : continente
   }



def buscar_pais(paises, nombre_buscado):
    nombre_buscado = nombre_buscado.lower().strip()

    for pais in paises:
        if pais["nombre"] == nombre_buscado:
            return pais   
    


def min_p(p):


    return min(p)


def max_p(p):


    return max(p)


def promedio_p(paises):
    total_poblacion = 0
    cantidad_paises = 0

    for pais in paises:
       
        cantidad_paises += 1
        total_poblacion += pais["poblacion"]

    promedio = total_poblacion / cantidad_paises
    return promedio
    
def promedio_s(paises):
    total_superficie = 0
    cantidad_paises = 0

    for pais in paises:
       
        cantidad_paises += 1
        total_superficie += pais["superficie"]

    promedio = total_superficie / cantidad_paises
    return promedio


def contar_paises_por_continente(paises):
    conteo = {}

    for pais in paises:
        continente = pais["continente"]
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1

    return conteo



def filtrar_paises_por_continente(paises, continente_buscado):
    paises_filtrados = []

    for pais in paises:
        if pais["continente"].lower() == continente_buscado.lower():
            paises_filtrados.append(pais)

    return paises_filtrados



def filtrar_paises_por_rango_poblacion(paises, poblacion_min, poblacion_max):
    paises_filtrados = []

    for pais in paises:
        if poblacion_min <= pais["poblacion"] <= poblacion_max:
            paises_filtrados.append(pais)

    return paises_filtrados


def filtrar_paises_por_rango_superficie(paises, superficie_min, superficie_max):
    paises_filtrados = []

    for pais in paises:
        if superficie_min <= pais["superficie"] <= superficie_max:
            paises_filtrados.append(pais)

    return paises_filtrados



def ordenar_paises_por_nombre(paises):
    return sorted(paises, key=lambda pais: pais["nombre"])


def ordenar_paises_por_poblacion(paises):
    return sorted(paises, key=lambda pais: pais["poblacion"])

def ordenar_paises_por_superficie(paises):
    
    return sorted(paises, key=lambda pais: pais["superficie"])


