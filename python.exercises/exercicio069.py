pessoas = 0
homem = 0
mulher20 = 0
continuar = ' '
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade <= 18:
        pessoas += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('Ao total foram {} pessoas com menos de 18 anos'.format(pessoas))
print('Foram cadastrados {} homens'.format(homem))
print('Ao todo foram {} mulheres com menos de 20 anos'.format(mulher20))
