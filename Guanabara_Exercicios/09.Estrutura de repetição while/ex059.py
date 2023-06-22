#Crie um programa que leia dois valores e 
#mostre um menu na tela:

#[1]somar
#[2] multiplicar
#[3] maior
#[4]novos números
#[5]sair do programa

#Seu programa deverá realizar a operação 
#solicitada em cada caso


#Minha tentativa:
'''
va1 = int(input('Digite um valor: '))
va2 = int(input('Digite outro valor: '))

n = 0 #esqueci de definir 'n', por isso o programa não rodava.
while n != 5:
    n = int(input('Qual das seguintes operações você quer fazer? 
    [1] somar 
    [2] multiplicar 
    [3] maior 
    [4] novos números 
    [5] sair do programa: ')) #Aspas triplas dentro dos parênteses possibilitam a quebra de linha de modo a deixaar o terminal igual ao código.
    if n == 1:
        print("A soma de {} e {} é {}".format(va1, va2, (va1 + va2)))
    if n == 2:
        print("A multiplicação entre {} e {} é igual a {}".format(va1, va2, (va1 * va2)))
    if n == 3:
        if va1 > va2:
            print("{} é maior que {}".format(va1, va2))
        else:
            print("{} é maior que {}".format(va2, va1))
    if n == 4:
print("Você saiu do programa")
'''

#Solução de Guanabara:

from time import sleep
n1 = int(input('Prineiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print(' O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep (2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim do programa! Volte sempre!')
