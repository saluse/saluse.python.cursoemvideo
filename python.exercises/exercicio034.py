sal = float(input('Qual o salário do funcionário? '))
if sal <= 1250:
    print('O salario do funcionário passará a ser de {:.2f}'.format((sal * 15) / 100 + sal))
else:
    print('O salario do funcionário passará a ser de {:.2f}'.format((sal * 10) / 100 + sal))

#Solução do professor:
salario = float(input('qual o salario do funcionário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ {:.2f} passará a ganhar R$ {:.2f}'.format(salario, novo))
