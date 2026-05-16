#autor: Karina Sousa
#projeto: Desvio Condicional

#criação das variáveis
nome = input('digite seu nome: ')
idade = input('digite sua idade')
carteira = (input('digite se carteira de motorista ou nao: '))
if carteira == 'sim':
    print('pode dirigir')
else:
    print('nao pode dirigir')
    