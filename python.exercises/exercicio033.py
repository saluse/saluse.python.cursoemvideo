num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
maior = max(num1, num2, num3)
print('\033[4;30;41mO maior valor digitado foi: {}\033[m'.format(maior))
menor = min(num1, num2, num3)
print('\033[4;30;44mO menor valor digitado foi: {}\033[m'.format(menor))

#Solução do professor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[4;30;41mO menor valor digitado é {}\033[m'.format(menor))
print('\033[4;30;44mO maior valor digitado é {}\033[m'.format(maior))
