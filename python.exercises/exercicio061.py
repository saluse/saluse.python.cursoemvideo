print('============ GERADOR DE PA ============')
n = int(input('Digite o primeiro número da PA: '))
r = int(input('Digite a razão da PA: '))
t = n
cont = 1
while cont <= 10:
    print('{} - '.format(t), end='')
    t = t + r
    cont = cont + 1
print('FIM')

