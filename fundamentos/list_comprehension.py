# Expresion for elementos in iterable if condicion
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

# 1. For loop a una sola linea, lista con los nombres de los productos que tienen más de 5 letras.
def sin_lc():
    filtrados = []
    for p in productos:
        if len(p) > 5:
            filtrados.append(p)
def con_lc():
    """
    La primera p funciona como una expresión para saber que hacer con el elemento final, si se deja vacio es un append al elemento declarado
    for p in productos es la manera de recorrer la lista "productos"
    el if del final es una condición que se añade para si se cumple, se ejecute la expresión
    list comprehension sigue este orden en ejecuciíb: 3 1 2.
    """
    filtrados = [p for p in productos if len(p) > 5]
    print(filtrados)

# 2.1 Transformando el elemento
def transformando_elemento(limite = 3):
    elementos_modificados = [elemento.upper() for elemento in productos]
    return elementos_modificados[:limite]

# forma alternativa: return [e.upper() for e in productos][:limite]

print(transformando_elemento(6))
print(transformando_elemento(1))
print(transformando_elemento(9))

# 2.2 Transformando el elemento, Quieres solo los productos que contienen una letra definida.
def obteniendo_productos_con_letra(letra, limite = 5):
    return [producto for producto in productos if letra in producto][:limite]

print(obteniendo_productos_con_letra("a"))
print(obteniendo_productos_con_letra("f"))
print(obteniendo_productos_con_letra("z"))

# 2.3 Transformación + Filtrado, Quieres solo los productos que empiezan con "p", pero quieres que en la lista aparezca cuánto mide cada palabra.
def longitud_de_productos_que_empiezan_con_p(limite=4):
     return [len(producto) for producto in productos if producto.startswith("p")][:limite]

print(longitud_de_productos_que_empiezan_con_p(10))

# EJERCICIOS

# 3.1 Crea una lista que solo tenga los productos que terminen con la letra "s".
def termina_con_s():
    return [p for p in productos if p.endswith("s")]

print(termina_con_s())

# 3.2 Crea una lista que contenga el índice y el nombre (puedes usar enumerate).
def indice_nombre():
    return [p for p in enumerate(productos)]

print(indice_nombre())

# 3.3 Crea una lista de booleanos que diga True si el producto tiene más de 7 letras y False si no.
# si hay un else, el condicional DEBE de ir al inicio
def lista_boleanos():
    return [True if len(p) > 7 else False for p in productos]
    # forma optimizada:
    # [len(p) > 7 for p in productos]
    # Recordar que una operación de comparación ya devuelve True o False













