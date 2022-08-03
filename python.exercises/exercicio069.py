pessoas = 0
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
if idade < 18:
    print('Ao  total, tem {} pessoas com menos de 18 anos'.format(pessoas))
    pessoas += 1
print('FIM')
