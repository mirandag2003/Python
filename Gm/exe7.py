lista = []

lista.append(input("Digite o nome do primeiro produto: "))
lista.append(input("Digite o nome do segundo produto: "))
lista.append(input("Digite o nome do terceiro produto: "))
lista.append(input("Digite o nome do quarto produto: "))

p = float(input("Digite o valor do primeiro produto:"))
p1 = float(input("Digite o valor do segundo produto:"))
p2 = float(input("Digite o valor do terceiro produto:"))
p3 = float(input("Digite o valor do quarto produto:"))

tupla = (lista[0],p,lista[1],p1,lista[2],p2,lista[3],p3)

quantidade = {
    "produto" : "",
    "produto1" : "",
    "produto2" : "",
    "produto3" : ""
}

quantidade["produto"] = int(input("Digite a quantidade do primeiro produto:"))
quantidade["produto1"] = int(input("Digite a quantidadedo segundo produto:"))
quantidade["produto2"] = int(input("Digite a quantidade do terceiro produto:"))
quantidade["produto3"] = int(input("Digite a quantidade do quarto produto:"))

for item in tupla:
    print(item)

print(lista)

for chave,valor in quantidade.items():
    print(f"{chave}: {valor}")
