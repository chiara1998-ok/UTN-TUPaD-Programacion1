
#1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 



precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300




#2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 



precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300



precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800



#3


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 



precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300



precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

lista = list(precios_frutas)

print(lista)


#4

contactos = {}


for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    contactos[nombre] = telefono



nombre_ingresado = input("Ingrese el nombre del contacto a buscar: ")
if nombre_ingresado in contactos:
    print(f"El teléfono de {nombre_ingresado} es {contactos[nombre_ingresado]}")
else:
    print(f"Contacto {nombre_ingresado} no encontrado.")



#5

frase = input("Ingrese una frase: ")

palabras_unicas = set(frase.split())


recuento = {}
for palabra in palabras_unicas:
    recuento[palabra] = frase.count(palabra)



print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")



#6


alumnos = { 

    "Chiara": ( 8,9,10),    
    "Sofia": ( 7,8,9),
    "Mateo": ( 9,10,7),
    }

alumnosPromedio = {}
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    alumnosPromedio[nombre] = promedio


print(f"El promedio de {alumnos} es {alumnosPromedio}")



#7

estudiantes_parcial1 = {101, 102, 103, 104, 105, 106}
estudiantes_parcial2 = {101, 102, 105}

aprobaron_ambos = estudiantes_parcial1 & estudiantes_parcial2
algun_parcial = estudiantes_parcial1 | estudiantes_parcial2

aprobaron_uno = estudiantes_parcial1 ^ estudiantes_parcial2

print(f"Estudiantes que aprobaron ambos parciales: {aprobaron_ambos}")

print(f"Estudiantes que aprobaron solo uno de los parciales: {aprobaron_uno}")
print(f"Estudiantes que aprobaron al    menos un parcial: {algun_parcial}")



#8



stock = {
    "Laptop": 30,
    "Smartphone": 40,
    "Tablet": 20,
    "Monitor": 15  
}

opcion = input("Ingrese una opcion : consultar, agregar ").lower()

while opcion not in ["consultar", "agregar"]:
    print("Opción no válida. Por favor, ingrese 'consultar' o 'agregar'.")
    opcion = input("Ingrese una opcion : consultar, agregar").lower()
match opcion:
    case "consultar":
        consultar_stock = input("Ingrese el nombre del producto para consultar su stock: ")
        if consultar_stock in stock:
            print(f"El stock de {consultar_stock} es: {stock[consultar_stock]} unidades.")
        else:
            print(f"Producto {consultar_stock} no encontrado en el stock.")
    case "agregar":
        agregar_producto = input("Ingrese el nombre del producto para agregar al stock: ")
        if agregar_producto in stock:
            cantidad_agregar = int(input(f"Ingrese la cantidad de {agregar_producto} a agregar: "))
            stock[agregar_producto] += cantidad_agregar
            print(f"Se han agregado {cantidad_agregar} unidades de {agregar_producto}. Nuevo stock: {stock[agregar_producto]} unidades.")
        else:
            nuevo_producto = input("El producto no existe. Ingrese el nombre del nuevo producto: ")
            cantidad_nuevo = int(input(f"Ingrese la cantidad de {nuevo_producto} a agregar: "))
            stock[nuevo_producto] = cantidad_nuevo
            print(f"Se ha agregado el nuevo producto {nuevo_producto} con un stock de {cantidad_nuevo} unidades.")
    case _:
        print("Opción no válida.")



#9


agenda ={  
    ("Lunes", "10:00"): "Reunión con el equipo",
    ("Martes", "14:00"): "Cita con el médico",
    ("Miércoles", "09:00"): "Clase de yoga",
    ("Jueves", "16:00"): "Llamada con el cliente",
    ("Viernes", "12:00"): "Almuerzo con amigos"
 }


dia = input("Ingrese el día de la semana: ")
hora = input("Ingrese la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")


#10

capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Uruguay": "Montevideo"
}
print(f"Capitales: {capitales}")

invertido = {capital: pais for pais, capital in capitales.items()}
print(f"Invertido: {invertido}")




