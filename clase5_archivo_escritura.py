
def para_escribir():
    with open(r'C:\Users\ecsa\OneDrive - GFT Technologies SE\Documents\otro_archivo.txt', 'a') as f:
        f.write('\ny me invitó a una fiesta')

para_escribir()

with open(r'C:\Users\ecsa\OneDrive - GFT Technologies SE\Documents\otro_archivo.txt', 'r') as f:
    mi_archivo = f.read()

print(mi_archivo)