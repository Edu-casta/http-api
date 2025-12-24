from fastapi import FastAPI

app = FastAPI()
productos = [
    "zanahoria",
    "manzanas",
    "papas",
    "leche",
    "pan",
    "huevos",
    "arroz",
    "frijoles",
    "cebolla",
    "tomates",
    "bananos",
    "queso",
    "pollo",
    "café",
    "azúcar",
    "aceite",
    "aguacate",
    "pasta",
    "naranjas",
    "limones"
]

"""
La paginación básica consiste en usar el Slicing de Python aplicado a los parámetros que recibimos de la URL. 
Usamos skip (cuántos saltar) y limit (cuántos mostrar).
"""

@app.get("/p1-ej1")
def limite_fijo():
    return productos[:5], productos[:5] # Devuelve una tupla con los primeros cinco valores y los últimos cinco valores

@app.get("/p1-ej2")
def limite_dinamico(limite: int = 10):
    return productos[:limite]

@app.get("/p1-ej3")
def paginacion_basica(skip: int = 0, limit: int = 5):
    return productos[skip : skip+limit]

#EJERCICIOS
# 1. Crea un endpoint que siempre se salte los primeros 2 productos de la lista y muestre los siguientes 3.
@app.get("/p1-ex1")
def ejercicio_1(skip: int = 2,limit = 3):
    return productos[skip : skip + limit]

# 2. Crea un endpoint donde el limit sea obligatorio (sin valor por defecto) y el skip siempre sea 0.
@app.get("/p1-ex2")
def ejercicio_2(limit: int):
    skip = 0
    return productos[skip : skip + limit]

# 3. Crea un endpoint que reciba pagina (int). Si el usuario pide la página 1,
#    muestra los productos del 0 al 4. Si pide la página 2, del 5 al 9. (Pista: necesitas multiplicar).
@app.get("/p1-ex3")
def ejercicio_3(pagina: int = 1, tamano: int = 5):
    mostrar = (pagina - 1) * tamano
    return productos[mostrar : mostrar + tamano]

"""
En el tercer endpoint se aplico la lógica de paginas, en vez de calcular por rango de items, se asume que los items están agrupados por paginas
skip y limit se dejan de usar, se introduce simplemente el número de página y su tamaño de la siguiente manera:

(pagina - 1) * tamaño

Se debe restar uno para que si el usuario pide la pagina 1 esta empiece desde el producto 0, al "mostrar" en la primera iteración
tener un valor de cero funciona como un skip que suma con un limite, en este caso tamaño.

[mostrar : mostrar + tamaño]

En las siguientes iteraciones "tamaño" ayuda a que el contenido a mostrar sea agrupado.
"""