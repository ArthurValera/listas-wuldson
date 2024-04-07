#Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado 
# (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2)/2

if media >= 6:
    print("APROVADO! com media %.2f" % media)
else:
    print("REPROVADO! com media %.2f" % media)