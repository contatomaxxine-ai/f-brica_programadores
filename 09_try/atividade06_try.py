#autor: Karina Sousa
#projeto: conversor de moeda

try:
    dolar = 5.08
    real = float(input('Digite seu valor em reais: '))
    conversao = real/dolar
    print(f'o valor é: US$ {conversao:.2f}')
except:
    print('Digite um número!')