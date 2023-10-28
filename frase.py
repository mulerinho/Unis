# Retorne uma nova frase com cada palavra com as letras invertidas.
from ntpath import split
frase = input('Digite uma frase para ter as palavras  invertidas: ')
inverte = frase.split()
inverte.reverse()
nova = ' '.join(inverte)
print(f'A frase invertida: ==>   {nova}')
print('***********************************')
print('Misturando as palavras e as letras nas palavras.')
for i in inverte:
    print(f'{i[::-1]}')