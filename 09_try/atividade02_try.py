# autor: Karina Sousa
# Projeto: entendendo tratamento de exceção


try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f'a soma é {soma}')
except:
    print('Digite um número!')

    
