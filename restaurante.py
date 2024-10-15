def valorPratos():
    while True:
        print("Seja bem-vindo ao restaurante japonês Komero Mioku!")
        valor = float(input("Insira o valor total de sua refeição (favor substituir a vírgula por um ponto): "))
        return valor

def calculaTaxa():
    taxa = (valor / 10)
    return taxa

def calculaTotal():
    valorTotal = (valor + taxa)
    return valorTotal

valor = valorPratos()
taxa = calculaTaxa()
valorTotal = calculaTotal()

print(f"Valor da refeição: {valor:.2f}")
print(f"Valor da taxa de serviço: {taxa:.2f}")
print(f"Valor total: {valorTotal:.2f}")
print("Muito obrigado por escolher o nosso restaurante!")


