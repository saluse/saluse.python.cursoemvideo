num = int(input('Digite um número entre 0 e 10: '))
numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
if num < 0 or num > 10:
    print('Número inválido, digite outro número entre 0 e 10: ')
else:
    print('Você digitou o número {}'.format(numero[num]))
