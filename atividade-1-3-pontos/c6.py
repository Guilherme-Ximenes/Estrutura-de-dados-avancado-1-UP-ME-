import pandas as pd
from rich.console import Console

# configs iniciais:
console = Console()

# No:
class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None
        self.altura = 1

# ==================== BST ======================
class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):

        def rec(no):
            if no is None:
                return No(chave)

            if chave < no.chave:
                no.esq = rec(no.esq)

            elif chave > no.chave:
                no.dir = rec(no.dir)

            return no

        self.raiz = rec(self.raiz)

    def altura(self):

        def rec(no):
            if no is None:
                return 0

            return 1 + max(
                rec(no.esq),
                rec(no.dir)
            )

        return rec(self.raiz)

    def quantidade_nos(self):

        def rec(no):
            if no is None:
                return 0

            return (
                1
                + rec(no.esq)
                + rec(no.dir)
            )

        return rec(self.raiz)

# ==================== AVL ======================
class AVL:
    def __init__(self):
        self.raiz = None

    def obter_altura(self, no):
        if no is None:
            return 0

        return no.altura

    def fator_balanceamento(self, no):
        if no is None:
            return 0

        return (
            self.obter_altura(no.esq)
            - self.obter_altura(no.dir)
        )

    def rotacao_direita(self, y):
        x = y.esq
        t2 = x.dir

        x.dir = y
        y.esq = t2

        y.altura = 1 + max(
            self.obter_altura(y.esq),
            self.obter_altura(y.dir)
        )

        x.altura = 1 + max(
            self.obter_altura(x.esq),
            self.obter_altura(x.dir)
        )

        return x

    def rotacao_esquerda(self, x):
        y = x.dir
        t2 = y.esq

        y.esq = x
        x.dir = t2

        x.altura = 1 + max(
            self.obter_altura(x.esq),
            self.obter_altura(x.dir)
        )

        y.altura = 1 + max(
            self.obter_altura(y.esq),
            self.obter_altura(y.dir)
        )

        return y

    def inserir(self, chave):

        def rec(no):
            if no is None:
                return No(chave)

            if chave < no.chave:
                no.esq = rec(no.esq)

            elif chave > no.chave:
                no.dir = rec(no.dir)

            else:
                return no

            no.altura = 1 + max(
                self.obter_altura(no.esq),
                self.obter_altura(no.dir)
            )

            balanceamento = self.fator_balanceamento(no)

            if balanceamento > 1 and chave < no.esq.chave:
                return self.rotacao_direita(no)

            if balanceamento < -1 and chave > no.dir.chave:
                return self.rotacao_esquerda(no)

            if balanceamento > 1 and chave > no.esq.chave:
                no.esq = self.rotacao_esquerda(no.esq)
                return self.rotacao_direita(no)

            if balanceamento < -1 and chave < no.dir.chave:
                no.dir = self.rotacao_direita(no.dir)
                return self.rotacao_esquerda(no)

            return no

        self.raiz = rec(self.raiz)

    def altura(self):
        return self.obter_altura(self.raiz)

    def quantidade_nos(self):

        def rec(no):
            if no is None:
                return 0

            return (
                1
                + rec(no.esq)
                + rec(no.dir)
            )

        return rec(self.raiz)

# lendo os arquivos:
arquivos = [
    "dados/dados_ordenados.csv",
    "dados/dados_aleatorios.csv"
]
resultados = []

for arquivo in arquivos:
    df = pd.read_csv(arquivo)

    if "codigo" in df:
        coluna_chave = "codigo"
    else:
        coluna_chave = df.columns[0]

    valores = df[coluna_chave].tolist()

    bst = BST()
    avl = AVL()

    for valor in valores:
        bst.inserir(valor)
        avl.inserir(valor)

    resultados.append({
        "Estrutura": "BST",
        "Arquivo": arquivo.split("/")[-1],
        "Quantidade de nós": bst.quantidade_nos(),
        "Altura": bst.altura()
    })

    resultados.append({
        "Estrutura": "AVL",
        "Arquivo": arquivo.split("/")[-1],
        "Quantidade de nós": avl.quantidade_nos(),
        "Altura": avl.altura()
    })


# tabela:
tabela = pd.DataFrame(resultados)

print("\nComparação de alturas:\n")
console.print(tabela.to_string(index=False))

''' 
EXPLICAÇÃO:
As alturas diferem porque a BST comum não realiza balanceamento automático, já a AVL sim. 
Na BST, quando os dados são inseridos em ordem crescente, os nós tendem a ser adicionados sempre 
no mesmo lado da árvore, fazendo com que sua estrutura pareça com uma lista e sua altura aumente 
significativamente. Na AVL, por outro lado, é realizado rotações sempre que necessário para manter o balanceamento, 
fazendo com que sua altura permaneça próxima de O(log n) independentemente da ordem de inserção.
'''