usuario = {
    "nome": "",
    "senha":""
}

usuario["nome"] = input("Digite o seu nome:")
usuario["senha"] = int(input("Digite sua senha:"))

for chave,valor in usuario.items():
    print(f"{chave}: {valor}")