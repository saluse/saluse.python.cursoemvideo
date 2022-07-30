nome = str(input('Digite uma frase: ')).strip().upper()
palavra = nome.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase não é um PALÍNDROMO')
