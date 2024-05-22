vel = int(input('\nQual é a velocidade atual do carro? '))
multa = (vel - 80) * 7

if vel > 80:
    print('\033[1;31mMULTADO![m Você excedeu o limite permitido de 80Km/h.')
    print('Você deve pagar uma mmulta de\033[m \033[1;33m${:,.2f}\033[m'.format(multa))
print('\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')
