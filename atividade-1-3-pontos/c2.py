import pandas as pd
import heapq as hq
from rich.console import Console
from rich.panel import Panel

# dataframe
df = pd.read_csv('dados/chamados.csv')
#Heap fila
fila = []

#adicionando no heap fila
for _, r in df.iterrows():
    hq.heappush(fila, (int(r.prioridade), int(r.tempo_estimado), int(r.id), r.cliente))

# ==== Atividade 2 (C2) ======
fila_copia = fila.copy()
# ========================

#Ordem de chamado:
console = Console() #Console do rich(estilização)
ordem_chamados = [] 
contador = 1

for i in range(3):
    chamado = hq.heappop(fila_copia) # até aqui é a atividade, em diante é para estilização com rich
    prioridade, tempo, id, cliente = chamado
    ordem_chamados.append(
        f"[bold cyan]{contador:>2}º chamado:[/bold cyan]  "
        f"[bright_green]{cliente:15}[/bright_green]  "
        f"[yellow]Prioridade {prioridade:>1}[/yellow]  "
        f"[white bold]Tempo: {tempo:>2} min[/white bold]"
    )
    contador += 1

#painel rich (estilização)
painel_fila_copia = Panel(
    "\n".join(ordem_chamados),
    title="Ordem de chamados(próximos 3 atendimentos e sem excluir a fila original)",
    subtitle="Organizado por prioridade e tempo estimado",
    width=75,
    border_style="dark_green",
)

# Fila original:
console.print("Fila original: ")
console.print(fila)

# Cópia:
console.print("\nCópia da fila original, após remover os 3 próximos chamados:")
console.print(fila_copia)

# C2 -> imprimindo os 3 próximos chamados a serem atendidos (sem alterar a fila original):
console.print("\nPróximos 3 chamados a serem atendidos (sem alterar a fila original):")
console.print(painel_fila_copia)
