from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('Analisando os números digitados: ')
sleep(3)
if n1 > n2:
    print('O PRIMEIRO número {} é maior'.format(n1))
elif n2 > n1:
    print('O SEGUNDO número {} é maior'.format(n2))
else:
    print('Não existe valor maior, os dois são IGUAIS.')
