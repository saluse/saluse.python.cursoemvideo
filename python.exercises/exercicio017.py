co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co ** 2) + (ca ** 2)
h1 = h ** (1/2)
print('O valor da hipotenusa é: {:.2f}'.format(h1))

import math
co1 = float(input('Comprimento do cateto oposto: '))
ca1 = float(input('Comprimento do cateto adjacente: '))
h2 = math.hypot(co1, ca1)
print('A hipotenusa vale {:.2f}'.format(h2))

