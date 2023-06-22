#Crie um programa que leia o nome de uma cidade e diga se ela começa ou 
# não com o nome "SANTO"

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

'''
if cidade[:5] == 'SANTO':
    print('O nome da cidade começa com SANTO.')
else:
    print('Não começa com SANTO')
'''
