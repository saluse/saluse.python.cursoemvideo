km = float(input('Qual a velocidade do seu carro? '))
if km > 80:
    kmu = (km - 80) * 7
    print('Você ultrapassou o limite de velocidade, você foi multado!')
    print('O valor da multa é de R${:.2f}'.format(kmu))
else: # Eu tambem posso programar uma condição simples, com apenas o *if*, basta não escrever o *else* ou colocar hastag no inicio.
    print('Cuidado com a velocidade, o limite máximo é de 80Km/H')
print('Tenha um bom dia, dirija com segurança')

# A resposta do professor
velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite de velocidade, você foi multado!')
    print('O valor da multa é de R${:.2f}'.format(multa))
#else: # Eu tambem posso programar uma condição simples, com apenas o *if*, basta não escrever o *else* ou colocar hastag no inicio.
    #print('Cuidado com a velocidade, o limite máximo é de 80Km/H')
print('Tenha um bom dia, dirija com segurança')
