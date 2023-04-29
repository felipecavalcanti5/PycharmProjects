#Desenvolva um programa que leia o primeiro termo e a razão
#de uma PA. No final, mostre os 10 primeiros
#termos desssa progressão.

# Minha solução:
'''
a1 = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão da PA: "))
n = 11
an = a1 +(n-1)*r


for c in range(a1, an, r):
    print(c)
'''
# Solução de Guanabara:

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print("{}".format(c), end='-> ')
print('ACABOU')
