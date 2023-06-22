#Crie um programa que mostre na tela todos os
#números pares que estão no intervalo entre
#1 e 50.

#Minha solução:
#for c in range(2, 50, 2):
 #   print(c)

"""
for n in range(1, 51):
    print('.')
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')
"""

#Solução Guanabara final:
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')

