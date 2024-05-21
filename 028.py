from random import randint
from time import sleep

print('\033[1;33m-=-\033[m' * 19)
print('\033[1;36mVOU ESCOLHER UM NÚMERO ENTRE 0 E 5, TENTE ADIVINHAR...\033[m')
print('\033[1;33m-=-\033[m' * 19)
numero = randint(0, 5) #RANDOMIZA UM NÚMERO ENTRE 0 E 5.
chute = int(input('Qual número eu escolhi? ')) #JOGADOR TENTA ADIVINHAR

print('\033[1;35mPROCESSANDO...\n\033[m')
sleep(2)
if chute == numero:
    print('\033[1;32mVOCÊ ACERTOU! Parabéns!\033[m')
else:
    print('\033[1;31mVOCÊ ERROU!\033[m Eu escolhi o \033[1;32mnúmero {}\033[m, e não o \033[1;31mnúmero {}!\033[m'
          .format(numero, chute))
print('\033[1;36mFIM DE JOGO!\033[m')
