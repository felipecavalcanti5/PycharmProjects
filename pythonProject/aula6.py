conjunto = {1, 2, 3, 4, 5}#OBS: CONJUNTO = {}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) #junta a porra toda
print('união: {}'.format(conjunto_uniao)) #.'format' serve para colocar aquilo que se formata dentro das chaves
conjunto_interseccao = conjunto.intersection(conjunto2) #somente o que tem nos dois
print('interseccao:{}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('diferença entre 1 e 2:{}'.format(conjunto_diferenca1))
print('diferenca entre 2 e 1:{}'.format(conjunto_diferenca2))
#OBS: a ordem na diferença importa!
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferença simétrica:{}'.format(conjunto_diff_simetrica)) #Diferença simétrica é tudo o que NÃO TEM um no outro
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)#issubset = está contido em
print('A é um subconjunto de B:{}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A:{}'.format(conjunto_superset))
# conjunto.discard(2)
# conjunto.add(5)
# print(conjunto)
# print(type(conjunto))
Lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(Lista) #ao converter 'lista' para 'conjunto', elimina-se a aduplicidade
print(conjunto_animais)
print('animais:{}'.format(conjunto_animais))
lista_animais = list(conjunto_animais)
print(lista_animais)