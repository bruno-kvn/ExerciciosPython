from datetime import date

ano = int(input('\nAno de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print('\033[1;34mO atleta completou ou completará {} anos de idade neste ano,'
          '\nportanto ele é classificado como um ATLETA MIRIM!\033[m'.format(idade))
elif idade <= 14:
    print('\033[1;34mO atleta completou ou completará {} anos de idade neste ano,'
          '\nportanto ele é classificado como um ATLETA INFANTIL!\033[m'.format(idade))
elif idade <= 19:
    print('\033[1;34mO atleta completou ou completará {} anos de idade neste ano,'
          '\nportanto ele é classificado como um ATLETA JUNIOR!\033[m'.format(idade))
elif idade <= 25:
    print('\033[1;34mO atleta completou ou completará {} anos de idade neste ano,'
          '\nportanto ele é classificado como um ATLETA SÊNIOR!\033[m'.format(idade))
else:
    print('\033[1;34mO atleta completou ou completará {} anos de idade neste ano,'
          '\nportanto ele é classificado como um ATLETA MASTER!\033[m'.format(idade))
