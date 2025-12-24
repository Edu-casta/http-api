"""
Imagina que eres el encargado del Backend de una tienda virtual. Tienes tu lista de 20 productos y 
necesitas un endpoint profesional que los clientes (Frontend) puedan usar para mostrar el catálogo.

Requisitos del Endpoint:
Ruta: @app.get("/catalogo").

Búsqueda: Query Param q (opcional). Si viene vacío, se usan todos los productos.

Ordenamiento: Query Param orden. Debe aceptar solo dos valores: "asc" (A-Z) o "desc" (Z-A).

Pista: Usa la función sorted(lista) o lista.sort().

REGLA IMPORTANTE: Debes ordenar antes de paginar.

Paginación: Query Params page (defecto 1) y size (defecto 4).

Validaciones:

Si page es menor a 1, lanza HTTPException 400.

Si size es mayor a 10, lanza HTTPException 400 (no queremos sobrecargar la red).

Si después de filtrar no hay nada, lanza HTTPException 404.

Respuesta Final: Debe ser un diccionario con esta estructura exacta:

{
    "meta": {
        "total_items": 20,
        "total_pages": 5,
        "current_page": 1,
        "page_size": 4,
        "has_next": true,
        "order": "asc"
    },
    "data": ["aguacate", "arroz", "azúcar", "bananos"]
}
"""

from fastapi import FastAPI, HTTPException, status
import math

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

@app.get("/catalogo")
def obtener_catalogo(page : int = 1, size : int = 4, query : str = "", sort : str = "asc"):
    # Validar args
    if page < 1: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Número de página no valido.")
    if size > 10 or size < 1: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
    # List Comprehension
    data = [p for p in productos if query.lower() in p.lower()]
    
    # Validar items
    if not data: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No se han encontrado coincidencias.")
     
    # Sort
    if sort == "asc": data.sort()
    elif sort == "desc": data.sort(reverse = True)
    else: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Parametro sort no valido.")
    
    # Cálculo de páginas
    total_pages = math.ceil(len(data) / size)
    has_next = page < total_pages
    
    # Paginar
    offset = (page - 1) * size
    offset_data = data[offset : offset + size] # Recordatorio personal, siempre hacer el offset desde la lista modificada (en este caso data), no la original: productos
    
    return {
        "meta" : {
            "total_items": len(data),
            "total_pages": total_pages,
            "current_page": page,
            "page_size": size,
            "has_next": has_next,
            "order": sort
        },
        "data": offset_data
    }
    