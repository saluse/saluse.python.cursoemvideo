diesel = float(input('Valor diesel atual: '))
kwp = float(input('Valor do Kwh/Ponta: '))
kwt = float(input('Consumo total em KW: '))
ktp = float(input('Consumo total na ponta Kwh: '))
Consumopontad = diesel * ktp
consumopontae = ktp * kwp
print('O valor do consumo em reais com o gerador operando na ponta é de R${}'.format(Consumopontad))
print('O valor do consumo em reais sem o gerador operando na ponta é de R${}'.format(consumopontae))
