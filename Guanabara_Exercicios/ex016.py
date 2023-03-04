# Crie um programa que leia um número Real qualquer pelo teclado e mostre
# na tela a sua porção inteira

# ex.: Digite um número: 6.127
# o número 6.127 tem a parte inteira 6.

'''
import math

num = float(input("Digite um número real qualquer: "))
print("o numero {} tem a parte inteira {}".format(num, math.trunc(num)))'''

from math import trunc

num = float(input("Digite um número real qualquer: "))
print("o numero {} tem a parte inteira {}".format(num, trunc(num))) #formatar para tirar as casas decimais"

# OBS1.: É necessário importar a biblioteca math (para operações matemáticas) e acrescer na formatação a funcionalidade 'math.trunc',
# que serve para 'arredondar para baixo'.

# OBS2.: Pra formatar, utiliza-se chaves '{}'

# OBS3.: Quando for necessário somente uma funcionalidade de uma biblioteca, ao invés de exportá-la toda, é possível importar apenas a
# função desejada. ex.: 'from math import trunc'
