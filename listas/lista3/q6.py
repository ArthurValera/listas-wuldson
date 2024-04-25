#a) Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

convidados = ["Michael Jordan", "Kendrick Lamar", "Kevin Durant", "Megan Fox", "Angelina Jolie"]

#b) Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
#personalizado.

for convi in convidados:
    print(f"Olá {convi}, venho por essa mensagem te convidar ao meu jantar")
    
#c) Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
#convites. Imprima o nome das pessoas que não poderão comparecer.

npode = "Kevin Durant"
print(f"{npode} não conseguirá comparecer")

#d) Modifique sua lista, substitua os desistentes por novos convidados.
convidados.remove(npode)
convi_novo = ["ScHoolboy Q"]
convidados.extend(convi_novo)

#e) Exiba um novo convite para cada pessoa que continua presente em sua lista.

print("Novos convites")

for convi in convidados:
    print(f"Olá {convi}, conto com sua presença no meu jantar no dia 05/05/2024 às 20:00")