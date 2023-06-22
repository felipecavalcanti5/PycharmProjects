# Faça um programa que leia o comprimento do cateto oposta 
# e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.

#Minha solução:
c_op = float(input("O valor do cateto oposta é de: "))
c_ad = float(input("O valor do cateto adjacente é de: "))
hipotenusa = (c_op**2 + c_ad**2)**(1/2)

print(hipotenusa)

#Solução de Guanabara:
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

