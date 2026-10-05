import pandas as pd
from rich.console import Console

# configs iniciais
df_produtos = pd.read_csv("dados/produtos.csv")
df_acessos = pd.read_csv("dados/acessos.csv")
console = Console()

# NO
class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None

# SplayTree:
class Splaytree:
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

        # chave está à esquerda
        if chave < raiz.chave:

            if raiz.esq is None:
                return raiz

            # Zig-zig
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
  
# Criando a Splay Tree:
arvore = Splaytree()

# inserindo todos os produtos:
for produto in df_produtos['produto']:
    arvore.inserir(produto)

print("\nRaiz após inserir todos os produtos:")
console.print(arvore.raiz.chave)

# Contar os acessos:
contagem_acessos = {}
contagem_raizes = {}

print("\nBuscas realizadas:\n")

for produto in df_acessos["produto"]:
    # contando quantidade de buscas:
    if produto in contagem_acessos:
        contagem_acessos[produto] += 1
    else:
        contagem_acessos[produto] = 1

    # busca com operação de splay
    arvore.buscar(produto)

    # mostrando a raiz após a busca
    console.print(
        f"Produto buscado: {produto} | "
        f"Raíz atual: {arvore.raiz.chave}"
    )

    # contando quantas vezes cada produto apareceu na raiz:
    raiz_atual = arvore.raiz.chave

    if raiz_atual in contagem_raizes:
        contagem_raizes[raiz_atual] += 1
    else:
        contagem_raizes[raiz_atual] = 1

print("\nQuantidade de acessos por produto:\n")

for produto, quantidade in contagem_acessos.items():
    console.print(
        f"{produto}: {quantidade} acesso(s)"
    )


print("\nQuantidade de vezes que cada produto apareceu na raiz:\n")

for produto, quantidade in contagem_raizes.items():
    console.print(
        f"{produto}: {quantidade} vez(es)"
    )
'''
Explicação:
A Splay Tree se autoajusta conforme os produtos são acessados, movendo o elemento buscado 
para a raiz por meio de rotações. Dessa forma, produtos acessados com frequência tendem a 
aparecer repetidamente próximos ou na própria raiz da árvore. Essa caracterítica pode ser 
vantajoso em relação a uma BST comum quando existe localidade temporal, ou seja, quando 
determinados elementos são acessados repetidamente em um curto período. Na BST comum, 
a estrutura não muda após uma busca, enquanto na Splay Tree os acessos recentes influenciam 
sua organização, tornando próximas buscas desses mesmos elementos mais rápidas.
'''