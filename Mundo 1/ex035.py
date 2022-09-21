a = int(input('Digite o valor do comprimento da reta a: '))
b = int(input('Digite o valor do comprimento da reta b: '))
c = int(input('Digite o valor do comprimento da reta c: '))

if c + b > a and c + a > b and b + a > c:
    print('É possível a construção do triângulo')
else:
    print('Não é possível a construção do triângulo')
