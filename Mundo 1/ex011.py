largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
area = largura * altura
print('Você terá uma área de {} metros quadrados'.format(area))
tinta = area/2
print('Com {:.2f} litro(s) você poderá pintar a parede'.format(tinta))
