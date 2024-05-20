frase = str(input('\nDigite uma frase: ')).lower().strip()

print('A letra "a" aparece {} vezes nesta frase.'.format(frase.count('a')))
print('A primeira letra "a" está na posição {}.'.format(frase.find('a')+1))
print('A última letra "a" está na posição {}.'.format(frase.rfind('a')+1))
