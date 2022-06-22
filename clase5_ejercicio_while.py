# vamos a crear una aplicacion que almanece datos de personas
# vamos almacenar:
# nombre
# telefono

# para poder hacer consultas sobre los datos almacenados

# guardar la informacion es estructura de datos
# listar la informacion en pantalla

# estrategia de solucion
# definir la estructura de datos
# crear funciones (logica) para poder resolver las mas importante operaciones
# de la aplicacion

# estructura de datos
# una lista de listas

agenda_de_contactos = [
    ['juan', '45678547'],
    ['susana', '5445124'],
    ['carlos', '45452174']
]

def agregar_contacto(nombre, telefono):
    agenda_de_contactos.append([nombre, telefono])

def listar_contactos():
    for nombre, telefono in agenda_de_contactos:
        print(f'Mi amigo {nombre} tiene el telefono {telefono}')

# ciclo que pregunte por un nombre y luego por un telefono
# el ciclo va a salir si el nombre es 'x' y inmediatamente se va mostrar en pantalla
# los contactos

informacion_desde_teclado = ''
while informacion_desde_teclado != 'x':
    nombre = input('Escriba el nombre:')
    if nombre == '10':
        continue
    if nombre == 'x':
        # break
        # continue
        informacion_desde_teclado = nombre
        continue
    telefono = input('Escriba el telefono')

    # agregar contacto
    agregar_contacto(nombre, telefono)

listar_contactos()