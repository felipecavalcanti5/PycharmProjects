#Faça um programa que leia um número 
#qualquer e mostre o seu fatorial.


#minha tentativa:
'''
n = int(input('Digite um número: '))

while n != 0:
    print(n * (n-1)) * n
'''

#Solução do Guanabara: 
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))