import pickle

mis_datos = [
    ('carlos', 100, 'heredia'),
    ('juan', 150, 'san jose'),
    ('maria', None, 'alajuela'),
    ('andres', 1.5, None)
]

with open('mi_info.p', 'wb') as f:
    pickle.dump(mis_datos, f, pickle.HIGHEST_PROTOCOL)

with open('mi_info.p', 'rb') as f:
    mis_datos_recuperados = pickle.load(f)

pass