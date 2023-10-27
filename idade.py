# 1) Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
print('  ***** Digite apenas números inteiros *****')
dias = int(input('Digite o número de dias para o cálculo da idade: '))
anos = (dias // 365)
meses = (dias % 365 // 30)
totalDias = (dias % 365 % 30)
print('***************************************')
print(f'Total de anos = {anos}\nTotal de meses = {meses}\nTotal de dias = {totalDias}')
print('***************************************')