a = int(input('Entre com o múnero'))

div = 0
for x in range (1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print('número {} é primo'. format(a))
else:
    print('número {} não é primo'. format(a))

# a = int(input('Entre com o múnero'))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div = div + 1
#
# if div == 2:
#     print('número {} é primo'. format(a))
# else:
#     print('número {} não é primo'. format(a))
