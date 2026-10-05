import pandas as pd
from rich.console import Console

# configs iniciais:
console = Console()
df = pd.read_csv("dados/funcionarios.csv")


# mapeamento: (a troca dos cargos por numeros sao para a arvore de decisao trabalhar com numeros)
df["cargo"] = df["cargo"].map({
    "Analista": 0,
    "Desenvolvedor": 1,
    "Gerente": 2
})

# separando X:
colunas_x = [
    "idade",
    "salario",
    "tempo_empresa",
    "cargo"
]

x = df[colunas_x].values.tolist()

#separando Y:
y = df["saiu"].tolist()

# criando funcao gini_impurity:
def gini_impurity(y_subset):
    total = len(y_subset)

    if total == 0:
        return 0

    qtd_0 = y_subset.count(0)
    qtd_1 = y_subset.count(1)

    p0 = qtd_0 / total
    p1 = qtd_1 / total

    gini = 1 - (p0 ** 2 + p1 ** 2)

    return gini

'''
Questão incompleta, não soubemos resolver.
'''