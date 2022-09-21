salario = int(input('Qual o seu salário? '))
novo = salario * (15/100) + salario
if salario <= 1250:
    novo = salario * (15 / 100) + salario
    print('Seu salário, R${:.2f} recebeu 15% de aumento, valendo {:.2f}.'.format(salario, novo))
elif salario < 0:
    print('Você não tem salário para receber')
else:
    novo = salario * (10 / 100) + salario
    print('Seu salário, R${:.2f} recebou 10% de aumento, valendo {:.2f}'.format(salario, novo))
