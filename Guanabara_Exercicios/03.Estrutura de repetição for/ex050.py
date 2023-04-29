#Desenvolva um programa que leia seis números inteiros
#e mostre a soma apenas daqueles que forem
#pares. Se o valor digitado for ímpar, desconsidere-o


# Minha solução:
# OBS.: Não atentei para o 'leia'; era para o usuário digitar os valores no terminal.
cont = 0
soma = 0
for c in range(1, 7):
    if c % 2 == 0:
        soma +=c
        cont +=1
print("A soma dos {} números pares é igual a {}".format(cont, soma))

# Solução do Guanabara:
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))