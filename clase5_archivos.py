
# leer un archivo

with open('mis_datos.txt', 'r') as f:
    # leer el archivo todo!
    #mis_datos = f.read()

    # para leer el archivo linea a linea
    mis_datos = f.readlines()

# quitar el salto de linea que tiene al final

# forma tradicional
resultado = []
for mi_linea in mis_datos:

    # quitar el salto de linea
    # acumulo en variable resultado
    resultado.append(mi_linea.rstrip())

# list comprehension
resultado = [mi_linea.rstrip() for mi_linea in mis_datos]


resultado2 = []
for mi_linea in resultado:
    resultado2.append(mi_linea.split(','))

resultado2 = [mi_linea.split(',') for mi_linea in resultado]
pass
# fragmentar el linea del archivo separado por coma

