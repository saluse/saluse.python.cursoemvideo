from time import sleep
print('Vamos Converter alguns valores distanciais')
d = float(input('Uma distância em metros: '))
k = d/1000
print('A medida de {}m corresponde a {}Km: '.format(d, k))
sleep(1)
print('A medida de {}m corresponde a {}Dm: '.format(d, d/100))
sleep(1)
print('A medida de {}m corresponde a {}cm: '.format(d, d*1000))







