import pandas as pd
from rich.console import Console

# configs iniciais
console = Console()
df = pd.read_csv("dados/palavras.csv")


# NÓ
class No:
    def __init__(self):
        self.filhos = {}
        self.fim_termo = False
        self.termo = None
        self.buscas = 0


# TRIE
class Trie:
    def __init__(self):
        self.raiz = No()

    def insert(self, termo, buscas):
        termo = termo.lower()

        no = self.raiz

        for letra in termo:

            if letra not in no.filhos:
                no.filhos[letra] = No()

            no = no.filhos[letra]

        no.fim_termo = True
        no.termo = termo
        no.buscas = buscas

    def search(self, termo):
        termo = termo.lower()

        no = self.raiz

        for letra in termo:

            if letra not in no.filhos:
                return False

            no = no.filhos[letra]

        return no.fim_termo
    
    def starts_with(self, prefixo):
        prefixo = prefixo.lower()

        no = self.raiz

        for letra in prefixo:

            if letra not in no.filhos:
                return []

            no = no.filhos[letra]

        resultados = []

        def coletar(no):

            if no.fim_termo:
                resultados.append(
                    (no.termo, no.buscas)
                )

            for filho in no.filhos.values():
                coletar(filho)


        coletar(no)

        resultados.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return resultados


# Criando trie
trie = Trie()

for _, r in df.iterrows():

    termo = str(r.termo).lower()
    buscas = int(r.buscas)

    trie.insert(termo, buscas)

# teste search
termo_teste = str(df["termo"][0]).lower()

console.print(
    "\n[bold yellow]Busca por termo completo:[/bold yellow]"
)

console.print(
    f"{termo_teste}: {trie.search(termo_teste)}"
)

# Consultas prefixos
prefixos = ["mo", "me", "note", "te"]

for prefixo in prefixos:

    console.print(
        f"\n[bold cyan]Sugestões para '{prefixo}':[/bold cyan]"
    )

    sugestoes = trie.starts_with(prefixo)

    if not sugestoes:
        console.print("Nenhum termo encontrado.")

    else:
        for termo, buscas in sugestoes:
            console.print(
                f"{termo} - {buscas} buscas"
            )