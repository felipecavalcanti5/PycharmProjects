# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input("Diga a largura da parede em metros: "))
h = float(input("Diga a altura da parede em metros: "))

área = l * h

print(f"Sua parede tem {área}m². Serão necessários {(área) / 2} litros de tinta para pintar a parede por completo")
