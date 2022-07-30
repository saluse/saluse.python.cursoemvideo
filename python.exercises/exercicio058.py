from random import randint
computador = randint(1, 3)
tentativas = 1
print('Vou pensar em um número, tente adivinhar...')
jogador = int(input('Em que número eu pensei? '))
while computador != jogador:
    jogador = int(input('Valor errado, digite outro: '))
    tentativas = tentativas + 1
if jogador == computador:
    print('Você acertou')
    print('Você tentou {}X até acertar'.format(tentativas))
