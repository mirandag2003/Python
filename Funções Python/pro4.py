saque = float(input("Digite o valor que deseja sacar: "))
saldo = 1000

while saque > saldo:
    saque = float(input("Saldo insuficiente para saque:"))
print("Saque efetuado com sucesso, saldo disponível de ", saldo - saque)