cont = 0
num = 0
soma = 0
while True:
    num = int(input('Digite um número: [digite 999 para parar]: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print('Você digitou {} números é a soma deles é {} '.format(cont, soma))
