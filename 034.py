salario = float(input('\nQual é o salário do funcionário? R$'))

if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print('Quem ganhava \033[1;33mR${:,.2f}\033[m passa a ganhar \033[1;32mR${:,.2f}\033[m'.format(salario, novo))
