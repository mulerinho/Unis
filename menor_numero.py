# Faça um programa que leia 3 números inteiros e mostre o menor deles.
print('**********************')
count = 0
lista = []
while (count < 3):
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    count += 1
    
print(lista)
print(f'O menor número da lista: {min(lista)}')