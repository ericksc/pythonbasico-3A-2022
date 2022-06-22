
with open('mi_libro.txt', 'a') as f:

    mis_reglones = [
        'y entonces exclamo!\n',
        'vamos!!\n',
        'y dijo te estoy esperando\n'
    ]

    f.writelines(mis_reglones)

with open('mi_libro.txt', 'r') as f:
    mi_libro = f.read()
print(mi_libro)