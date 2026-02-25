login = int(input("Digite sua senha: "))
senha = 1234
x = 3

while login != senha and x > 0:
    x -= 1
    if x > 0:
        login = int(input("Senha incorreta! Digite novamente sua senha: "))

if login == senha:
    print("Acesso Liberado")
else:
    print("Conta bloqueada")