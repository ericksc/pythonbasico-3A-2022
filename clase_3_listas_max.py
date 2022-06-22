frutas = ['apple', 'grape', 'blackberry', 'orange', 'cas', 'kiwi', 'albaricoque']
print(frutas)

# obtener el maximo por el tamaño de la palabra
# la palabras mas larga

resultado = max(frutas, key=len)
print(resultado)

# la palabra mas corta
mas_corta = min(frutas, key=len)
print(mas_corta)