#Refaça o DESAFIO 051

#(Desenvolva um programa 
#que leia o primeiro termo e a razão
#de uma PA. No final, mostre os 10 primeiros
#termos desssa progressão.),

# lendo o primeiro 
#termo e a razão de uma PA, mostrando o 10 
#primeiros termos da progressão usando a 
#estrutura while.

# Minha solução com for:
'''a1 = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão da PA: "))
n = 11
an = a1 +(n-1)*r


for c in range(a1, an, r):
    print(c)

# Minha tentativa de solução com while:
a1 = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão da PA: "))
n = 11
an = a1 +(n-1)*r

while n < 11:
    print(n)'''

# Solução do Guanabara:
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} = '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')