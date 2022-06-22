nombres_edad = (
    ('juan', 20),
    ('pedro', 40),
    ('carlos', 18)
)
# crear un texto juan tiene 20 años
def una_funcion(elemento):
    return f'{elemento[0]} tiene {elemento[1]} años'

resultado = map(una_funcion, nombres_edad)
print(list(resultado))

