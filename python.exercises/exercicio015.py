print('Pagamento de diária de carro e KMs rodados')
d = int(input('Quantos dias alugados? '))
k = float(input('Quantos KMs rodados? '))
pd = d * 60
pk = k * 0.15
print('O preço a pagar é de: R${}'.format(pd + pk))


