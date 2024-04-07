#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

num1 = int(input('Digite um numero: '))
num2= int(input('Digite outro numero: '))

if num1 == num2:
    print("Digite numeros diferentes entre si")
elif num1 > num2:
    numM = num1
    numm = num2
else:
    numM = num2
    numm = num1
    
print("Os numeros em ordem crescente ficam: {}, {}" .format(numM, numm))