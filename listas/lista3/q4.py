#Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

num = int(input("Digite um numero: "))

print(f"Tabuada do {num}:")
# definindo os multiplicadores de 1 a 10
for multi in range(1, 11):
    # definição do resultado da tabuada
    tab = num * multi
    print(f"{num} x {multi} = {tab}")