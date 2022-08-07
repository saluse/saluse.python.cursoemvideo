lanche = ('Hamburguer', 'Suco', 'Refrigerante', 'Bolo', 'Pudim', 'Batata frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('{:=^50}'.format(' PAUSA '))
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')
print('{:=^50}'.format(' PAUSA '))
for pos, comida in  enumerate(lanche):
    print(f'Eu vou comer {comida}, na posição {pos}')
print('{:=^50}'.format(' PAUSA '))
print(sorted(lanche))
print('{:=^50}'.format(' PAUSA '))
print('EXEMPLO COM NÚMEROS')
a = (2, 3, 5, 8)
b = (6, 5, 3, 7, 9)
c = a + b
print(c) #retorna o resultado da junção das duas tuplas (a + b)
print(c.index(5)) #index retorna a posição do número digitado a partir do inicio.
print(c.index(5, 3)) #retorna a posição do número digitado a partir do 3 elemento.

