valores = []
valores.append (int(input("Digite seu numero: ")))
valores.append (int(input("Digite seu numero: ")))
valores.append (int(input("Digite seu numero: ")))
valores.append (int(input("Digite seu numero: ")))

menor = min(valores)
maior = max(valores)
dif = maior - menor


print("O maior valor é: ", maior)
print("O menor valor é: ", menor)
print("A diferença entre eles é: ", dif)