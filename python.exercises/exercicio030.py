num = int(input('Digite um número: '))
if num / 2 % 1:
    print('O número {} é IMPAR'.format(num))
else:
    print('O número {} é PAR'.format(num))

# A resposta do professor foi essa abaixo.

numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))


