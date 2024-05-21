vel = int(input('\nQual é a velocidade atual do carro? '))
multa = (vel - 80) * 7

if vel > 80:
    print('\033[1;31mMULTADO!\033[m Você excedeu o limite permitido de 80Km/h.')
    print('Você deve pagar uma \033[1;31mmulta de R${:,.2f}\033[m'.format(multa))
print('\033[1;33mTenha um bom dia! Dirija com segurança!\033[m')
