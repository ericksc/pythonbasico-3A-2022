#           0        1        2         3       4           5
frutas = ['apple', 'grape', 'lemon', 'pear', 'blackberry', 'orange']

# # extrar un segmento
#
# # principio hasta el final
# resultado = frutas[:] # unos va a dar toda la coleccion
# print(resultado)
#
# # vamos obtener la coleccion desde el indice 1 en adelante
# resultado = frutas[1:]
# print(resultado)
#
# # desde el indice 1 hasta antes del final
# resultado = frutas[1:-1]
# print(resultado)
#
#
# resultado = frutas[2:4+1]
# print(resultado)
#
# # con salto. de uno en uno
# resultado = frutas[::]
# print(resultado)
#
# # hacer saltos de 2 en 2
# resultado = frutas[::2] # obtener los elementos de indice par
# print(resultado)
#
# resultado = frutas[1::2] # obther los elementos de indice impar
# print(resultado)
#
# resultado = frutas[0:1] + frutas[1::2]
# print(resultado)
#
# resultado = frutas[::-1] # obteniendo la coleccion en reversa
# print(resultado)

# utilizando ciclos con slicing

for mi_fruta in frutas[:]:
    # la fruta apple al reves es elppa
    fruta_al_reves = mi_fruta[::-1] # para leer la palabra al reves
    print(f'la fruta {mi_fruta} al reves es {fruta_al_reves}')