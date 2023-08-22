def calcular_elevacao(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * calcular_elevacao(base, expoente - 1)

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = calcular_elevacao(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")