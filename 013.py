salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)

print('Um funcionário que ganha R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, aumento))
