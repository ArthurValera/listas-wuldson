#Crie um programa em Python que solicite um número do usuário, depois some este número com
# 1357, multiplique por 8, divida por 5 e eleve ao quadrado.

num = float(input('Digite seu numero: '))
operacao = ((num + 1357) * 8 / 5) ** 2

print("seu novo numero é %d" % operacao)