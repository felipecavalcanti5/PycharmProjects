vel = float(input("Qual a velocidade do carro? "))
if vel > 80:
    multa = (vel-80) * 7
    print("{} km/h ultrapassa o limite de velocidade. Você foi multado em {} reais".format(vel, multa))
else: 
    print("Pode prosseguir.")