valores = []
pares = []

valores.append (int(input("Digite seu numero: ")))
valores.append (int(input("Digite seu numero: ")))
valores.append (int(input("Digite seu numero: ")))
valores.append (int(input("Digite seu numero: ")))


for n in valores:
    if n %2 ==0:
        pares.append(n)

soma =sum(pares)

print("Os numeros pares são ", pares)
print("A soma dos numeros pares é: ",soma)