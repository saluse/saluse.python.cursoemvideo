print('Responda as perguntas abaixo para simular o seu emprestimo para compra de imóvel.')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual a sua renda mensal? R$'))
meses = int(input('Em qual prazo deseja pagar? '))
parcela = salario - (salario / 100 * 70)
valor = casa / meses
if valor <= parcela:
    print('Seu emprestimo foi APROVADO. Você pagará R$ {:.2f} por mês'.format(valor))
else:
    print('Seu emprestimo foi NEGADO')
