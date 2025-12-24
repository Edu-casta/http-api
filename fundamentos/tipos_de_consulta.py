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

#path param, se usa para identificar un recurso único
@app.get("/productos/{nombre}", status_code=status.HTTP_200_OK)
def get_producto(nombre: str): #se usa un parametro fijo
    if nombre in productos:
        return nombre
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#query param, filtra una lista
@app.get("/producto/{nombre}")
def get_productos(limite: int = 5):
    return productos[:limite]

