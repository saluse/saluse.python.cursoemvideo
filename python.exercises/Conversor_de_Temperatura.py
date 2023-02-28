from random import shuffle

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
n5 = str(input('Quinto nome: '))
lista = [n1, n2, n3, n4, n5]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
