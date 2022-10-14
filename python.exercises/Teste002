res = 'S'
media = 0
soma = 0
quant = 0
while res in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('Você digitou {} números e a média dos números digitado é {}'.format(quant, media))
print('O maior número é o {} e o menor é o {}'.format(maior, menor))
print('Fim')
