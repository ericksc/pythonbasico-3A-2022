import pickle

# mis_datos = [
#     ('carlos', 100, 'heredia', '2001-01-01'),
#     ('juan', 150, 'san jose', '2001-01-01'),
#     ('maria', None, 'alajuela', '2001-01-01'),
#     ('andres', 1.5, None, '2022-06-24')
# ]

# with open('mi_info_profe.p', 'wb') as f:
#     pickle.dump(mis_datos, f, pickle.HIGHEST_PROTOCOL)

with open('mi_info_profe.p', 'rb') as f:
    mis_datos_recuperados = pickle.load(f)

pass

pass