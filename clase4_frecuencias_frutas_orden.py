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


# tener una forma para acceder a la informacion de las cuentas
datos = list(resultado.items())

# sort, sorted -> key

# ciclo
for nombre_fruta, cantidad in sorted(datos, key=lambda x:x[-1]):
    print(f'La fruta {nombre_fruta} les gusta a {cantidad} personas')