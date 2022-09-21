a = int(input('Digite um número: '))
b = int(input('Digite outro número:'))
c = int(input('Digite o último número: '))
# Analisando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Analisando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
