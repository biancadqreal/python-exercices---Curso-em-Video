from math import sin, cos, tan, radians

angulo_qualquer = float(input('Digite o valor de um ângulo qualquer: '))

angulo_sin = sin(radians(angulo_qualquer))
angulo_cos = cos(radians(angulo_qualquer))
angulo_tan = tan(radians(angulo_qualquer))

print('O seno do ângulo é {:.2f} e o cosseno do ângulo é {:.2f} e sua tangente é {:.2f}'.format(angulo_sin, angulo_cos, angulo_tan))
