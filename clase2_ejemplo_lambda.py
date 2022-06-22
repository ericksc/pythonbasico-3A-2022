

# voy a crear una calculadora
# suma
# resta
# multiplicacion
# division

def calculadora(numero1, numero2, operador):
    # el operador es una funcion
    return operador(numero1, numero2)

# multiplicacion
resultado = calculadora(5, 4, lambda x, y: x * y )
print(resultado)

# suma
resultado = calculadora(5, 4, lambda x, y: x + y )
print(resultado)

# resta
resultado = calculadora(5, 4, lambda x, y: x - y )
print(resultado)

# division
resultado = calculadora(5, 4, lambda x, y: x / y )
print(resultado)

