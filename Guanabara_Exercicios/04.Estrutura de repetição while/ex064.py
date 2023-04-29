#Crie um programa que leia vários números 
#inteiros pelo teclado. O programa só vai 
#parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, 
#mostre quantos números foram digitados e 
#qual foi a soma entre eles 
#(desconsiderando o flag) 


#Minha solução:
'''n = 0
c = 0
soma = 0

while n != 999:    
    n = int(input("Digite um número: "))
    c += 1
    soma += n
if n == 999:
    soma -= 999
    c -= 1
    print("Você digitou {} números e a soma total entre eles é {}".format(c, soma))
'''

#Solução do Guanabara:
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input("Digite um número [999 para parar]: "))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))