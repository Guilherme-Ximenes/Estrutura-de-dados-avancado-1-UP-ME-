import pandas as pd
import math
from rich.console import Console

#configs iniciais:
console = Console()
df = pd.read_csv("dados/funcionarios.csv")

# função entropy:
def entropy(dados):
    total = len(dados)

    if total == 0:
        return 0

    qtd_0 = len(dados[dados["saiu"] == 0])
    qtd_1 = len(dados[dados["saiu"] == 1])

    p0 = qtd_0 / total
    p1 = qtd_1 / total

    entropia = 0

    if p0 > 0:
        entropia -= p0 * math.log2(p0)

    if p1 > 0:
        entropia -= p1 * math.log2(p1)

    return entropia

# função gini:
def gini(dados):
    total = len(dados)

    if total == 0:
        return 0

    qtd_0 = len(dados[dados["saiu"] == 0])
    qtd_1 = len(dados[dados["saiu"] == 1])

    p0 = qtd_0 / total
    p1 = qtd_1 / total

    return 1 - (p0 ** 2 + p1 ** 2)


total = len(df)

resultados = []

# === Divisão 1: salario <= 3500: ===
esquerda = df[df["salario"] <= 3500]
direita = df[df["salario"] > 3500]

gini_salario = (
    (len(esquerda) / total) * gini(esquerda)
    +
    (len(direita) / total) * gini(direita)
)

entropia_salario = (
    (len(esquerda) / total) * entropy(esquerda)
    +
    (len(direita) / total) * entropy(direita)
)

resultados.append(
    ("salario <= 3500", gini_salario, entropia_salario)
)

# === Divisão 2: idade <= 30: ===
esquerda = df[df["idade"] <= 30]
direita = df[df["idade"] > 30]

gini_idade = (
    (len(esquerda) / total) * gini(esquerda)
    +
    (len(direita) / total) * gini(direita)
)

entropia_idade = (
    (len(esquerda) / total) * entropy(esquerda)
    +
    (len(direita) / total) * entropy(direita)
)

resultados.append(
    ("idade <= 30", gini_idade, entropia_idade)
)

# === Divisão 3: tempo_empresa <= 3: ===
esquerda = df[df["tempo_empresa"] <= 3]
direita = df[df["tempo_empresa"] > 3]

gini_tempo = (
    (len(esquerda) / total) * gini(esquerda)
    +
    (len(direita) / total) * gini(direita)
)

entropia_tempo = (
    (len(esquerda) / total) * entropy(esquerda)
    +
    (len(direita) / total) * entropy(direita)
)

resultados.append(
    ("tempo_empresa <= 3", gini_tempo, entropia_tempo)
)

# Exibindo resultados:
console.print("\nComparação das divisões:\n")

for divisao, valor_gini, valor_entropia in resultados:
    console.print(divisao)
    console.print(f"Gini: {valor_gini:.4f}")
    console.print(f"Entropia: {valor_entropia:.4f}")
    console.print()

# Melhor divisão pelo Gini e pela Entropia:
melhor_gini = min(
    resultados,
    key=lambda item: item[1]
)

melhor_entropia = min(
    resultados,
    key=lambda item: item[2]
)


console.print("Melhor divisão pelo Gini:")
console.print(
    f"{melhor_gini[0]} "
    f"(Gini = {melhor_gini[1]:.4f})"
)

console.print("\nMelhor divisão pela Entropia:")
console.print(
    f"{melhor_entropia[0]} "
    f"(Entropia = {melhor_entropia[2]:.4f})"
)