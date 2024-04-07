#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o 
#saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
#senão escrever a mensagem 'Saldo Negativo'.

conta = int(input('Digite o número de sua conta: '))
saldo = float(input('Digite o saldo em conta: R$ '))
debito = float(input('Digite o débito em conta: R$ '))
credito = float(input('Digite o crédito em conta: R$ '))

saldoatual = saldo - (debito + credito)

if saldoatual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")