valor = int(input('Digite o valor: '))
valor_desconto = valor*(5/100)
valor_final = valor - valor_desconto
print('Sendo o valor escolhido {}, obtivendo 5% de desconto, o valor de desconto será {:.2f} e o valor final do produto será de {:.2f}.'.format(valor, valor_desconto, valor_final))
