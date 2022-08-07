num = int(input('Digite um número entre 0 e 10: '))
numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
if num < 0 or num > 10:
    print('Número inválido, digite outro número entre 0 e 10: ')
else:
    print('Você digitou o número {}'.format(numero[num]))



#Solução do Professor:
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    num = int(input('Digite um número de 0 a 10: '))
    if 0 <= num <= 10:
        break
    print('Tente NOvamente: ', end='')
print(f'Você digitou o número {cont[num]}')

#Soluções Alternativas
sequence = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
            'sete', 'oito',
            'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('digite um número:'))
    if num < 0 or num > 20:
        print('Tente novamente, N: [0/20]')
        continue
    if 0 <= num <= 20:
        print(f'Você digitou o número: {sequence[num]}')
        continuar = str(input('Você quer continuar?')).strip().lower()[0]
        if continuar in 'Ss':
            continue
        if continuar in 'Nn':
            print('O program foi encerrado!')
            break
#More

extensos = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze', 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um numero de 0 a 20: '))
while numero not in range(0,21):
	numero = int(input('Tente novamente.Digite um numero de 0 a 20: '))
print(f'Você digitou o numero {extensos[numero]}!')