#Faça um programa que leia um número inteiro
#e diga se ele é ou não um número primo


#Minha tentativa de resolução:
'''
numPrimo = 

numInt = int(input("Digite um número primo: "))
if numInt == numPrimo:
    print("{} é um número primo".format(numInt))

else: print("{} não é um número primo".format(numInt))
'''


# Resolução de Guanabara:
núm = int(input("Digite um número: "))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')