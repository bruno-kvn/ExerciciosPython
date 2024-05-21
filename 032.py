from datetime import date

ano = int(input('\nDigite um ano para saber se ele \033[1;32mÉ BISSEXTO\033[m, coloque \033[1;36m"0"\033[m para '
                'analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[1;32mÉ BISSEXTO.\033[m'.format(ano))
else:
    print('O ano {} \033[1;31mNÃO É BISSEXTO.\033[m'.format(ano))
