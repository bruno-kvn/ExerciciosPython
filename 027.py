nome = str(input('\nDigite seu nome completo: ')).title().strip().split()

print('Seu primeiro nome é \033[1;34m{}.\033[m'.format(nome[0]))
print('Seu último nome é \033[1;35m{}.\033[m'.format(nome[len(nome)-1]))
