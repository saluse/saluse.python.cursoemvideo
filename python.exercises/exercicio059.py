from time import sleep
n1 = int(input('Número 01: '))
n2 = int(input('Número 02: '))
opções = 0
while opções != 5:
    print('=-=-=-=-=-=-=-=-=-=' * 5)
    print('''Selecione a opção abaixo: 
    [ 1 ] - Para somar
    [ 2 ] - Para multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Para Sair do programa''')
    opções = int(input('Qual a sua opção? '))
    if opções == 1:
        soma = n1 + n2
        print('O resultado da soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opções == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}'.format(n1, n2, produto))
    elif opções == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é o {}'.format(n1, n2, maior))
    elif opções == 4:
        print('Digite novos numeros.')
        n1 = int(input('Número 01: '))
        n2 = int(input('Número 02: '))
    elif opções == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
    sleep(2)
sleep(3)
print('Fim do Programa.')
