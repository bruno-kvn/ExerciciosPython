dist = int(input('\nQual é a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de \033[1;33m{:,}Km.\033[m'.format(dist))

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('E o preço da sua passagem será de \033[1;33mR${:,.2f}\033[m'.format(preco))
