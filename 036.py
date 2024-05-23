print('\033[1m-\033[m' * 50)
casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos ele vai pagar? '))
parcela = casa / (anos * 12)
print('\033[1m-\033[m' * 50)

print('\033[1;34mValor da casa:              R${:,.2f}'.format(casa))
print('Salário do comprador:       R${:,.2f}'.format(salario))
print('Valor da parcela:           R${:,.2f}'.format(parcela))
print('Quantidade de parcelas:     {}'.format(anos * 12))
print('Anos até quitar a casa:     {}\033[m'.format(anos))
print('\033[1m-\033[m' * 50)

if parcela > salario * 0.30:
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')
else:
    print('\033[1;32mEMPRÉSTIMO APROVADO!\033[m')
