#autor: Karina Sousa
#projeto: Desvio Condicional

#criação das variáveis
nome = input('digite seu nome: ')
peso = float (input('digite seu peso:'))
altura = float (input('digite sua altura:'))
imc = peso/(altura*altura)
if imc <= 18.5:
    print('magro')
else:
    print('peso normal')