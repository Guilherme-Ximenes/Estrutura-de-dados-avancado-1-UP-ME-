import pandas as pd
from rich.console import Console
from rich.panel import Panel

# configs iniciais:
console = Console()
df = pd.read_csv("dados/funcionarios.csv")

# Gini antes da divisão:
total = len(df)

saiu_0 = len(df[df["saiu"] == 0])
saiu_1 = len(df[df["saiu"] == 1])

p0 = saiu_0 / total
p1 = saiu_1 / total

gini_antes = 1 - (p0 ** 2 + p1 ** 2)

# === Divisão pelo salário: ===
ramo_esquerdo = df[df["salario"] <= 3500]
ramo_direito = df[df["salario"] > 3500]

# Ramo <= 3500:
total_esquerdo = len(ramo_esquerdo)

esq_0 = len(ramo_esquerdo[ramo_esquerdo["saiu"] == 0])
esq_1 = len(ramo_esquerdo[ramo_esquerdo["saiu"] == 1])

p_esq_0 = esq_0 / total_esquerdo
p_esq_1 = esq_1 / total_esquerdo

gini_esquerdo = 1 - (p_esq_0 ** 2 + p_esq_1 ** 2)

# Ramo > 3500:
total_direito = len(ramo_direito)

dir_0 = len(ramo_direito[ramo_direito["saiu"] == 0])
dir_1 = len(ramo_direito[ramo_direito["saiu"] == 1])

p_dir_0 = dir_0 / total_direito
p_dir_1 = dir_1 / total_direito

gini_direito = 1 - (p_dir_0 ** 2 + p_dir_1 ** 2)

# === Gini ponderado: ===
gini_ponderado = (
    (total_esquerdo / total) * gini_esquerdo
    +
    (total_direito / total) * gini_direito
)

# === Resultados: ===
resultado = f"""
Gini antes da divisão: [bold cyan]{gini_antes:.4f}[/bold cyan]
Gini salário <= 3500: [bold cyan]{gini_esquerdo:.4f}[/bold cyan]
Gini salário > 3500: [bold cyan]{gini_direito:.4f}[/bold cyan]
Gini ponderado: [bold cyan]{gini_ponderado:.4f}[/bold cyan]
"""
painel = Panel(
    resultado,
    title="cálculo de Gini",
    subtitle="Decisão de divisão pelo salário",
    width=40,    
)

console.print(painel)