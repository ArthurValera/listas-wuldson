#Crie um programa em Python que imprima um convite para uma festa com o nome do usuário que for
#digitado. O nome do usuário precisará ser apresentado todo em caixa alta.

conv = input('Digite o nome do convidado:')
#.upper converte tudo para caixa alta
conv = conv.upper()

print("%s te convidamos para a festa!" % conv)
