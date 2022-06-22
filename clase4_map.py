frutas = ['cas', 'mora', 'guanabana']

# pasar a mayusculas los nombres de las frutas
#lambda nombre: nombre.upper()

# str.upper()
#                una funcion                , coleccion
resultado = map(lambda nombre: nombre.upper(), frutas)
print(list(resultado))








