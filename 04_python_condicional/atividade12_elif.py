#autor: Karina Sousa
#projeto: condição de salario

#criação das variáveis
nome = input('digite seu nome: ')
telefone = input('digite seu telefone:')
cidade = input('digite sua cidade:')
salario = float (input('digite seu salário:'))
if salario >= 1000:
    print('você possui uma boa renda')
elif salario >=700:
    print('você possui uma renda razoável')
elif salario >=500:
    print('você possui uma renda baixa')
else:
    print('você possui uma renda muito baixa')
