print(str('Digite 3 valores de retas e veja se é possível formar um triângulo: '))
print('/\/' * 20)
a = float(input('Primeira Reta: '))
b = float(input('Segunda Reta: '))
c = float(input('Terceira Reta: '))
equi = a == b == c
esca = a != b != c != a
print('/\/' * 20)
if a < b + c and b < a + c and c < a + b:
    print('Sim, o triângulo pode ser formado.')
    if equi:
        print('Triângulo: Equilátero')
    elif esca:
        print('Triângulo: Escaleno')
    else:
        print('Triângulo: Isoceles')
else:
    print('Não, o triângulo não pode ser formado')
