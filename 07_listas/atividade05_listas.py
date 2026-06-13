#autor: Karina Sousa
#projeto: listas em python

campeoes = ['Brasil','Alemanha','Itália','Argentina', 'França', 'Uruguai', 'Inglaterra', 'Espanha']

penta = ['Brasil']
tetra = ['Brasil', 'Alemanha','Itália']
tri = ['Brasil', 'Alemanha', 'itália', 'Argentina']
bi = ['Brasil','Alemanha','Itália','Argentina','França','Uruguai']
campeao = ['Brasil','Alemanha','Itália','Argentina', 'França', 'Uruguai', 'Inglaterra', 'Espanha']

print(f'São PENTA: {campeoes[0]}')
print(f'São TETRA: {campeoes[0]}, {campeoes[1]}, {campeoes[2]}')
print(f'São TRI: {campeoes[0]}, {campeoes[1]}, {campeoes[2]}, {campeoes[3]}')
print(f'São BI: {campeoes[0]}, {campeoes[1]}, {campeoes[2]}, {campeoes[3]}, {campeoes[4]} ,{campeoes[5]}')
print(f'São CAMPEOES: {campeoes[0]}, {campeoes[1]}, {campeoes[2]}, {campeoes[3]}, {campeoes[4]} ,{campeoes[5]}, {campeoes[6]},{campeoes[7]}')

print(f'São PENTA: {'Brasil'[0]}')
print(f'São TETRA: {'Brasil'[0]}, {'Alemanha'[1]}, {'Itália'[2]}')
print(f'São TRI: {'Brasil'[0]}, {'Alemanha'[1]}, {'Itália'[2]}, {'Argentina'[3]}')
print(f'São BI: {'Brasil'[0]}, {'Alemanha'[1]}, {'Itália'[2]}, {'Argentina'[3]}, {'França'[4]} ,{'Uruguai'[5]}')
print(f'São UNI: {'Brasil'[0]}, {'Alemanha'[1]}, {'Itália'[2]}, {'Argentina'[3]}, {'França'[4]} ,{'Uruguai'[5]}, {'Inglaterra'[6]}, {'Espanha'[7]}')