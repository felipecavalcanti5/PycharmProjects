#Crie um programa que leia uma frase 
#qualquer e diga se ela é um palíndromo.
#esconsiderando os espaços


# Minha tentativa:
'''
for c in range(1, 4):
    c = str(input("Digite uma frase qualquer: "))
    if 1 == 3:
        print("É palíndromo")
    else: print("Não é palíndromo")
    '''

# Solução do Guanabara:
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #a função .split separa as palavras de uma string
junto = ''.join(palavras) # .join serve para juntar os termos de uma string
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')