# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

KmP = float(input("Quantos km rodou? "))
DR = int(input("Por quantos dias ele foi alugado? "))
VT = (KmP*0.15)+(DR*60)

print("Considerando que rodou {}km durante {} dias, o preço total a pagar é de R${:.2f}".format(KmP, DR, VT))