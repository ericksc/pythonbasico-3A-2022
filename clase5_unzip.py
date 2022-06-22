

personas_informacion = [
    ('juan', 'heredia', 'juan@gmail.com'),
    ('andres', 'limon', 'andres@gmail.com'),
    ('maria', 'pavas', 'maria@gmail.com')
]

# deseas descomponer la anterior extructura:
# tengas por separado los nombres, los lugares y los emails

resultado = zip(*personas_informacion)

# unpacking!!
nombres, lugares , email = list(resultado)
print(nombres)
print(lugares)
print(email)