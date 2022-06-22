# ejemplo del zip

nombres = ['alejandro', 'jonathan', 'juan']

edades = [31, 25, 40]

resultado = zip(nombres, edades)
#print(list(resultado))

for mi_amigo, vida in resultado:
    print(f'Mi amigo {mi_amigo} tiene {vida} años')