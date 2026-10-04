import pandas as pd
from rich.console import Console

# configs iniciais:
console = Console()
df = pd.read_csv("dados/vendas.csv")

# TreeSort:
class No:
    def __init__(self, id, produto, valor):
        self.id = id
        self.produto = produto
        self.valor = valor
        self.esq = None
        self.dir = None

class TreeSort:
    def __init__(self):
        self.raiz = None

    def inserir(self, id, produto, valor):
        def rec(no):
            if no is None:
                return No(id, produto, valor)
            elif valor < no.valor:
                no.esq = rec(no.esq)
            else:
                no.dir = rec(no.dir)
            return no
        self.raiz = rec(self.raiz)

    def percurso_decrescente(self):
        resultados = []
        def rec(no):
            if no is not None:
                rec(no.dir)
                resultados.append((no.id, no.produto, no.valor))
                rec(no.esq)
        rec(self.raiz)
        return resultados

# Criando a arrvore e inserindo os dados do dataframe:
tree_sort = TreeSort()
for _, r in df.iterrows():
    tree_sort.inserir(int(r.id), r.produto, float(r.valor))

# Percorrendo a árvore em ordem decrescente e criando um df com os valores ordenados:
resultados_decrescentes = tree_sort.percurso_decrescente()

df_ordenado = pd.DataFrame(
    resultados_decrescentes,
    columns=["id", "produto", "valor"]
)

df_ordenado.to_csv(
    "dados/vendas_ordenadas_desc.csv",
    index=False
)

console.print("\nVendas em ordem decrescente de valor:")

for id, produto, valor in resultados_decrescentes:
    console.print(
        f"{id}: {produto} - R$ {valor:.2f}"
    )