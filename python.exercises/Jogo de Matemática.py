from time import sleep
print('Oi!')
sleep(1)
print('Vamos exercitar a matemática?')
sleep(1)
n = int(input('Digite um número: '))
print('Qual o dobro, o triplo e a raiz quadrada do número informado')
sleep(3)
print('Não se preocupe, vou te ajudar')
sleep(2)
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {}, o  triplo de {} é {}, a raiz quadrada é {:.2f}'.format(n, d, n, t, r))
pergunta = input('Quer continuar? ')
if pergunta == "sim":
    while pergunta == "sim":
        n = int(input('Digite um número: '))
        print('Qual o dobro, o triplo e a raiz quadrada do número informado')
        sleep(3)
        print('Não se preocupe, vou te ajudar')
        sleep(2)
        d = n * 2
        t = n * 3
        r = n ** (1/2)
        print('O dobro de {} é {}, o  triplo de {} é {}, a raiz quadrada é {:.2f}'.format(n, d, n, t, r))
        pergunta = input('Quer continuar? ')
        if pergunta == "não":
            break
    print('Fim')
else:
    print('Fim')
