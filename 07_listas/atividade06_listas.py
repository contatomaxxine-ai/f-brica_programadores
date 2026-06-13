#autor: Karina Sousa
#projeto: listas em python

#          0          1          2        3          4           5
nomes = ['Pelé', 'Maradona', 'Messi', 'Ronaldo', 'Neymar', 'Bobadilla']
print(nomes)

#adicionando um nome na lista
#para retirar as aspas e os colchetes,use *
nomes.append('Pedro')
print(*nomes)

#adicionando um nome em uma posição específica

nomes.insert(4,'Neymar')
print(*nomes)

#modificar uma pessoa da lista
nomes [5] = 'MBAPPE'
print(*nomes)

#removendo nome da lista
del nomes [2]
print(*nomes)

#removendo um nome por texto
#buscar o nome e apagar o primeiro que aparecer
nomes.remove('Maradona')
print(*nomes)

#usando o pop para mostrar o nome removido
#  0      1      2      3
# Pelé Ronaldo Neymar MBAPPE
removido = nomes.pop(1)
print(f'Após o pop foi removido o nome: {removido}',nomes)

#limpar a lista
nomes.clear ()
print(f'Após o clear a lista é: {nomes}')
