'''nome = str(input('qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('seu nome é tão normal')
print('Bom dia, {}!'.format(nome)) # também pode ser escrito assim: print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2/2)
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

