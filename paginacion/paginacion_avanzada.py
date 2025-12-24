from fastapi import FastAPI, HTTPException, status
from math import ceil

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

@app.get("/p3-ex1")
def metadata_basica(pagina: int = 1):
    limite = 5
    return {
        "total_items": len(productos),
        "pagina_actual": pagina,
        "data": productos[(pagina - 1) * limite : pagina * limite] 
    }
    
@app.get("/p3-ex2")
def total_paginas():
    tamano = 5
    total = ceil(len(productos) / tamano)
    return {"total_paginas": total}

@app.get("/p3-ex3")
def buscador_completo(query: str = "", page: int = 1):
    tamano = 5
    filtrados = [p for p in productos if query.lower() in p.lower()]
    paginas_totales = ceil(len(filtrados) / tamano)
    
    if not filtrados: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se encontraron coincidencias.") # No hay items
    if page > paginas_totales or page <= 0: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pagina no encontrada.") # Pagina no valida
    
    return {
        "total_items": len(productos),
        "items": filtrados[(page - 1) * tamano : page * tamano],
        "pagina_actual": page,
        "paginas_totales": paginas_totales
    }
    
    
# Crea un endpoint que devuelva: la lista paginada, el total de resultados encontrados tras el filtro y un booleano has_next que sea True si hay una página siguiente disponible.

@app.get("/p3-ej")
def busqueda(q : str = "", page : int = 1, s : int = 5): # Si el string se deja como un query param, devuelve la lista completa
    # List Comprehension a productos, items son los resultados encontrados tras el filtro
    items_filtrados = [p for p in productos if q.lower() in p.lower()]
    
    # Validamos items
    if not items_filtrados: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay coincidencias.")
    
    # Calcular metadatos
    total_resultados = len(items_filtrados)
    total_paginas = ceil(total_resultados / s) # Regla de oro: Las páginas totales se calculan sobre la lista de resultados ya filtrados (items)
    
    # Validamos rango de pagina
    if page > total_paginas or page <= 0: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Pagina no valida.")
    
    # Paginamos
    offset = (page - 1) * s
    data_paginada = items_filtrados[offset : offset + s]
    
    # Comprobamos si hay más páginas
    has_next = page < total_paginas
    
    # Enviamos data
    return {
        "items": data_paginada, # Siempre enviar la data paginada
        "total_resultados": total_resultados,
        "pagina_actual": page,
        "paginas_totales": total_paginas,
        "has_next": has_next
    }
    
    
    
    
    
    