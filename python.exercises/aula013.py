for c in range(50, 0, -10):
    print(c)
print('Fim')
n = int(input('Digite um número: '))
for c in range(0, n+1, 2):
    print(c)
i = int(input('Inicio: '))
f = int(input('final: '))
p = int(input('passo: '))
for c in range(i, f, p):
    print(c)
print('FIM')
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = n + s
print('O somatorio de todos os valos foi {}'.format(s))
