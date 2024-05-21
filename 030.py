numero = int(input('\nDigite um número para saber se ele é \033[1;36mPAR\033[m ou \033[1;35mÍMPAR:\033[m '))
result = numero % 2

if result == 0:
    print('O número {} é \033[1;36mPAR.\033[m'.format(numero))
else:
    print('O número {} é \033[1;35mÍMPAR.\033[m'.format(numero))
