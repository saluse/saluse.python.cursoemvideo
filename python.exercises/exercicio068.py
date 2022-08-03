from random import randint
v = 0
while True:
    jogador = int(input('Escolha um número: '))
    computador = randint(0, 10)
    resultado = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
    if tipo == 'P':
        if resultado % 2 == 0:
            print('O jogador jogou {} e o computador jogou {}: {} é PAR - JOGADOR GANHOU'.format(jogador, computador, resultado))
            v += 1
        else:
            print('VOCÊ PERDEU, GAME OVER')
            break
    elif tipo == 'I':
        if resultado % 2 == 1:
            print('O Jogador jogou {} e o computador jogou {}: {} é IMPAR - JOGADOR GANHOU'.format(computador, jogador, resultado))
            v += 1
        else:
            print('VOCÊ PERDEU, GAME OVER')
            break
    print('Vamos jogar novamente... ')
print('Voce venceu {} vezes'.format(v))
