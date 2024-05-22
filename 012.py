preco = float(input('\nQual é o preço do produto? R$'))
desc = preco - (preco * 5 / 100)

print('Um produto que custa \033[1;33mR${:,.2f}\033[m, com desconto de \033[1;36m5%\033[m, passsa a custar '
      '\033[1;32mR${:,.2f}\033[m'.format(preco, desc))
