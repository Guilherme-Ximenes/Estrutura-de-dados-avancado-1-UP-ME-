import pandas as pd
from rich.console import Console

# configs iniciais:
console = Console()
df = pd.read_csv("dados/produtos.csv")

# No:
class No:
    def __init__(self, codigo, produto, preco, estoque):
        self.codigo = codigo
        self.produto = produto
        self.preco = preco
        self.estoque = estoque
        self.esq = None
        self.dir = None

# BST
class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo, produto, preco, estoque):
        def rec(no):
            if no is None:
                return No(codigo, produto, preco, estoque)
            elif codigo < no.codigo:
                no.esq = rec(no.esq)
            elif codigo > no.codigo:
                no.dir = rec(no.dir)
            else:
                no.produto, no.preco, no.estoque = produto, preco, estoque
            return no
        self.raiz = rec(self.raiz)

    def buscar(self, codigo):
        def rec(no):
            if no is None:
                return None

            if codigo == no.codigo:
                return no

            if codigo < no.codigo:
                return rec(no.esq)

            return rec(no.dir)

        return rec(self.raiz)

    def remover_no(self, codigo):
        def menor(no):
            while no.esq is not None:
                no = no.esq
            return no

        def rec(no, codigo_remover):
            if no is None:
                return None

            if codigo_remover < no.codigo:
                no.esq = rec(no.esq, codigo_remover)

            elif codigo_remover > no.codigo:
                no.dir = rec(no.dir, codigo_remover)

            else:
                # Sem filho esquerdo
                if no.esq is None:
                    return no.dir

                # Sem filho direito
                if no.dir is None:
                    return no.esq

                # Dois filhos
                sucessor = menor(no.dir)

                no.codigo = sucessor.codigo
                no.produto = sucessor.produto
                no.preco = sucessor.preco
                no.estoque = sucessor.estoque

                no.dir = rec(no.dir, sucessor.codigo)

            return no

        self.raiz = rec(self.raiz, codigo)

    def altura(self):
        def rec(no):
            if no is None:
                return 0

            h_esq = rec(no.esq)
            h_dir = rec(no.dir)

            return 1 + max(h_esq, h_dir)

        return rec(self.raiz)
            
                
    def em_ordem(self):
        resultados = []

        def rec(no):
            if no is None:
                return
            rec(no.esq)
            resultados.append((no.codigo, no.produto, no.preco, no.estoque))
            rec(no.dir)

        rec(self.raiz)
        return resultados

    def exibir_arvore(self, mensagem):
        console.print(f"\n[bold yellow]{mensagem}[/bold yellow]")

        resultados = bst.em_ordem()

        for codigo, produto, preco, estoque in resultados:
            console.print(
                f"Código: {codigo} | "
                f"Produto: {produto} | "
                f"Preço: R$ {preco:.2f} | "
                f"Estoque: {estoque}"
            )

        console.print(
            f"[bold cyan]Altura da árvore: {bst.altura()}[/bold cyan]"
        )

# Confirmando se aparece ordenado os códigos:
bst = BST()

for _, r in df.iterrows():
    bst.inserir(int(r.codigo), r.produto, int(r.preco), int(r.estoque))

bst.exibir_arvore("Árvore inicial")

# Removendo nós:
bst.remover_no(30)
bst.remover_no(50)
bst.remover_no(80)
bst.exibir_arvore("Após remover os nós 30, 50 e 80")




            

            
            

    



