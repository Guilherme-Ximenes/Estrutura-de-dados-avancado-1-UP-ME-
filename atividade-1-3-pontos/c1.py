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

#Ordem de chamado:
console = Console()
ordem_chamados = [] #Console do rich(estilização)
contador = 1

while fila:
    chamado = hq.heappop(fila) # até aqui é a atividade, em diante é para estilização com rich
    prioridade, tempo, id, cliente = chamado 
    ordem_chamados.append(
        f"[bold cyan]{contador:>2}º chamado:[/bold cyan]  "
        f"[bright_green]{cliente:15}[/bright_green]  "
        f"[yellow]Prioridade {prioridade:>1}[/yellow]  "
        f"[white bold]Tempo: {tempo:>2} min[/white bold]"
    )
    contador += 1

#painel rich (estilização)
painel = Panel(
    "\n".join(ordem_chamados),
    title="Ordem de chamados",
    subtitle="Organizado por prioridade e tempo estimado",
    width=75,
    border_style="dark_green",
)

console.print(painel)
