n = int(input('Digite um número qualquer: '))
n1 = 1
for n in range(n, 0, -1):
    n1 = n1 * n

print('O fatorial é: {}'.format(n1))

from math import factorial
n = int(input('Digite um número para saber qual é o seu fatorial: '))
f = factorial(n)
print('O fatorial de {}! é {}.'.format(n, f))

n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))
