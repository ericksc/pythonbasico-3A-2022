import pandas as pd
import re
with open('sofia.txt') as f:
    data = f.readlines()


pattern = r'\d{1}(\d{1})(\d{12})(\w{0,20})\s+\d{1}(\d{8})([\w\s]+)'
sumario = []
for p in data:

    m = re.search(pattern, p).groups()
    sumario.append(m)

print(sumario[:1])
df = pd.DataFrame(sumario, columns=['Tipo', 'Cita', 'Cedula', 'Fecha', 'Nombre'])
print(df.head())
