from datetime import date

ano = int(input('\nQual é o ano de nascimento do jovem? '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print('\033[1;34mVocê completou ou completará {} anos de idade neste ano, portanto você'
          '\nainda deve se alistar ao serviço militar daqui há {} anos, no ano de {}.\033[m'
          .format(idade, (idade - 18) * -1, ano_atual + (idade - 18) * -1))
elif idade == 18:
    print('\033[1;34mVocê completou ou completará 18 anos de idade neste ano, portanto'
          '\nvocê deve se alistar ao serviço militar ainda este ano.\033[m')
else:
    print('\033[1;34mVocê completou ou completará {} anos de idade neste ano, o seu período'
          '\nde alistamento ao serviço militar foi há {} anos atrás, no ano de {}.\033[m'
          .format(idade, idade - 18, ano_atual - (idade - 18)))
