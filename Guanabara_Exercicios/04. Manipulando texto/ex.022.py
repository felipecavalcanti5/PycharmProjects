#Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas;

# O nome com todas minúsculas;

# Quantas letras ao todo( sem considerar espaços)

#Quantas letrar tem o primeiro nome.

'''frase = 'Curso em vídeo python'
print(frase)
print(len(frase))
print(len(frase.replace('python', 'android')))'''

nome = str(input("Diga o seu nome completo: ")).strip()

print(nome.upper())

print(nome.lower())

print(len(nome) - nome.count(' '))

print(nome.find(' '))