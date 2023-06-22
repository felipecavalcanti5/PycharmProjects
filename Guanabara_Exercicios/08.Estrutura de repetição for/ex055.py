#Faça um programa que leia o peso de 5 
#pessoas. No final, mostre qual foi o maior
#e o menor peso lidos.


# Minha tentativa:
menorpeso = 0
maiorpeso = 0
peso = 0

for c in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: ".format(c)))
    if c == 1:
          maiorpeso = peso
          menorpeso = peso

    elif peso > maiorpeso:
        maiorpeso = peso

    elif peso < menorpeso:
         menorpeso = peso

print("O maior peso foi {} e o menor peso, {}".format(maiorpeso, menorpeso))


# Solução do Guanabara:
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))