#Faça um programa que leia o sexo de uma pessoa, mas 
#só aceite os valores 'M' ou 'F'. Caso esteja
#errado, peça a digitação novamente até ter 
#um valor correto.


#Minha tentativa:

'''
s = str(input("Digite o seu sexo [M/F]: "))
while s != M or F:
    print(input("{} não é uma resposta válida. Por favor, digite novamente: ".format(s)))
'''

#Solução do Guanabara:

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper() [0] # .strip() remove os espaços vazios; .upper() transforma em maiúscula e [0] pega o caracter da primeira posição da string. 
while sexo not in 'MmFf': #para string, utilizar 'not in', e não o '!='.
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper() [0]
print('Sexo {} registrado com sucesso'.format(sexo))