print('\033[1m-\033[m' *35)

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('\033[1;31mA média do aluno é {:.1f}'.format(media))
    print('ele está REPROVADO!\033[m')
elif media <= 6.9:
    print('\033[1;35mA média do aluno é {:.1f}'.format(media))
    print('ele está de RECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mA média do aluno é {:.1f}'.format(media))
    print('ele está APROVADO!\033[m')

print('\033[1m-\033[m' * 35)
