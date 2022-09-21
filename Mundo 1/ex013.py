valor = int(input('Digite o seu salário atual: '))
aumento = valor * (15/100) + valor
print('Tendo um aumento de 15%, seu salário de {:.2f}, passará a ser {:.2f}'.format(valor, aumento))