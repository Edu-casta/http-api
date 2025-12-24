from fastapi import FastAPI, HTTPException, status
"""
HTTPException sirve para levantar excepciones http, se usa status para describir el estado de la solicitud
"""

app = FastAPI()
lista_de_usuarios = []

@app.get("/")
def index():
    return "Hello World"

@app.get("/usuarios/{nombre}") #Se puede agregar un argumento para la URL
def get_usuario(nombre: str): #Tipado para validación
    if nombre in lista_de_usuarios:
        return {"nombre": nombre}

    #No es necesario un else, al no cumplirse el if va a la excepción
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

@app.post("/usuarios/{nombre}", status_code=status.HTTP_201_CREATED)
def post_usuario(nombre: str):
    if nombre not in lista_de_usuarios:
        lista_de_usuarios.append(nombre)
        return {"nombre": nombre, "mensaje": "Usuario creado"}
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Usuario ya existe")

@app.delete("/usuarios/{nombre}", status_code=status.HTTP_204_NO_CONTENT) #se puede usar un 201 para mandar una pequeña descripción
def delete_usuario(nombre: str):
    if nombre in lista_de_usuarios:
        lista_de_usuarios.remove(nombre)
        return # 204 devuelve nada
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")



