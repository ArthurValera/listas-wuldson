#Crie um programa em Python que pergunte o nome do usuário e imprima um bom dia com o nome do
#usuário. Dica: você pode utilizar o método .format() ou uma concatenação de string, por exemplo.
msgpadrao = 'Bom dia'
nome = input('Qual seu nome? ')

print("{} {}!" .format(msgpadrao, nome))