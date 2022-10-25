lista = [12, 10, 7, 5]
# print(type(lista))
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

# lista_animal[0] = 'macaco' # [x] = macaco ; substitui a posição 'x' por macaco
# print(lista_animal)

tupla = (1, 10, 12, 14) #tupla = lista imutável
# tupla[0] = 12 # tupla torna o bagulho imutável

print(len(lista))
print(len(lista_animal))
print(len(tupla))
#'len' diz quantos elementos há num dado conjunto

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
#'tuple' converte lista em tupla

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 100
print(lista_numerica)
#'list' converte tupla em lista
#obs: deixa de ser imutável



# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)



# print(lista_animal)
# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'lobo' in lista_animal:
#     print('existe lobo em lista_animal')
# else:
#     print('não existe lobo em lista_animal')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# # lista_animal.pop(2)
# # print(lista_animal)
#
# lista_animal.remove('elefante')
# print(lista_animal)