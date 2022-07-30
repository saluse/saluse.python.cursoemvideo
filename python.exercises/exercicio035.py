print('Digite 3 valores de reta e veja se é possível formar um triangulo')
print('/' * 25)
a = float(input('Tamanho do primeiro lado: '))
b = float(input('Tamanho do segundo lado: '))
c = float(input('Tamanho do terceiro lado: '))
print('/' * 25)
if a < b + c and b < a + c and c < a + b:
    print('Sim, o triângulo pode ser formado')
else:
    print('Não, com esses valores não é possível formar um triângulo')
