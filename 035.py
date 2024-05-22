from time import sleep

print('\033[1;33m-=-\033[m' * 15)
print(' ' * 10, '\033[1;36mANALISADOR DE TRIÂNGULOS\033[m', ' ' * 10)
print('\033[1;33m-=-\033[m' * 15)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

print('\033[1;35mANALISANDO...\033[m')
sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[1;32mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m um triângulo!')
