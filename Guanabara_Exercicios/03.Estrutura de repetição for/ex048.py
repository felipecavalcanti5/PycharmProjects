#Faça um programa que calcule a soma entre 
#todos os números ímpares que são múltiplos
#de três e que se encontram no intervalo de 
#1 até 500

soma = 0
cont = 0
for c in range(1, 501, 2): # O intervalo tem que partir do 1 e ir até o menos 1 e de dois em dois porque eu quero apenas os ímpares.
    if c % 3 == 0:# Quero números cuja divisão por 3 apresentem como resto, 0.
        soma += c # Dessa forma, a soma vai acrecendo ao seu resultado os números que aparecem quando respeitada a condição.
        cont += 1 # O contador é útil para armazenar a quantidade de voltas de um laço de repetição.
print("a soma de todos os {} números múltiplos de 3 no intervalo entre 1 e 500 é {}".format(cont, soma))