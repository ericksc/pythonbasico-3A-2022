
#        0  1  2  3  4
datos = [5, 4, 3, 2, 9]

# la funcion enumerate

def detector_de_pares(numero):
    return numero % 2 == 0

valores_de_indice_par = []
valores_de_indice_impar = []

for indice, valor in enumerate(datos):
    print(f'El indice {indice} corresponde al valor {valor}')
    if detector_de_pares(indice):
        valores_de_indice_par.append(valor)
    else:
        valores_de_indice_impar.append(valor)

print(datos)
print(valores_de_indice_par)
print(valores_de_indice_impar)