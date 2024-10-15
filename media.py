
notas = []

num_notas = int(input("Quantas notas você deseja inserir? "))

for i in range(num_notas):
  while True:
    try:
      nota = float(input(f"Digite a nota {i+1} (com casas decimais): "))
      if 0 <= nota <= 10:  
        notas.append(nota)
        break
      else:
        print("Nota inválida. A nota deve estar entre 0 e 10.")
    except ValueError:
      print("Entrada inválida. Por favor, insira um número decimal.")

media = sum(notas) / len(notas) if notas else 0

print(f"A média das notas inseridas é: {media:.1f}")


