nome = str(input('\nDigite seu nome completo: ')).title().strip().split()

print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
