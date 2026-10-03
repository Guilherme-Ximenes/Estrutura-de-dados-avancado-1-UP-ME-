import pandas as pd
from rich.console import Console

# configs iniciais:
console = Console()
df = pd.read_csv('dados/produtos.csv')

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
            elif codigo < no.codigo:
                no.esq = rec(no.esq)
            elif codigo > no.codigo:
                no.dir = rec(no.dir)
            else:
                no.produto, no.categoria, no.preco, no.estoque = produto, categoria, preco, estoque
            return no

        self.raiz = rec(self.raiz)

    def buscar_entre_30_70(self): # buscar apenas os proutos com código entre 30 e 70
        resultados = []
        def rec(no):
            if no is not None:
                if 30 <= no.codigo <= 70:
                    resultados.append((no.codigo, no.produto, no.categoria, no.preco, no.estoque))

                if no.codigo > 30:
                    rec(no.esq)

                if no.codigo < 70:
                    rec(no.dir)

        rec(self.raiz)
        return resultados

bst = BST()
for _, r in df.iterrows(): #adicionando o dataframe na BST
    bst.inserir(int(r.codigo), r.produto, r.categoria, float(r.preco), int(r.estoque))

# Buscando produtos com código entre 30 e 70:
produtos_30_70 = bst.buscar_entre_30_70()

console.print("\nProdutos com código entre [bold yellow] 30 [/bold yellow] e [bold yellow] 70 [/bold yellow]:")
for produto in produtos_30_70:
    console.print(f"[bold yellow]Código: {[produto[0]]}[/bold yellow] | [bold green]Produto: {produto[1]} [/bold green]")
