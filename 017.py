from math import hypot

co = float(input('\nComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hp = hypot(co, ca)

print('A hipotenusa mede {:.2f}'.format(hp))
