numero = int(input('Sinalize com quantos Km/h foi avistado o carro? '))
multa = (numero - 80)*7

if(numero>80):
    print('Você foi multado em {} reais'.format(multa))
else:
    print('Você não foi multado')