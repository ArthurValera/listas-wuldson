#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

num1 = int(input('Digite um numero: '))
num2= int(input('Digite outro numero: '))

if num1 == num2:
    print("Digite numeros diferentes entre si")
elif num1 > num2:
    numM = num1
else:
    numM = num2
    
print("O maior numero é %d" % numM)