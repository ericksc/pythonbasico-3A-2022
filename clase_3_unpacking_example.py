datos = [123, 456, 789, 321, 456, 786, 123]

# necesita el primero como referencia
# para calcula la diferencia respecto a los demas valores

primero, *los_demas = datos

# para resolver el mini_problema de ir atravez de los elementos de la lista "los_demas"

resultados = []

# ciclos
for valor in los_demas:
    calculo = valor - primero
    resultados.append(calculo)
    print(f'La diferencia es:{calculo}')

pass