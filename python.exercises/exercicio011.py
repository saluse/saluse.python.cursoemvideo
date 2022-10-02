print('CALCULO PARA PINTURA')
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
w = l * a
print('Sua parede tem a dimensão de {}X{} e sua área é de {:.3f}m²'.format(l, a, w))
t = w / 2
print('Para pintar sua parede, você precisará de {}L de tinta'.format(t))



