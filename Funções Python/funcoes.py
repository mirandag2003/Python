def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    return media

def verificar_aprovacao(media):
    if media >= 7:
        return "aprovado"
    else:
        return "Reprovado"