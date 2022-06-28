# 1
# Escribir el codigo necesario que muestre
# la cadena de caracteres:
# "Bienvenido al curso Introductorio de Python"

print("Bienvenido al curso de Introductorio de Python")

# 2
# Escribir el codigo necesario de Python que
# pregunte por un nombre de persona
# y luego que este es introducido,
# muestre por pantalla la cadena:
# "Bienvenido al curso Introductorio de Python <nombre> !"
# <nombre> es la persona introducida

nombre = input("Escriba el nombre:")
print(f"Bienvenido al curso Introductorio de Python {nombre} !")

# 3
# Escribir el codigo que lea un entero <n>
# introducido por el usuario y despues
# muestre en pantalla el resultado de la
# siguiente operacion

#         n(n+1)
# suma = -------
#           2

n = int(input("Escriba el valor de n:"))
suma = n * (n + 1) / 2
print(suma)

# 4
# Escribir el codigo que pida dos numeros
# enteros y muestre por pantalla la <n> entre <m> da un cociente <c>
# y un resto <r>
# donde <n> y <m> son los numeros introducidos y <c> y <r> son el cociente y el resto
# de la division entera respectivamente

n = int(input("Escriba n:"))
m = int(input("Escriba m:"))

c = n // m
r = n % m
print(f'n:{n} m:{m} c:{c} r:{r}')