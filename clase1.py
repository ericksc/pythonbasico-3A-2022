# voy al super y compro 3 frutas
# mango cuesta 100, manzana cuesta 50 y un limon que cuesta 30

# cuanto debo pagar si quiero el mango , la manzana y el limon

# ocupamos sumar los valores de los precios de las frutas

# suponga que las frutas tienen un 13% de impuesto al valor agregado
# cual es el precio final al comprar las frutas?
from precios import mango, manzana, limon


costo = mango + manzana + limon
# 1 + 0.13 -----> 1.13
costo_final = costo * 1.13

print(costo_final)

# seria el costo del mango igual a 200
print(mango == 100)

print('hola a mundo')

# concatenar
mensaje_completo = 'hola' + ' ' + 'a todos'
print(mensaje_completo)


