
# como crear un diccionario
# cualquier de informacion .. cualquier tipo de dato

mi_diccionario = {
    'carlos': {'canton': 'alajuelita',
               'provincia': 'san jose',
               'correo': 'carlos@gmail.com',
               'telefono': '123'
               },
    'luis': {'canton': 'cartago',
             'provincia': 'cartago',
             'correo': 'luis@gmail.com',
             'telefono': '987'},
    'andres': {'canton': 'san francisco',
               'provincia': 'heredia',
               'correo': 'andres@gmail.com'},
    'maria': {'canton': 'grecia',
              'provincia': 'alajuela',
              'correo': 'maria@gmail.com',
              'telefono': '456'}
}

# para acceder a los datos de un diccionario
# telefono_carlos = mi_diccionario['andres']
# print(telefono_carlos)

# para agregar elementos al diccionario
# mi_diccionario['juan'] = 88327166
#
# informacion_juan = mi_diccionario['juan']
# print(informacion_juan)

# como podemos acceder al correo de maria
#
# correo = mi_diccionario['maria']['correo']
# print(correo)

# # hacer una iteracion atravez de los datos del diccionario
# for amigo in mi_diccionario:
#     # utilizando la funcion get
#     #print(mi_diccionario[amigo]['telefono'])
#     print(mi_diccionario[amigo].get('telefono', '0000-0000'))

# iteracion por los valores

for amigo, datos_de_amigo in mi_diccionario.items():
    canton = datos_de_amigo.get('canton', '')
    telefono = datos_de_amigo.get('telefono', '(506)0000-0000')
    print(f'El amigo {amigo} vive en {canton} y tiene telefono {telefono}')