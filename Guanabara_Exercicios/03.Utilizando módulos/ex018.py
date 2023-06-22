# Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

#Minha tentativa:
"""import math

a = float(input("Digite o valor de um ângulo qualquer: "))
s = math.asin(a)
c = math.acos(a)
t = math.atan(a)

print("o valor do seno para o ângulo {:.2} é de {:.2}".format(a, s))
print("o valor do cosseno para o ângulo {:.2} é de {:.2}".format(a, c))
print("o valor do tangente para o ângulo {:.2} é de {:.2}".format(a, t))"""

#Solução de Guanabara:
import math

ângulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))

print("O ângulo de {:.2f} tem o SENO de {:.2f}".format(ângulo, seno))
print("O ângulo de {:.2f} tem o COSSENO de {:.2f}".format(ângulo, cosseno))
print("O ângulo de {:.2f} tem a TANGENTE de {:.2f}".format(ângulo, tangente))