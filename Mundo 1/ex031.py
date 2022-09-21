numero = float(input('Digite quantos km será sua viagem: '))
menordist = 0.5 * numero
maiordist = 0.45 * numero
if numero <= 200:
    print('Você terá que pagar por {}'.format(menordist))
else:
    print('Você terá que pagar por {}'.format(maiordist))
