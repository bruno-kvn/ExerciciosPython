real = float(input('\nQuanto dinheiro você tem na carteira? R$'))
dolar = real / 5.15

print('Considerando uma contação de R$5.15 por dólar,')
print('com \033[1;33mR${:.2f}\033[m você pode comprar \033[1;32mUS${:.2f}\033[m'.format(real, dolar))
