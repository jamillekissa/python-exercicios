# Exercício 01 — Análise de Notas de Alunos
# Objetivo: explorar um dataset simples e extrair insights

import pandas as pd

# Dataset
dados = {
    "aluno": ["Ana", "Bruno", "Carol", "Diego", "Elena"],
    "nota_1": [8.5, 6.0, 9.0, 4.5, 7.5],
    "nota_2": [7.0, 8.0, 9.5, 5.0, 6.5],
    "nota_3": [9.0, 5.5, 10.0, 6.0, 8.0]
}

df = pd.DataFrame(dados)

# Média por aluno
df["media"] = df[["nota_1", "nota_2", "nota_3"]].mean(axis=1).round(2)

# Situação dos alunos
df["situacao"] = df["media"].apply(
    lambda x: "Aprovado" if x >= 6 else "Reprovado"
)

# Análises
print("=== NOTAS DOS ALUNOS ===")
print(df.to_string(index=False))

print("\n=== ESTATÍSTICAS GERAIS ===")
print(f"Maior média: {df['media'].max():.2f}")
print(f"Menor média: {df['media'].min():.2f}")
print(f"Média da turma: {df['media'].mean():.2f}")
print(f"Aprovados: {(df['situacao'] == 'Aprovado').sum()}")
print(f"Reprovados: {(df['situacao'] == 'Reprovado').sum()}")
