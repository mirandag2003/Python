dados = {
    "nome":"",
    "idade":"",
    "cidade":"",
    "telefone":"" 
}

dados["nome"] = input("Digite o seu nome:")
dados["idade"] = int(input("Digite a sua idade:"))
dados["cidade"] = input("Digite a sua cidade:")
dados["telefone"] = int(input("Digite o seu telefone:"))

for chave,valor in dados.items():
    print(f"{chave}: {valor}")