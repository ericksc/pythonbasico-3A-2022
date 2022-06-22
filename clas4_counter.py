from collections import Counter

frutas = ['coco',
          'limon',
          'piña',
          'melon',
          'sandia',
          'sandia',
          'papaya',
          'piña',
          'mango',
          'limon',
          'melon',
          'piña',
          'uva',
          'naranja'
          ]

resultado = Counter(frutas)
#print(resultado)

numero_de_sandias = resultado['sandia']
#print(numero_de_sandias)

# la fruta sandia les gusta a 2 compañeros

# ocupamos: tener la coleccion de frutas sin repetir
# 1. le podemos preguntar al resultado del counter si conoce la colecion de las frutas sin repetir
# de objectos como Counter o diccionarios
la_lista_sin_repetir_de_frutas = list(resultado.keys())
pass
# 2. si python en su biblioteca estandar tiene una funcion para tener coleccion sin duplicacion
la_lista_sin_repetir_de_frutas = list(set(frutas))

for mi_fruta in sorted(la_lista_sin_repetir_de_frutas):
    # la fruta sandia les gusta a 2 compañeros
    numero = resultado[mi_fruta]
    print(f'la fruta {mi_fruta} les gusta a {numero} compañeros')