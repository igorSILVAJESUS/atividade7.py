notas = []
for i in range(1, 6):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

notas.remove(max(notas))
notas.remove(min(notas))

media = sum(notas) / len(notas)

print(f"Média das notas (descontando a maior e a menor): {media:.1f}")
