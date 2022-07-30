print('=' * 75)
print('10 TERMOS DE UMA PA')
print('=' * 75)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
a = n + (10 - 1) * r
for a in range(n, a + r, r):
    print(a, end='-')
print('ACABOU')

#Solução do Professor:
primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end=' - ')
print('FIM')
