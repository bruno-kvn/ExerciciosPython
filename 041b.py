from datetime import date

ano = int(input('\nAno de nascimento do atleta: '))
idade = date.today().year - ano

frase = ('\033[1;34mO atleta completou ou completará {} anos de idade neste ano,'
         '\nportanto ele é classificado como um ATLETA {}!\033[m')

if idade <= 9:
    print(frase.format(idade, 'MIRIM'))
elif idade <= 14:
    print(frase.format(idade, 'INFANTIL'))
elif idade <= 19:
    print(frase.format(idade, 'JUNIOR'))
elif idade <= 25:
    print(frase.format(idade, 'SÊNIOR'))
else:
    print(frase.format(idade, 'MASTER'))
