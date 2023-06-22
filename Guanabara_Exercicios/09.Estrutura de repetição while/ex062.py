#Melhore o DESAFIO 061, perguntando para o 
#usuário se ele quer mostrar mais alguns 
#termos. O programa encerra quando ele 
#disser que quer mostrar 0 termos.

#Minha tentativa:
''' Tem nada a ver
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} = '.format(termo), end='')
    termo += razão
    cont += 1
pergunta = srt(input("você quer mostrar mais algum termo?[S/N]: "))
if pergunta == 'Ss':
    print('Gerador de PA')
    print('-=' * 10)
    primeiro = int(input('Primeiro termo: '))
    razão = int(input('Razão da PA: '))
else:
    print("Cabou")

print('FIM')
'''

'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} = '.format(termo), end='')
    n = int(input("quantos termos a mais você quer mostrar?: "))
    termo += razão
    cont += n

print('FIM')
'''

#Guanabara:
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} = '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quanros termos você quer mostrar a mais?: '))
print("Progressão finalizada com {} termos mostrados.".format(total))
