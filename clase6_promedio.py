
valor1 = 10
valor2 = 20
valor3 = 30
datos = [valor1, valor2, valor3]

# resultado = 0
# for numero in datos:
#     resultado += numero
#
# promedio = resultado / len(datos)
# print(promedio)

# invitemos a la funcion sum

# promedio = sum(datos) / len(datos)
# print(promedio)

# usando funciones

def promedio(*valores):
    return sum(valores) / len(valores)


resultado = promedio(10,20,30, 40, 50 , 60,70, 432, 5,4, 7, 321, 423,3 ,21)
print(resultado)

def funncion_hueca():
    pass

print('fddasa')