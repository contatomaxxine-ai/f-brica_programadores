#autor: Karina Sousa
#projeto: Desvio Condicional

#criação das variáveis
nome = input('digite seu nome: ')
peso = float (input('digite seu peso:'))
altura = float (input('digite sua altura:'))
imc = peso/(altura*altura)
if imc <= 18.5:
    print('magro')
elif imc <= 24.9:
    print('peso normal')
elif imc <= 29.9:
    print('sobrepeso')
elif imc <= 39.9:
    print('obesidade')
elif imc > 39.9:
    print('obesidade grave')