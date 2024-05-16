m = float(input('Uma distância em metros: '))

print('A medida de {}m corresponde a: '.format(m))
print('{}km\n{:,.0f}cm\n{:,.0f}mm'.format(m/1000, m*100, m*1000))
