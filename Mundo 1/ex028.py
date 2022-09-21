from random import randint
from time import sleep
numero = int(input('Tenta adivinha o número que eu estou pensando: '))
ncpu = randint(0, 5)
print('Processando...')
sleep(3)
if ncpu == numero:
    print('Você acertou, parabéns! Pensei no número {}'.format(ncpu))
else:
    print('Poxa, você errou, pensei no número {}, tente novamente =D'.format(ncpu))




