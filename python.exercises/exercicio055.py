maior = 0
menor = 0
for p in range(1, 3):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kgs'.format(maior))
print('O menor peso foi de {}Kgs'.format(menor))
