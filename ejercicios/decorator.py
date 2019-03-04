def sucesor(n):
    return n+1
def decorador_funcion(funcion):
    def envoltorio(*args):
        return sucesor(funcion(*args))
    return envoltorio
@decorador_funcion
def suma(a,b):
    return a + b
print(suma(1,1))
