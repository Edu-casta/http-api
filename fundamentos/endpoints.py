from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def bienvenida():
    return "Bienvenido a la app"

@app.get("/contacto")
def contacto():
    return "contacto@api.com"

