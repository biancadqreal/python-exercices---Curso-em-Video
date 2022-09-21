frase = str(input('Digite sua frase: ')).strip()
namelower = frase.lower()
print('A letra a na sua frase aparece {} vezes'.format(namelower.count('a')))
print('A primeira vez que a letra a aparece na sua frase é na posição {}'.format(namelower.find('a')+1))
print('A última vez que a letra aparece na sua frase é na posição {}'.format(namelower.rfind('a')+1))

