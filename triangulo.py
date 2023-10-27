""" 2) Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam
triângulo algum, se a é o maior)."""
def area(a,b,x):
    resposta = (b * a) / 2
    return resposta


print('***************************************')
print('Lendo valores para verificar a possível formação de um triangulo.')
print('Digite apenas valores inteiros.')
a = int(input('Digite um valor para reta "Altura": '))
b = int(input('Digite um valor para reta "Base": '))
x = int(input('Digite um valor para reta "X": '))
if(a + b > x and a + x > b and x + b > a):
    print('A montagem do triangulo é possível.')
    
    retorno = area(a,b,x)
    print(f' A área do triangulo é ==>  {retorno}')

else:
    print('A montagem do triangulo não é possível.')
    print(f' A soma de {a} + {b} é menor que a reta " X "')

# Analizando condição de existencia do triangulo.

# base * altura / 2