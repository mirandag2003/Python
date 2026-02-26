pessoas = []

while True:
    nome = input("Digite um nome:")
    if nome == 'sair':
       print(pessoas)
       break
    else: pessoas.append(nome)

    