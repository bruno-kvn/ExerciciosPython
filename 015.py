dias = int(input('\nQuantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)

print('O total a pagar é de \033[1;32mR${:,.2f}\033[m'.format(total))
