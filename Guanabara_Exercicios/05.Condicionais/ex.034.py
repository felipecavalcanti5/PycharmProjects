salario = float(input("Qual é o seu salário? "))

if salario > 1250.00:
    aumento = salario * 1.1
    print("Seu salário é superior a R$ 1250.00. Logo, seu aumento foi de R$ {}".format(aumento))
elif salario <= 1250.00:
    aumento = salario * 1.15
    print("Seu salário é inferior ou igual a R$ 1250.00. Logo, seu aumento foi de R$ {}".format(aumento))