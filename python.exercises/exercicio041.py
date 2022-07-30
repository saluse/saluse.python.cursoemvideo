from datetime import date
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
ano = date.today().year - idade
if idade <= 9:
    print('De acordo com o ano que você nasceu ({}), sua categoria é Mirim'.format(ano))
elif 9 < idade <= 14:
    print('De acordo com o ano que você nasceu ({}), sua categoria é INFANTIL'.format(ano))
elif 14 < idade <= 19:
    print('De acordo com o ano que você nasceu ({}), sua vategoria é JUNIOR'.format(ano))
elif 19 < idade <= 25:
    print('De acordo com o ano que você nasceu ({}), sua categoria é SÊNIOR'.format(ano))
else:
    print('De acordo com o ano que você nasceu ({}), sua categoria é MASTER'.format(ano))
