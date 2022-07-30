s = 0
cont = 0
for n in range(0, 500, 3):
    s = s + n
    cont += n
print('A soma de todos os {} números impares de 0 até 500 é {}'.format(cont, s))

#Solução do Professor
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
       soma += c
       cont = cont + 1
print('A soma  de todos {} valores solicitados é {}'.format(cont, soma))
