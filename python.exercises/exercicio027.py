nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
ns = nome.split()
print('Seu primeiro nome é {}'.format(ns[0]))
print('Seu último nome é {}'.format(ns[len(ns)-1]))
