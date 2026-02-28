from funcoes import calcular_media,verificar_aprovacao

notas = []
quantidade = int(input("Quantas notas:"))

for i in range(quantidade):
    nota = float(input(f"Nota{i + 1}:"))
    notas.append(nota)

media = calcular_media(notas)
status = verificar_aprovacao(media)

print(status)