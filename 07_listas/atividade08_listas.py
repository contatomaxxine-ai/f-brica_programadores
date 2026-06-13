#autor: Karina Sousa
#projeto: listas em python - cadastro

#          0          1          2           3       
nomes = ['Renata', 'Tamires', 'Vanessa', 'Pietra']
print(nomes)

#adicionando um nome na lista
nomes.append (input ('digite o nome que deseja cadastrar:'))
print(*nomes)

#modificar uma pessoa da lista
nomes [3] = 'Soraya'
print(*nomes)

#removendo nome da lista
del nomes [2]
print(*nomes)

