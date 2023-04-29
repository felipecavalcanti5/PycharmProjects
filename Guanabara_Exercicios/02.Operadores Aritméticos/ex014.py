#Informe a temperatura em graus celsius e depois converta-a para farenheit

c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5)+32
print('A temperatura de {0}ºC corresponde a {1}ºF!'.format(c, f))