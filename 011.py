larg = float(input('\nLargura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {:,}m2.'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:,}l de tinta.'.format(tinta))
