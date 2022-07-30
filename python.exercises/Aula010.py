nome = str(input('Qual é o seu nome? '))
if nome == 'Weverton':
    print('\033[4;36;40mBem vindo, Senhor!')
else:
    print('Que nome normal!')
print('Tenha um bom dia {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {}'.format(m))
if m >= 6.0:
    print('Você está na média! PARABÉNS!')
else:
    print('Você ficou abaixo da média, ESTUDE MAIS!')
carro = int(input('Que ano é o seu carro? '))
if carro >= 2010:
    print('Carro novo')
else:
    print('Carro velho')
