frutas = ['apple', 'grape', 'blackberry', 'orange', 'cas', 'kiwi', 'albaricoque']


# reemplazar apple por pear

posicion = frutas.index('apple')

frutas.pop(posicion)

frutas.insert(posicion, 'pear')
pass