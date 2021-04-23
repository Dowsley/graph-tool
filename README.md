# Documentação

# Sumário
1. Introdução a Grafos
    -   Grafo Direcionado
    -   Grafo Ponderado
    -   Tamanho
    -   Ordem
    -   Adjacência
    -   Grau
2. Tecnologias
3. Passo a Passo
4. Banco de Horas

# Introdução a Grafos
***
Grafo é um par de conjuntos: `vértices`, `arestas`, onde cada `aresta` é um par ordenado de `vértices`.
***

## Grafo Direcionado
Um grafo é direcionado quando suas `arestas` podem ser chamadas de `vetores` ou `setas`, pois possuem direção, um `vértice` de origem e um `vértice` de entrada.

## Grafo Ponderado
Um grafo é ponderado quando suas arestas possuem pesos.

## Tamanho
Número de arestas do Grafo.

## Ordem
Número de vértices do Grafo

## Adjacência

>### Adjacência(Não Direcionado)
> É a relação entre vértices que compartilham uma mesma `aresta`. 

>### Adjacência(Direcionado)
> Dado um vértice `v`, A relação de Adjacência em Grafos Direcionados mostra a lista de vértices adjacentes de entrada e a lista de vértices adjacentes de saída.

## Grau
>### Grau do Vértice(Não Direcionado)
> O grau de um vértice é o número de arestas incidentes para com o vértice

>### Grau do Vértice(Direcionado)
>A seqüência de graus de um gráfico direcionado é a lista de seus pares `indegree` e `outdegree`.
> - Indegree of vertex V is the number of edges which are coming into the vertex V.
> - Outdegree of vertex V is the number of edges which are going out from the vertex V.

# Tecnologias

## Backend
- Criamos uma classe `Graph` com os seguintes **atributos**:
    - `directed` - Booleano que recebe `True` se o Grafo for Direcionado, e `False` se o Grafo for Não-Direcionado
    - `weighted` - Booleano que recebe `True` se o Grafo for Ponderado, e `False` se o Grafo for Não-Ponderado
    - `graph` - Dicionário python onde será alocado os vertices e as arestas.
- E os seguintes **métodos**:
    - `add_edge` - Adiciona uma aresta com base nos vértices de origem e destino.
    - `print_graph` - Printa um Grafo de uma Maneira Simplificada.
    - `get_order` - Calcula a ordem do Grafo.
    - `get_size` -  Calcula o tamanho do Grafo.
    - `adjacency` - Verifica se dois vértices são adjacentes ou não.
    - `get_degree` - Calcula o grau de um dado vértice.
    - `get_adjacents` - Retorna os vértices adjacentes de um determinado vértice.

## Frontend

Escolhendo se é Ponderado
- [ ] True
- [x] False

Escolhendo se é Direcionado
- [ ] True
- [x] False

# Passo a Passo

# Banco de Horas

|Atividade| Horas Usadas|
|:--|--:|
|Planejamento geral do projeto| 01:00|
|Planejamento da representação do grafo| 00:30|
|Criação da Classe e dos métodos iniciais| 01:00|
|Criação do método que verifica edges existentes| 00:10|
|Implementação do tratamento de grafos direcionados| 00:16|
|Implementação do tratamento de grafos ponderados| 00:15|
|Criação do método que retonra o tamanho do Grafo| 00:45|
|Criação do método que retonra a ordem do Grafo| 00:25|
|Criação do método que verifica adjacencia de 2 vértices| 00:27|
|Criação do método que verifica o grau de um dado vértice| 00:27|
|Criação do método que retonra a lista de vertices adjacentes| 00:15|
|Backend utilizando Flask| 03:00|
|Frontend utilizando ReactJS| 20:30 - agora|

Total: 8 horas e 27 minutos
