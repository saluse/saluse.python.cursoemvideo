preco = 0
totmil = 0
soma = 0
cont = 0
menor = 0
print('{:=^40}'.format(' Lojas Barateira '))
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma = soma + preco
    if preco > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if resp == 'S':
            print('Digite mais produtos: ')
    if resp == 'N':
        break
print('O totas das suas compras é R$ {:.2f}'.format(soma))
print('Na lista existem {} produtos que custam mais de R$1.000,00'.format(totmil))
print('O produto de menor preço custa: R${}'.format(menor))
print('{:=^40}'.format(' FIM DAS COMPRAS '))
