days = int(input('Quantos dias alugados? '))
kilometer = float(input('Quantos km rodados ?'))
dias = days * 60
km = kilometer * 0.15
aluguel = dias + km
print('O total a pagar é de R${}'.format(aluguel))