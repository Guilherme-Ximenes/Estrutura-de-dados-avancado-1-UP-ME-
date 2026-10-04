import pandas as pd
from rich.console import Console
from rich.panel import Panel

# Configs iniciais
console = Console()
df = pd.read_csv("dados/funcionarios.csv")

# Função para calcular Gini
def gini(dados):
    total = len(dados)

    if total == 0:
        return 0

    qtd_0 = len(dados[dados["saiu"] == 0])
    qtd_1 = len(dados[dados["saiu"] == 1])

    p0 = qtd_0 / total
    p1 = qtd_1 / total

    return 1 - (p0 ** 2 + p1 ** 2)

# Gini antes da divisão
total = len(df)

gini_antes = gini(df)


# Divisão pelo salário
ramo_esquerdo = df[df["salario"] <= 3500]
ramo_direito = df[df["salario"] > 3500]

gini_esquerdo = gini(ramo_esquerdo)
gini_direito = gini(ramo_direito)


# Gini ponderado
gini_ponderado = (
    (len(ramo_esquerdo) / total) * gini_esquerdo
    +
    (len(ramo_direito) / total) * gini_direito
)

# Resultado
resultado = f"""
Gini antes da divisão: [bold cyan]{gini_antes:.4f}[/bold cyan]
Gini salário <= 3500: [bold cyan]{gini_esquerdo:.4f}[/bold cyan]
Gini salário > 3500: [bold cyan]{gini_direito:.4f}[/bold cyan]
Gini ponderado: [bold cyan]{gini_ponderado:.4f}[/bold cyan]
"""

painel = Panel(
    resultado,
    title="Cálculo de Gini",
    subtitle="Divisão pelo salário",
    width=45
)

console.print(painel)