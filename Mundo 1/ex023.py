numero = int(input('digite um numero: '))
number = str(numero)
if 0 <= numero <= 9999:
    unidade: print('unidade:{}'.format(number[3]))
    dezena: print('dezenas:{}'.format(number[2]))
    centena: print('centenas:{}'.format(number[1]))
    milhar: print('milhares:{}'.format(number[0]))
else:
    print('Número inválido, tente novamente')
    exit()
