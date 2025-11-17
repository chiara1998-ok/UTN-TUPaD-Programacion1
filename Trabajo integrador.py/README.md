📘 Descripción del Programa

Este programa permite gestionar, analizar y almacenar información sobre países utilizando estructuras de datos y técnicas fundamentales de programación en Python.

El sistema trabaja con un archivo CSV donde se registran los países y, al iniciar, carga sus datos en una lista de diccionarios. Desde un menú interactivo, el usuario puede:

Agregar países nuevos al CSV y a la lista en memoria

Actualizar población y superficie de un país existente

Buscar un país por nombre

Filtrar países por continente, rango de población o superficie

Ordenar países por nombre, población o superficie

Realizar estadísticas (promedios, máximos, mínimos, conteos)

Las funciones principales se encuentran en el módulo operaciones.py 

operaciones

, mientras que el programa principal (control del menú, carga del CSV y flujo general) se desarrolla en Trabajo integrador.py 

Trabajo integrador

.

🧭 Instrucciones de Uso

Ejecutar el archivo principal

python Trabajo integrador.py


Al iniciar, el programa:

Verifica si el archivo CSV existe

Si no existe, lo crea con los encabezados

Carga todos los países en memoria

Se muestra un menú con 7 opciones:

1. Agregar un país
2. Actualizar datos de población y superficie
3. Buscar un país
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Salir


El usuario debe ingresar un número del 1 al 7 según la acción que desea realizar.

Las operaciones se ejecutan hasta que el usuario ingresa 7 (Salir).

🧪 Ejemplos de Entradas y Salidas
✔ Ejemplo 1 – Agregar un país

Entrada del usuario:

1
Ingrese la cantidad de paises que desea ingresar: 1
Ingrese el pais que desea ingresar: chile
Ingrese la poblacion: 19000000
Ingrese la superficie en km2: 756102
Ingrese el continente del pais ingresado: America


Salida:

Se ha ingresado : {'nombre': 'chile', 'poblacion': 19000000, 'superficie': 756102, 'continente': 'America'}

✔ Ejemplo 2 – Buscar un país

Entrada:

3
Ingrese el país que desea buscar: argentina


Salida:

{'nombre': 'argentina', 'poblacion': 45000000, 'superficie': 2780000, 'continente': 'america'}

✔ Ejemplo 3 – Filtrar por continente

Entrada:

4
1
Ingrese el continente por el que desea filtrar: Europa


Salida:

Países en el continente Europa:
{'nombre': 'francia', 'poblacion': 67800000, 'superficie': 643801, 'continente': 'Europa'}
{'nombre': 'alemania', 'poblacion': 83100000, 'superficie': 357386, 'continente': 'Europa'}

✔ Ejemplo 4 – Estadísticas: País con mayor y menor población

Entrada:

6
1


Salida:

El país con MAYOR población es: china (1402000000)
El país con MENOR población es: islandia (372000)

