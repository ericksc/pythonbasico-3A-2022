impuesto = 1.13

with open('lista_compras.txt', 'r') as f:
    lista = f.readlines()

quita_fin_de_linea = [elemento.rstrip() for elemento in lista]

# # tradicionalmente
# quita_fin_de_linea = []
# for elemento in lista:
#     #puedo agregar mas logica
#     quita_fin_de_linea.append(elemento.rstrip())


lista_fruta_precio = [elemento.split(',') for elemento in quita_fin_de_linea]

lista_fruta_precio_impuesto = []
for fruta, precio in lista_fruta_precio:
    lista_fruta_precio_impuesto.append([fruta, str(round(int(precio) * impuesto))])

list_reglon = [','.join(elemento) for elemento in lista_fruta_precio_impuesto]

#pone_fin_de_linea = [f'{elemento}\n' for elemento in list_reglon]
pone_fin_de_linea = [elemento for elemento in list_reglon]

with open('lista_compras_procesada.txt', 'w') as f:
    f.writelines(pone_fin_de_linea) # ocupa una lista de reglones!!!!

