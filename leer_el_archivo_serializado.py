import pickle


with open('mi_info.p', 'rb') as f:
    mis_datos_recuperados = pickle.load(f)

print(mis_datos_recuperados)