n_conta = int(input("Digite o numero de conta: "))
nome = (input("Digite o seu nome: "))
saldo = float(input("Digite o saldo: "))

conta = (n_conta,nome,saldo)

for item in conta:
 print(item)

print("O nome do usuário é",conta[1])

print("Seu saldo é",conta[2])
