
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
# Verificando quem é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    meor = c
#Verificando quem é o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor número é {} e o maior número é {}".format(menor, maior))