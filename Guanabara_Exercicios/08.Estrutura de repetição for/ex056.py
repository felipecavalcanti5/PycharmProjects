#Desenvolva um programa que leia o nome, 
#idade e sexo de 4 pessoas. No final do 
#programa, mostre:

#1 - A média de idade do grupo.
#2 - Qual é o nome do homem mais velho.
#3 - Quantas mulheres têm menos de 20 anos.


#Minha tentativa:
'''
mulheresAbaixodeVinte = 0
idade = 0
idadeinicial = 0
MediaIdade = idade/ 4

for p in range(1, 5):

    nome = str(input("Nome da {}ª pessoa: ".format(p)))  
    idade = int(input("Idade da {}ª pessoa: ".format(p)))  
    idade += idade
    sexo = str(input("Sexo da {}ª pessoa[M/F]: ".format(p)))

    if idade < 20:
        mulheresAbaixodeVinte +=1

print("A média das idades é {}".format(MediaIdade))
#print("{} é o homem mais velho".format())
print("{} mulheres estão abaixo de 20 anos".format(mulheresAbaixodeVinte))
'''

#Solução do Guanabara:
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo, são {} mulheres com menos de 20 anos'.format(totmulher20))


    
