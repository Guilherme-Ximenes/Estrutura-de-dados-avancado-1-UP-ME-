import pandas as pd
from rich.console import Console

# Configs iniciais
console = Console()

df = pd.read_csv("dados/acessos.csv")

acessos = df["produto"].tolist()

# NÓ
class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None


# SPLAY TREE
class SplayTree:
    def __init__(self):
        self.raiz = None

    def rotacao_direita(self, no):
        novo_topo = no.esq

        no.esq = novo_topo.dir
        novo_topo.dir = no

        return novo_topo

    def rotacao_esquerda(self, no):
        novo_topo = no.dir

        no.dir = novo_topo.esq
        novo_topo.esq = no

        return novo_topo

    def splay(self, raiz, chave):
        if raiz is None or raiz.chave == chave:
            return raiz

        # Chave está à esquerda
        if chave < raiz.chave:

            if raiz.esq is None:
                return raiz

            # Zig-Zig
            if chave < raiz.esq.chave:
                raiz.esq.esq = self.splay(
                    raiz.esq.esq,
                    chave
                )

                raiz = self.rotacao_direita(raiz)

            # Zig-Zag
            elif chave > raiz.esq.chave:
                raiz.esq.dir = self.splay(
                    raiz.esq.dir,
                    chave
                )

                if raiz.esq.dir is not None:
                    raiz.esq = self.rotacao_esquerda(
                        raiz.esq
                    )

            if raiz.esq is None:
                return raiz

            return self.rotacao_direita(raiz)

        # Chave está à direita
        else:
            if raiz.dir is None:
                return raiz

            # Zig-Zig
            if chave > raiz.dir.chave:
                raiz.dir.dir = self.splay(
                    raiz.dir.dir,
                    chave
                )

                raiz = self.rotacao_esquerda(raiz)

            # Zig-Zag
            elif chave < raiz.dir.chave:
                raiz.dir.esq = self.splay(
                    raiz.dir.esq,
                    chave
                )

                if raiz.dir.esq is not None:
                    raiz.dir = self.rotacao_direita(
                        raiz.dir
                    )

            if raiz.dir is None:
                return raiz

            return self.rotacao_esquerda(raiz)

    def buscar(self, chave):
        self.raiz = self.splay(self.raiz, chave)
        return self.raiz

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
            return

        self.raiz = self.splay(self.raiz, chave)

        # Não insere duplicado
        if self.raiz.chave == chave:
            return

        novo = No(chave)

        if chave < self.raiz.chave:
            novo.dir = self.raiz
            novo.esq = self.raiz.esq

            self.raiz.esq = None

        else:
            novo.esq = self.raiz
            novo.dir = self.raiz.dir

            self.raiz.dir = None

        self.raiz = novo


# funcao para criar a arvore:

def criar_arvore():
    arvore = SplayTree()

    for produto in dict.fromkeys(acessos):
        arvore.inserir(produto)

    return arvore


# sequencia original:
arvore_original = criar_arvore()

console.print(
    "\n[bold cyan]=== Sequência original ===[/bold cyan]"
)

for produto in acessos:
    arvore_original.buscar(produto)

    console.print(
        f"Acesso: [yellow]{produto}[/yellow] "
        f"-> Raiz: [green]{arvore_original.raiz.chave}[/green]"
    )

# sequencia com blocos repetidos
acessos_repetidos = []

for produto in acessos:
    acessos_repetidos.extend([produto] * 3)


arvore_repetida = criar_arvore()

console.print(
    "\n[bold cyan]=== Sequência com blocos repetidos ===[/bold cyan]"
)

for produto in acessos_repetidos:
    arvore_repetida.buscar(produto)

    console.print(
        f"Acesso: [yellow]{produto}[/yellow] "
        f"-> Raiz: [green]{arvore_repetida.raiz.chave}[/green]"
    )