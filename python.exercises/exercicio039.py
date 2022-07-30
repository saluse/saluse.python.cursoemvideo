from datetime import date
nome = str(input('Digite seu nome: '))
n1 = nome.split()
print('Óla {}! Por favor, digite abaixo a sua idade.'.format(n1[0]))
idade = int(input('Qual a sua idade? '))
ano = date.today().year - idade
print('Você nasceu no ano de: {}'.format(ano))
if idade == 18:
    print('Você deve se apresentar ao serviço militar IMEDIATAMENTE.')
elif idade < 18:
    id1 = 18 - idade
    print('Você ainda irá se apresentar, Atenção você deve comparecer em {} anos.'.format(id1))
    print('Seu alistamento será em {}'.format(ano + 18))
elif idade > 18:
    id2 = idade - 18
    print('Seu tempo de apresentação ao serviço militar já passou, você deveria ter se apresentado hà {} anos.'.format(id2))
    print('O ano do seu alistamento foi em {}'.format(ano + 18))
