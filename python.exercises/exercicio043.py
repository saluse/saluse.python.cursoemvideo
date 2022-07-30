print('Responda as questões abaixo e calcule o seu IMC')
nome = str(input('Digite o seu nome: '))
peso = float(input('Digite o seu peso (em Kgs): '))
altura = float(input('Digite sua altura (em M): '))
imc = peso / (altura ** 2)
print('IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('IMC Calculado: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('IMC calculado: PESO IDEAL')
elif 25.1 <= imc < 30:
    print('IMC calculado: SOBREPESO')
elif 30.1 <= imc < 40:
    print('IMC calculado: OBESIDADE')
elif imc >= 40:
    print('IMC calculado: OBESIDADE MORBIDA')

