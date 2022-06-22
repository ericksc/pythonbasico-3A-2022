lista = [3, 5 , 8 , 9, 1, 2]

primero, *los_demas = lista
diferencia = []

for value in los_demas:
    calculo = abs(value - primero)
    diferencia.append(calculo)

# lo nuevo. obtención del menor
menor = min(diferencia)
donde_esta_el_menor = diferencia.index(menor)
el_numero_mas_cerca_del_primero = los_demas[donde_esta_el_menor]

print(f'los datos originales:{lista}')
print(f'El primero es:{primero}')
print(f'las diferencias respecto al primero son:{diferencia}')
print(el_numero_mas_cerca_del_primero)



