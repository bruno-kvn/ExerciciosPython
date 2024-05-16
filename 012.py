preco = float(input('Qual é o preço do produto? R$'))
desc = preco - (preco * 5 / 100)

print('O produto que custa R${:.2f}, com desconto de 5% vai custar R${:.2f}'.format(preco, desc))
