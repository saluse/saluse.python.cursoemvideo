import random

def exibir_tabuleiro(tabuleiro):
    # Função para exibir o tabuleiro na tela
    print(" ")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2] + " ")
    print("---|---|---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5] + " ")
    print("---|---|---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8] + " ")
    print(" ")

def jogador_escolhe_letra():
    # Função para o jogador escolher X ou O
    letra = ""
    while not (letra == "X" or letra == "O"):
        letra = input("Você quer jogar com X ou O? ").upper()

    if letra == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def jogada_jogador(tabuleiro, letra):
    # Função para o jogador fazer uma jogada
    jogada_valida = False
    while not jogada_valida:
        jogada = input("Digite a posição para jogar (1-9): ")
        if jogada.isdigit() and int(jogada) in range(1, 10):
            if tabuleiro[int(jogada)-1] == " ":
                tabuleiro[int(jogada)-1] = letra
                jogada_valida = True
            else:
                print("Essa posição já está ocupada. Tente outra.")
        else:
            print("Entrada inválida. Digite um número de 1 a 9.")

def jogada_computador(tabuleiro, letra_computador):
    # Função para o computador fazer uma jogada
    print("Vez do computador...")
    jogada_valida = False
    while not jogada_valida:
        jogada = random.randint(1, 9)
        if tabuleiro[jogada-1] == " ":
            tabuleiro[jogada-1] = letra_computador
            jogada_valida = True

'''def verificar_vencedor(tabuleiro, letra):
    # Função para verificar se alguém venceu
    return ((tabuleiro[0] == letra and tabuleiro[1] == letra and tabuleiro[2] == letra) or
            (tabuleiro[3] == letra and tabuleiro[4] == letra and tabuleiro[5] == letra) or
            (tabuleiro[6] == letra and tabuleiro[7] == letra and tabuleiro[8] == letra) or
            (tabuleiro[0] == letra and tabuleiro[3] == letra and tabuleiro[6] == letra) or
            (tabuleiro[1] == letra and tabuleiro[4] == letra and tabuleiro[7] == letra) or
            (tabuleiro[2] == letra and tabuleiro[5] == letra and tabuleiro[8] == letra) or
            (tabuleiro[0] == letra and tabuleiro[4] == letra and tabuleiro[8] == letra) or'''
