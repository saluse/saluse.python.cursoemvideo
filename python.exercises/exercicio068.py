from random import randint
jogador = int(input('Escolha um número: '))
pergunta = str(input('Par ou Impar [P/I]: ')).upper().strip()
computador = randint(1, 10)
resultado = jogador + computador
if pergunta == 'Pp' and resultado % 2 == 0:
    print('O jogador jogou {} e o computador jogou {}: {} é PAR - JOGADOR GANHOU'.format(jogador, computador, resultado))
elif pergunta == 'Ii' and resultado != 0:
    print('O computador jogou {} e o jogador jogou {}: {} é PAR - COMPUTADOR GANHOU'.format(computador, jogador, resultado))
else:
    print('EMPATE')
