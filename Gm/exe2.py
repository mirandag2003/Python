estoque = []

estoque.append(int(input("Quantidade do primeiro produto: ")))
estoque.append(int(input("Quantidade de segundo produto: ")))
estoque.append(int(input("Quantidade de terceiro produto: ")))
estoque.append(int(input("Quantidade de quarto produto: ")))

for item in estoque:
    print(item)
soma = sum(estoque)
print("O primeiro produto tem o estoque de", estoque[0])
print("O primeiro produto tem o estoque de", estoque[3])
print("O quantidade total do estoque é",soma)
