#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

vm = float(input("Digite um valor em metros: "))
vcm = vm*100
vmm = vm*1000

print(f"{vm} metros equivale a {vcm}cm e {vmm}mm.")