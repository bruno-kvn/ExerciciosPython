salario = float(input('\nQual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)

print('Um funcionário que ganha \033[1;33mR${:,.2f}\033[m, com aumento de \033[1;36m15%\033[m, passa a receber '
      '\033[1;32mR${:,.2f}\033[m'.format(salario, aumento))
