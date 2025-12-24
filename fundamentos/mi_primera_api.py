from fastapi import FastAPI

app = FastAPI() # Se crea una instancia de la aplicación

@app.get("/") # /es para la raiz
def inicio():
    return "¡Este es mi primer servidor!"

"""
Se debe correr en la terminal el siguiente comando: "uvicorn {modulo actual}:app --reload"
esto crea un servidor ASGI en localhost y abre el puerto 8000, otras opciones:

--port {puerto}: define el puerto en el que se correra la app
--host {ip}: define la IP del servidor, por defecto 127.0.0.1
"""