import math

cateto_a = float(input('Digite o valor do cateto adjacente: '))
cateto_o = float(input('Digite o valor do cateto oposto: '))

print('Com o cateto adjacente {:.2f} e o cateto oposto {:.2f}, a hipotenusa é {:.2f}'.format(cateto_a, cateto_o, math.hypot(cateto_a, cateto_o)))
