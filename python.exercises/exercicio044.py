print('================ LOJAS KARLA =================')
preco = float(input('Preço total das Compras: R$'))
print('''Condições de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Sua escolha de pagamento: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} sairá por R${} com 10% de desconto'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de R${:.2f} sairá por R${:.2f} com 5% de desconto'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra de R${:.2f} dividida em 2x sem juros de R${:.2f}'.format(preco, parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    vezes = int(input('Em quantas parcelas você quer dividir? '))
    print('Sua compra de R${:.2f} divida em {}x sairá por R${:.2f}'.format(preco, vezes, (total / vezes)))
else:
    total = preco
    print('Opção invalida')
print('Sua compra de R${:.2f} será de R${:.2f} no final'.format(preco, total))

