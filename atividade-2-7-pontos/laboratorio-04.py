import pandas as pd
from rich.console import Console

# config inicial
console = Console()

# =========== BST =============
class NoBST:
    def __init__(self, codigo):
        self.codigo = codigo
        self.esq = None
        self.dir = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo):

        def rec(no):
            if no is None:
                return NoBST(codigo)

            if codigo < no.codigo:
                no.esq = rec(no.esq)

            elif codigo > no.codigo:
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


    def buscar_comparacoes(self, codigo):
        no = self.raiz
        comparacoes = 0

        while no is not None:
            comparacoes += 1

            if codigo == no.codigo:
                return comparacoes

            elif codigo < no.codigo:
                no = no.esq

            else:
                no = no.dir

        return comparacoes
    
# =========== AVL =============
class NoAVL:
    def __init__(self, codigo):
        self.codigo = codigo
        self.esq = None
        self.dir = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None


    def obter_altura(self, no):
        if no is None:
            return 0

        return no.altura


    def fator_balanceamento(self, no):
        return (
            self.obter_altura(no.esq)
            -
            self.obter_altura(no.dir)
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


    def inserir(self, codigo):

        def rec(no):

            if no is None:
                return NoAVL(codigo)

            if codigo < no.codigo:
                no.esq = rec(no.esq)

            elif codigo > no.codigo:
                no.dir = rec(no.dir)

            else:
                return no


            no.altura = 1 + max(
                self.obter_altura(no.esq),
                self.obter_altura(no.dir)
            )


            balanceamento = self.fator_balanceamento(no)


            # Esquerda - Esquerda
            if balanceamento > 1 and codigo < no.esq.codigo:
                return self.rotacao_direita(no)


            # Direita - Direita
            if balanceamento < -1 and codigo > no.dir.codigo:
                return self.rotacao_esquerda(no)


            # Esquerda - Direita
            if balanceamento > 1 and codigo > no.esq.codigo:
                no.esq = self.rotacao_esquerda(no.esq)
                return self.rotacao_direita(no)


            # Direita - Esquerda
            if balanceamento < -1 and codigo < no.dir.codigo:
                no.dir = self.rotacao_direita(no.dir)
                return self.rotacao_esquerda(no)


            return no


        self.raiz = rec(self.raiz)


    def altura(self):
        return self.obter_altura(self.raiz)


    def buscar_comparacoes(self, codigo):
        no = self.raiz
        comparacoes = 0

        while no is not None:
            comparacoes += 1

            if codigo == no.codigo:
                return comparacoes

            elif codigo < no.codigo:
                no = no.esq

            else:
                no = no.dir

        return comparacoes

# Lendo os arquivos CSV
arquivos = [
    "dados/dados_ordenados.csv",
    "dados/dados_aleatorios.csv"
]

resultados = []

for arquivo in arquivos:

    df = pd.read_csv(arquivo)

    codigos = df["codigo"].tolist()

    bst = BST()
    avl = AVL()

    for codigo in codigos:
        bst.inserir(int(codigo))
        avl.inserir(int(codigo))


    maior_codigo = max(codigos)


    resultados.append({
        "Arquivo": arquivo.split("/")[-1],
        "Estrutura": "BST",
        "Altura": bst.altura(),
        "Comparações": bst.buscar_comparacoes(maior_codigo)
    })


    resultados.append({
        "Arquivo": arquivo.split("/")[-1],
        "Estrutura": "AVL",
        "Altura": avl.altura(),
        "Comparações": avl.buscar_comparacoes(maior_codigo)
    })

# exibindo tabela
tabela = pd.DataFrame(resultados)

console.print(
    "\n[bold yellow]Comparação BST x AVL:[/bold yellow]\n"
)

console.print(
    tabela.to_string(index=False)
)
''' 
Explicação:
Com os dados ordenados, a BST ficou degenerada, apresentando altura 20 e exigindo 20 comparações para localizar o maior código, 
comportamento próximo de O(n). A AVL, por realizar rotações e manter o balanceamento, apresentou altura muito menor e busca próxima de 
O(log n). Com os dados aleatórios, a BST ficou naturalmente mais equilibrada, reduzindo sua altura. Isso mostra que o desempenho da BST 
depende da ordem de inserção, enquanto a AVL oferece maior garantia de balanceamento.
'''