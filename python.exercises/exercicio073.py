cont = 6
tab = ('Palmeiras', 'Corinthians', 'Fluminense', 'Flamengo', 'Atlético-PR', 'Internacional', 'Atlético Mineiro', 'Bragantino', 'América-MG', 'Santos')
for pos, time in enumerate(tab[:5]):
    print('O {} é o {}º colocado da tabela do Brasileirão'.format(time, pos + 1))
print('=' * 150)
for pos, time in enumerate(tab[5:]):
    print('O {} é o {}º da tabela do Brasileirão'.format(time, cont))
    cont += 1
print('=' * 150)
print('========== SEGUE ABAIXO OS TIMES DA TABELA EM ORDEM ALFABÉTICA ============')
print('=' * 150)
print(sorted(tab))
print('=' * 75)
print('O Internacional está na {}º posição'.format(tab.index('Internacional')+1))
print('=' * 150)
