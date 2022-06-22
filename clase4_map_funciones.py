

def multiplicar(numero):
    return numero * numero

def sumar(numero):
    return numero + numero

def raiz(numerito):
    return numerito ** 0.5


lista_de_funciones = [sumar, multiplicar, raiz]

# objetivo es ejecutar las funciones que estan en la lista
# en una misma expresion

un_numero = 10

resultado = map(lambda x: x(un_numero), lista_de_funciones)
print(list(resultado))
