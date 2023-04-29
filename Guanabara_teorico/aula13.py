"""for c in range(0, 6):
    print("Oi")
print("FIM")"""

# o python desconsidera o último número, logo: range(1, 6) = 5 repetições.
# corrigi-se isso colocando o range a partir do zero (ou aumentando 1 no fim) 

"""for c in range(0, 7, 2):
    print(c)
print("FIM")"""

#i = int(input("Início: "))
#f = int(input("Fim: "))
#p = int(input("passo: "))

#for c in range(i, f+1, p):
#    print(c)

s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n
print("O somatório de todos os valores foi {}".format(s))