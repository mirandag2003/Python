produtos = []
precos = []

produtos.append(input("Digite um produto: "))
produtos.append(input("Digite um produto: "))
produtos.append(input("Digite um produto: "))
produtos.append(input("Digite um produto: "))

precos.append(float(input("Digite o valor do produto: ")))
precos.append(float(input("Digite o valor do produto: ")))
precos.append(float(input("Digite o valor do produto: ")))
precos.append(float(input("Digite o valor do produto: ")))

for item in produtos:
    print(item)
for item in precos:
    print(item)

print("O valor do",produtos[0], "é", precos[0])
print("O valor do",produtos[3], "é", precos[3])

produtos [1] = (input("Digite um novo produto: "))

for item in produtos:
    print(item)