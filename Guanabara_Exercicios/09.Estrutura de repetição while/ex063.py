#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

#ex.: 0, 1, 1, 2, 3, 5, 8

#tentativa 1:


'''n = int(input('Digite um valor: '))
a1 = 0
a2 = 1
a3 = 0

while n > a2:
    
    print(n)
    a3 += a2'''

#tentativa 2:
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2 #lembrar de substituir os termos quando for necessário!
    t2 = t3
    cont += 1
print('- FIM')