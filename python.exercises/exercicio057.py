
print('======== DADOS ========')
nome = str(input('Digite seu nome: '))
sexo = str(input('Sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('Valor incorreto, tente novamente. Digite seu sexo [M/F]: ')).upper()[0].strip()
if sexo == 'F':
    print('Seu gênero é Feminino')
if sexo == 'M':
    print('Seu gênero é Masculino')
