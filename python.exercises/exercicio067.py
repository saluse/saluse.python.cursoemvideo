n = 1
while True:
    num = int(input('Quer saber a tabuada de qual valor? '))
    print('=' * 60)
    if num < 0:
        break
    for c in range(1, 11):
        print('{} X {} = {}'.format(num, c, num * c))
        n += 1
    print('=' * 60)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')

