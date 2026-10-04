import pandas as pd
import heapq as hq
from rich.console import Console

#configs iniciais:
console = Console()
df = pd.read_csv("dados/chamados.csv")

#criando fila heap:
fila = []

#adicionando dados na heap:
for _, r in df.iterrows():
    hq.heappush(fila, (int(r.prioridade), int(r.id), r.cliente, r.problema))

# 5 primeiras linhas:
console.print("[bold yellow]Cinco primeiras linhas:[/bold yellow]")
console.print(df.head(5))

# Primeiro chamado sem exluir permanentemente a fila original:
console.print("\n[bold yellow]Primeiro chamado:[/bold yellow] ")
console.print(fila[0])

# chamados em ordem de prioridade em uma cópia da fila original:
console.print("\n[bold yellow]Chamados em ordem de prioridade:[/bold yellow] 📋")
fila_copia = fila.copy()
while fila_copia:
    chamado = hq.heappop(fila_copia)
    prioridade, id, cliente, problema = chamado
    console.print(f"Prioridade: {prioridade}, ID: {id}, Cliente: {cliente}, Problema: {problema}")

# adicionando um novo chamado na fila original de prioridade 1 e exibindo a posição lógica do novo chamado na fila original:
hq.heappush(fila, (1, 109, "Empresa Zé delivery", "Falta de dinheiro"))

fila_copia_2 = fila.copy()

posicao = 1

console.print("\n[bold yellow]Adicionando um novo chamado na fila original de prioridade 1:[/bold yellow] 🆕")
while fila_copia_2:
    chamado = hq.heappop(fila_copia_2)
    prioridade, id, cliente, problema = chamado
    console.print(f"{posicao}º - Prioridade: {prioridade}, ID: {id}, Cliente: {cliente}, Problema: {problema}")
    if chamado == (1, 109, "Empresa Zé delivery", "Falta de dinheiro"):
        posicao_novo = posicao

    posicao += 1

console.print(f"\n[red]O novo chamado ficou na posição {posicao_novo} da ordem de atendimento.[/red]")

'''
A Min-Heap é mais adequada para uma fila de prioridade porque mantém o elemento de menor prioridade numérica no topo da estrutura. 
Dessa forma, consultar o próximo chamado custa O(1), enquanto remover ou inserir um chamado custa O(log n).
'''