#Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
#menor que 10. O programa deve escrever a mensagem correspondente (maior ou
#menor) e informar o valor digitado pelo usuário.

num = float(input('Digite um numero: '))

if num < 10:
    print("o numero %s é menor que 10" % num)
elif num > 10:
    print("o numero %s é maior que 10" % num)
else:
    print("o numero %s é igual que 10" % num)