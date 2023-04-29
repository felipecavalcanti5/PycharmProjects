# Crie um programa que leia o ano de 
# nascimento de sete pessoas. No final, 
# mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores


# Minha solução:
contMenor = 0
contMaior = 0

for c in range(1, 8):
    n = int(input("Digite o ano de seu nascimento: "))
    if (2023 - n) < 18:
        # print('Você é menor de idade')
        contMenor += 1
    else:
        # print('Você já é maior de idade')
        contMaior += 1
    
print("{} pessoas ainda não atingiram a maioridade e {} pessoas já são maiores de idade.".format(contMenor, contMaior))
 

# Solução do Guanabara:
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo, tivemos {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))

