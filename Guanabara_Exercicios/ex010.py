#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input("Quantos reais você tem na carteira? R$ "))
dolar = reais/5.30
print("Você pode comprar {:.2f} dólares com {:.2f} reais.".format(dolar, reais))