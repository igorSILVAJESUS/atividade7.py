nota1 = float(input("Informe a nota do aluno 1: "))
nota2 = float(input("Informe a nota do aluno 2: "))
nota3 = float(input("Informe a nota do aluno 3: "))
nota4 = float(input("Informe a nota do aluno 4: "))
nota5 = float(input("Informe a nota do aluno 5: "))

nota_alunos = [nota1, nota2, nota3, nota4, nota5]

maior = max(nota_alunos)
menor = min(nota_alunos)
media = sum(nota_alunos) / len(nota_alunos)

print(f"As notas dos alunos são: {nota_alunos}")
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"A média dos valores é: {media}")
