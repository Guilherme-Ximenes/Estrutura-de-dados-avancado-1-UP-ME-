import pandas as pd
from rich.console import Console

#configs iniciais:
df = pd.read_csv("dados/palavras.csv")
console = Console()

#TRIE:
class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False
        self.palavra = None
        self.buscas = 0


class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra, buscas):
        no = self.raiz

        palavra_normalizada = palavra.lower()

        for letra in palavra_normalizada:
            if letra not in no.filhos:
                no.filhos[letra] = TrieNode()

            no = no.filhos[letra]

        no.fim_palavra = True
        no.palavra = palavra
        no.buscas = buscas

    def buscar_prefixo(self, prefixo, limite=5):
        no = self.raiz

        prefixo = prefixo.lower()

        for letra in prefixo:
            if letra not in no.filhos:
                return []

            no = no.filhos[letra]

        resultados = []
        def coletar(no):
            if no.fim_palavra:
                resultados.append(
                    (no.palavra, no.buscas)
                )

            for filho in no.filhos.values():
                coletar(filho)

        coletar(no)

        
        resultados.sort(key=lambda item: item[1], reverse=True)

        return resultados[:limite]


# criando trie e adicionando os dados csv
trie = Trie()

for r in df.itertuples(index=False):
    trie.inserir(
        str(r.termo),
        int(r.buscas)
        )

# Consultas
while True:
    prefixo = input("Digite um prefixo: ").strip()
    sugestoes = trie.buscar_prefixo(prefixo)

    if sugestoes:
        console.print("\nSugestões:")

        for palavra, buscas in sugestoes:
            console.print(f"{palavra} - {buscas} buscas")

        break

    else:
        console.print("\nNenhuma palavra encontrada.")
        continue
    