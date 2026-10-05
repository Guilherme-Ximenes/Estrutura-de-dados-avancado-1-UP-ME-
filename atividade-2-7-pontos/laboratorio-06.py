import pandas as pd
from rich.console import Console

# configs iniciais
console = Console()

df = pd.read_csv("dados/vendas.csv")

# No:
class No:
    def __init__(self, id, produto, valor):
        self.id = id
        self.produto = produto
        self.valor = valor
        self.esq = None
        self.dir = None

# Tree:
class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, id, produto, valor):
        def rec(no):
            if no is None:
                return No(id, produto, valor)

            if valor < no.valor:
                no.esq = rec(no.esq)

            else:
                no.dir = rec(no.dir)

            return no

        self.raiz = rec(self.raiz)

    def em_ordem(self):
        vendas_ordenadas = []
        def rec(no):
            if no is None:
                return

            rec(no.esq)

            vendas_ordenadas.append({
                "id": no.id,
                "produto": no.produto,
                "valor": no.valor
            })

            rec(no.dir)

        rec(self.raiz)

        return vendas_ordenadas

# criando a arvore:
arvore = BST()

# adiciona os dados na arvore:
for _, linha in df.iterrows():
    arvore.inserir(
        int(linha["id"]),
        linha["produto"],
        int(linha["valor"])
    )

# ordena os dados:
vendas_ordenadas = arvore.em_ordem()

df_ordenado = pd.DataFrame(vendas_ordenadas)

# salvar csv:
df_ordenado.to_csv(
    "dados/vendas_ordenadas.csv",
    index=False
)

# validar visualmente:
print("\nVendas ordenadas:\n")
console.print(df_ordenado.to_string(index=False))

'''
Explicação: 
Se os valores já chegarem em ordem crescente, uma BST comum pode ficar
desbalanceada, com os nós sendo inseridos sucessivamente à direita. Nesse caso,
a árvore assume uma estrutura semelhante a uma lista, fazendo com que as
inserções possam chegar a O(n) e a construção completa da árvore a O(n²).
'''