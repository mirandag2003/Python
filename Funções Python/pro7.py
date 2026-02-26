while True:
    x = int(input("1 - Cadastrar | 2 - Listar | 3 - Sair:"))
    if x == 3:
        print("Programa encerrado")
        break
    elif x == 2:
        print("Bem vindo a area de Listagem")
    elif x == 1:
        print("Bem vindo a area de cadastro")

    else:print("Codigo inválido")
