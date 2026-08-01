#autor: Karina Sousa
#Projeto: trabalhando com arquivos

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')

arquivo = open('agenda.txt', 'a')
arquivo.write(nome + '|' + email + '\n' + telefone )
arquivo.close()