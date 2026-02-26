numeros = []


while True:
    n = int(input("Digite um numero:"))
    if n == 0:
        print(numeros)
        soma = sum(numeros)
        print(soma)
        break
    else:numeros.append(n)
