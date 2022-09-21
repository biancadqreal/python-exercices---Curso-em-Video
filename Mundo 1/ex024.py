nome = str(input('Digite um nome: ')).strip()
nameupper = nome.upper()
atrasespaco = nameupper.find(" ")

if nameupper == 'SANTO':
    print('A sua cidade começa com SANTO')
elif nameupper[:atrasespaco] == 'SANTO':
    print('Sua cidade começa com SANTO')
else:
    print('Sua cidade não começa com SANTO')
