
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