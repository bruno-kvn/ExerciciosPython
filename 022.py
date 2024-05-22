from time import sleep

nome = str(input('\nDigite seu nome completo: ')).title().strip()
print('\033[1;32mAnalisando seu nome...\033[m\n')
sleep(2)

print('\033[1;33m Seu nome em maiúsculas é {}. \033[m'.format(nome.upper()))
print('\033[1;34m Seu nome em minúsculas é {}. \033[m'.format(nome.lower()))
print('\033[1;35m Seu nome tem ao todo {} letras. \033[m'.format(len(nome) - nome.count(' ')))
print('\033[1;36m Seu primeiro nome é {}, e ele tem {} letras.\033[m'.format(nome.split()[0], len(nome.split()[0])))
