

def otra_funcion(informacion):
    return informacion * 2

def mi_funcion(data, accion):
    return accion(data)

#mi_funcion('hola mundo', print)

#mi_funcion('hola mundo', 'Juanito')

resultado = mi_funcion('hola mundo', otra_funcion)
print(resultado)
