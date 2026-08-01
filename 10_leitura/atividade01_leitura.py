#autor: Karina Sousa
#Projeto: trabalhando com arquivos

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')

arquivo = open('pessoa.txt', 'a')
arquivo.write(nome + '|' + email + '\n')
arquivo.close()