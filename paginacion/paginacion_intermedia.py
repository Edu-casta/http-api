from fastapi import FastAPI, HTTPException, status

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
Ahora se trabajará lo que el mundo actual demanda: Lógica de paginas, el usuario siempre pensará
en páginas, no en índices de elementes, a la vez se validan los datos que este envie para evitar:
pagina -5 o un límite de un billón
"""

@app.get("/p2-ej1")
def por_pagina(pagina: int = 1, tamaño: int = 5):
    offset = (pagina - 1) * tamaño
    return productos[offset : offset + tamaño]

    # Forma optimizada: items = productos[(pagina - 1) * tamaño : pagina * tamaño]
    # Normalmente se suele definir un número de "tamaño" definido
    
@app.get("/p2-ej2")
def validacion_basica(limite: int = 10):
    if limite > 100: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Limite demasiado alto")
    return productos[:limite]

@app.get("/p2-ej3")
def pagina_vacia(pagina: int = 1):
    items = productos[(pagina - 1) * 5 : pagina * 5]
    if not items:
        raise HTTPException(status_code=404, detail="Esta pagina no tiene productos")
    return items

#EJERCICIOS

# 1. Modifica el ejemplo de las páginas para que, si el usuario pide la página 0 o menor,
# devuelvas un error 400.
@app.get("/p2-ex1")
def validacion_rango_menor(pagina: int = 1):
    if pagina <= 0: raise HTTPException(status_code=400, detail="Página no valida")
    offset = (pagina - 1) * 5
    return productos[offset : offset + 5]

# 2. Crea un sistema donde el tamaño de página no pueda ser mayor a 20 ni menor a 1.
@app.get("/p2-ex2")
def validacion_rango(pagina: int = 1):
    if pagina < 1 or pagina > 20: raise HTTPException(status_code=400, detail="Rango no valido")
    offset = (pagina - 1) * 5
    return productos[offset : offset + 5]

# 3. Crea un endpoint que reciba una búsqueda (string). Primero filtra la lista usando
# List Comprehension y luego aplica la paginación sobre el resultado filtrado.

@app.get("/p2-ex3", status_code = status.HTTP_200_OK)
def busqueda_segun_str(busqueda: str, pagina: int = 1):
    lista_resultante = [p for p in productos if busqueda.lower() in p]
    if len(lista_resultante) == 0: raise HTTPException(status_code=404, detail="No se han encontrado coincidencias.")
    
    offset = (pagina - 1) * 5
    items = lista_resultante[offset : offset + 5]
    
    if not items: raise HTTPException(status_code=404, detail="No se han encontrado productos.")
    return items
    

