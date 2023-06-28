# Escreva um programa que faça o computador "pensar" em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o 
# usuário venceu ou perdeu.

from random import randint

numPC = randint(0, 5)

num = int(input("Digite um número entre 0 e 5: "))
if num == numPC:
    print("Você venceu! O número escolhido foi {}".format(numPC))
else: 
    print("Você perdeu! O número escolhido foi {}".format(numPC))