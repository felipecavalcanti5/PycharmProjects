distancia = float(input("Diga a distância da viagem em km. "))

if distancia <= 200:
    preco = distancia* 0.50
    print("Uma viagem cuja distância seja de {} km custará R$ {}".format(distancia, preco))

elif distancia > 200:
    preco = distancia* 0.45
    print("Uma viagem cuja distância seja de {} km custará R$ {}".format(distancia, preco))
