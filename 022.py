nome = str(input('\nDigite seu nome completo: ')).title().strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {}, e ele tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))
