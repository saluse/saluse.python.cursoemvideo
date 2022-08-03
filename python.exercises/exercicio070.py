while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if resp == 'S':
            print('Digite mais preços: ')
    if resp == 'N':
        break
print('FIM')
