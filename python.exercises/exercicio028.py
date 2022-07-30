from random import randint
from time import sleep
computer = randint(0, 5) # Faz o computador sortear um número.
print('\033[30;45m=-=-\033[m' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('\033[30;45m===---\033[m' * 13)
jogador = int(input('Em que número em pensei? ')) # O jogador tenta adivinhar.
print('PROCESSANDO')
sleep(1)
print('\033[31;41m.........\033[m' * 10)
sleep(1)
print('\033[33;43m.........\033[m' * 10)
sleep(1)
print('\033[32;42m.........\033[m' * 10)
sleep(1)
print('\033[34;44m.........\033[m' * 10)
sleep(1)
print('\033[35;45m.........\033[m' * 10)
sleep(2)
if jogador == computer:
    print('\033[1;30;42mParabéns, você acertou.\033[m')
else:
    print('\033[1;30;41mEu ganhei, eu pensei no numero {} e não no {}\033[m'.format(computer, jogador))

