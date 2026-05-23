#autor: Karina Sousa
#projeto: condição de notas

#criação das variáveis
nome = input('digite seu nome: ')
idade = input('digite sua idade:')
série = input('digite sua série:')
nota1 = float (input('digite sua primeira nota:'))
nota2 = float (input('digite sua segunda nota'))
nota3 = float (input('digite sua terceira nota'))
media = (nota1+nota2+nota3) / 3
if media >= 7:
    print('aluno aprovado')
elif media >=4:
    print('aluno de recuperação')
else:
    print('aluno está reprovado')
