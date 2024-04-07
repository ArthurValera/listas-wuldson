#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
#compradas, calcule e escreva o custo total da compra.

qmaca = int(input('Quantas maçãs foram compradas? '))

if qmaca < 12:
    pmaca = 1.3    
else:
    pmaca = 1.00
    
total = qmaca * pmaca

print("O total foi de %.2f" % total)