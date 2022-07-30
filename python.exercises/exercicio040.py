nome = str(input('Nome do aluno: '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua media foi: {:.2f}. Você foi REPROVADO'.format(media))
elif media >= 7.0:
    print('Sua média foi: {:.2f}. Você foi APROVADO'.format(media))
else:
    print('Sua média foi: {:.2f}. Você está em RECUPERÇÃO'.format(media))



