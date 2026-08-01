#autor: Karina Sousa
#projeto: conversor de temperatura


try:
   celsius = float(input('digite a temperatura:'))
   fahrenheit = (celsius * (9/5)) + 32
   print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
except:
    print('Somente permitido números.')
