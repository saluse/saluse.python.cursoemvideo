print('REAJUSTE DE 15%')
s = float(input('Qual é o salário do funcionário? R$'))
a = s + (s * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(s, a))



