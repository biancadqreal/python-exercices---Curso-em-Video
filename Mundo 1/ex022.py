nome = str(input('Digite seu nome completo: '))

pn_nome = nome[:nome.find(' ')]
pn_letras = nome.find(' ')

print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome, {}, tem {} letras.'.format(pn_nome, pn_letras))


