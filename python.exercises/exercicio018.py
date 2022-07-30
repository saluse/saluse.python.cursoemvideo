import math
a = float(input('Digite o ângulo que você deseja: '))
print('O angulo de {} tem o SENO de {:.2f}'.format(a, math.sin(math.radians(a))))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(a, math.cos(math.radians(a))))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(a, math.tan(math.radians(a))))

from math import radians, sin, cos, tan
a1 = float(input('Digite outro ângulo: '))
seno = sin(radians(a1))
print('O angulo de {} tem o SENO de {:.2f}'.format(a1, seno))
cosseno = cos(radians(a1))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(a1, cosseno))
tangente = tan(radians(a1))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(a1, tangente))
