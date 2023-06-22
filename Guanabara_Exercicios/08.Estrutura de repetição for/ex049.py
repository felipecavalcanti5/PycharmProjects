#Refaça o desafio 009, mostrando a tabuada 
#de um número que o usuário escolher. Só que
#agora utilizado um laço for.

num = int(input("Digite um número: "))
for c in range(1, 11):
    print("{} x {} é igual a: {}".format(num, c, num*c))