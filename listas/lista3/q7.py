#Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

#lista dos usuarios
usuarios = []

# Preenchimento das infos

nome = input("Digite o nome do usuário: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu email: ")

#dicionario para as infos
usuario = {
    "nome": nome,
    "idade": idade,
    "email": email
}

# add usuario na lista

usuarios.append(usuario)
print("Cadastrado com sucesso!")

#Mostrando Dados cadastrados
print("Lista de usuarios")

for usuario in usuarios:
     print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")