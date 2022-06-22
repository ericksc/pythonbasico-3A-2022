
def sumar(a, b):
    if isinstance(a, int):

        return a + b
    else:
        print('diay a no es entero')

c = sumar('hello', 5)
print(c)