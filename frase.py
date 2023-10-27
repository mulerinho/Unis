# Retorne uma nova frase com cada palavra com as letras invertidas.
from ntpath import split
frase = input('Digite uma frase para ser invertida: ')
inverte = frase.split()
inverte.reverse()
print(inverte)

nova = ' '.join(inverte)
print(f'A frase invertida: ==>   {nova}')