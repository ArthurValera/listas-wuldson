#Faça um programa que mostre as tabuadas dos números de 1 a 10.

for num in range(1, 11):
    print(f"Tabuada do {num}:")
    # definindo os multiplicadores de 1 a 10
    for multi in range(1, 11):
        # definição do resultado da tabuada
        tab = num * multi
        print(f"{num} x {multi} = {tab}")
    print() 