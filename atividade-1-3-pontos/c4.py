import pandas as pd
from rich.console import Console

# configs inicias:
df = pd.read_csv('dados/produtos.csv')
console = Console()

# No + BST:
class No:
    def __init__(self, codigo, produto, categoria, preco, estoque):
        self.codigo = codigo
        self.produto = produto
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque
        self.esq = None 
        self.dir = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo, produto, categoria, preco, estoque):
        def rec(no):
            if no is None:
                return No(codigo, produto, categoria, preco, estoque)
            elif preco < no.preco:
                no.esq = rec(no.esq)
            elif preco > no.preco:
                no.dir = rec(no.dir)
            else:
                no.produto, no.categoria, no.preco, no.estoque = produto, categoria, preco, estoque
            return no

        self.raiz = rec(self.raiz)

    def exibir_em_ordem(self):
        produtos = []
        def rec(no):
            if no is not None:
                rec(no.esq)
                produtos.append((int(no.codigo), no.produto, no.categoria, float(no.preco), int(no.estoque)))
                rec(no.dir)
        rec(self.raiz)
        return produtos

# Criação da BST e inserção dos produtos do DataFrame:
bst = BST()

for _, r in df.iterrows():
    bst.inserir(int(r.codigo), r.produto, r.categoria, float(r.preco), int(r.estoque))

# Exibição dos resultados:
produtos_crescente = bst.exibir_em_ordem()

console.print("\nProdutos do [bold red] mais barato [/bold red] ao [bold green] mais caro [/bold green] :")
for p in produtos_crescente:
    console.print(f"""
    Produto:[bold blue] {p[1]} [/bold blue] 
    Preço:[bold yellow] R${p[3]:.2f} [/bold yellow] 
    Código:[bold white] {p[0]} [/bold white] 
    Categoria:[bold green] {p[2]} [/bold green] 
    Estoque:[bold cyan] {p[4]} [/bold cyan]
    """)