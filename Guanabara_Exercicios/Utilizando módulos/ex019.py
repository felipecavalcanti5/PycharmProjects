# Um professor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo o 
# nome deles e escrevendo o nome do escolhido.

#Minha tentativa:
"""import random

aluno1 = "Ana"
aluno2 = "Pedro"
aluno3 = "João" 
aluno4 = "Maria"

aluno = (aluno1, aluno2,aluno3, aluno4)
for n in aluno:
    print("O aluno escolhido foi {}.".format(random(aluno)))"""

#Solução Guanabara:
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O(a) aluno(a) escolhido(a) foi {}'.format(escolhido))
