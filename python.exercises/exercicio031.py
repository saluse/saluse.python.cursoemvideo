dis = int(input('Qual a distância da sua viagem? '))
if dis <= 200:
    print('O preço da sua passagem é de R${:.2f}'.format(dis * 0.5))
else:
    print('O preço da sua passagem é de R${:.2f}'.format(dis * 0.45))

#A resolução do professor:

distancia = int(input('Qual é a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
