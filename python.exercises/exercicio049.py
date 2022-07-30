print('Digite um número para multiplicar.')
n = int(input('digite um número: '))
print('A tabuada de {} é:'.format(n))
print('-=' * 20)
for c in range(1, 11):
    s = n * c
    print(n, 'x', c, '= {}'.format(s))
print('-=' * 20)

#Solução do Professor:
num = int(input('Digite um número para ser multiplicado: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, num * c))
