# Estrutura de Dados Avançada — Atividades Avaliativas

Repositório destinado ao desenvolvimento das atividades avaliativas da disciplina de **Estrutura de Dados Avançada**, do curso de **Ciência da Computação — 3º Período**.

As atividades serão desenvolvidas em dupla e têm como objetivo aplicar, na prática, diferentes estruturas de dados e algoritmos utilizando Python.

## Informações

- **Curso:** Ciência da Computação
- **Integrantes da dupla:** Guilherme Ximenes e Jonatas José
- **Período:** 3º Período
- **Disciplina:** Estrutura de Dados Avançada
- **Data de entrega:** 05/10/2026
- **Linguagem principal:** Python

## Tecnologias

Durante o desenvolvimento das atividades serão utilizadas principalmente:

- Python
- Pandas
- NumPy
- Bibliotecas da biblioteca padrão do Python, como `heapq`
- Outras bibliotecas poderão ser utilizadas quando necessário

---

# Atividade Complementar — 0 a 3 pontos

A atividade é composta por **10 questões**, envolvendo diferentes estruturas de dados, algoritmos de ordenação, análise de árvores e métricas utilizadas em árvores de decisão.

## Questões

| Questão | Conteúdo                    | Arquivo/Dados                                  |
| ------- | --------------------------- | ---------------------------------------------- |
| C1      | Heap com desempate          | `chamados.csv`                                 |
| C2      | Top 3 chamados urgentes     | `chamados.csv`                                 |
| C3      | Busca de faixa na BST       | `produtos.csv`                                 |
| C4      | BST: preço como chave       | `produtos.csv`                                 |
| C5      | Trie com ranking            | `palavras.csv`                                 |
| C6      | Comparação de alturas       | `dados_ordenados.csv` / `dados_aleatorios.csv` |
| C7      | Splay e localidade temporal | `acessos.csv`                                  |
| C8      | TreeSort decrescente        | `vendas.csv`                                   |
| C10     | Entropia                    | `funcionarios.csv`                             |
| C9      | Gini manual                 | `funcionarios.csv`                             |

### Conteúdos abordados

A atividade trabalha conceitos como:

- Filas de prioridade e Min-Heap
- Árvores Binárias de Busca (BST)
- Trie / Árvore de Prefixos
- Altura e balanceamento de árvores
- Splay Tree
- TreeSort
- Índice de Gini
- Entropia
- Manipulação e análise de dados com Pandas e NumPy

---

# Atividade Principal — 0 a 7 pontos

A segunda atividade é composta por **7 laboratórios**, nos quais as estruturas de dados são implementadas e analisadas de forma mais completa.

## Laboratórios

| Laboratório | Tema                                      | Dados                                          |
| ----------- | ----------------------------------------- | ---------------------------------------------- |
| 1           | Heap — Central de Chamados                | `chamados.csv`                                 |
| 2           | BST — Catálogo de Produtos                | `produtos.csv`                                 |
| 3           | Trie — Sistema de Autocomplete            | `palavras.csv`                                 |
| 4           | BST × AVL — Impacto do Balanceamento      | `dados_ordenados.csv` / `dados_aleatorios.csv` |
| 5           | Splay — Acessos Frequentes                | `acessos.csv`                                  |
| 6           | TreeSort — Ordenação de Vendas            | `vendas.csv`                                   |
| 7           | Árvore de Decisão — Saída de Funcionários | `funcionarios.csv`                             |

Cada laboratório deverá conter a implementação da estrutura proposta, execução do código, apresentação dos principais resultados e uma interpretação do comportamento observado.

---

# Organização do Repositório

A estrutura planejada para o projeto é:

```text
estrutura-de-dados-avancada/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── atividade-1-3-pontos/
│   ├── C1/
│   ├── C2/
│   ├── C3/
│   ├── C4/
│   ├── C5/
│   ├── C6/
│   ├── C7/
│   ├── C8/
│   ├── C9/
│   └── C10/
│
├── atividade-2-7-pontos/
│   ├── laboratorio-01/
│   ├── laboratorio-02/
│   ├── laboratorio-03/
│   ├── laboratorio-04/
│   ├── laboratorio-05/
│   ├── laboratorio-06/
│   └── laboratorio-07/
│
└── dados/
    ├── (dados para a atividade)
```
