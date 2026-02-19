valores = []

valores.append (float(input("Digite seu numero: ")))
valores.append (float(input("Digite seu numero: ")))
valores.append (float(input("Digite seu numero: ")))
valores.append (float(input("Digite seu numero: ")))

menor = min(valores)
posicao = valores.index(menor)
print("O menor valor dessa lista é: ",menor)
print("A posição que ele se encontra é: ",posicao)