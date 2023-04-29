# O mesmo professor do desafio anterior quer sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada
'''
from random import choice

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

alunos = [a1,a2,a3,a4]S
aleatorio = choise(alunos)

print("A ordem de apresentação será {}".format(aleatorio))
'''

from random import shuffle
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))

alunos = [a1, a2, a3, a4]
shuffle(alunos)
# aleatorio = random(alunos)

print("A ordem de apresentação será ")
print(alunos)
      
