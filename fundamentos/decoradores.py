def decorador(funcion):
    def suma_compleja(*nums):
        print(f"números a sumar: {nums}")
        resultado = funcion(*nums)
        print(f"resultado: {resultado}")
        return resultado
    return suma_compleja

@decorador
def suma_simple(*nums):
    return sum(nums)

numeros = range(10,110,2)
suma_simple(*numeros)