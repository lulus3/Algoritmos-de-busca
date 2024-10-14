import heapq
from ClasseAtor import Ator
from funcoes import *

class NoExploracao:
    def __init__(self, ator, pai=None):
        self.ator: Ator = ator
        self.pai: NoExploracao = pai  # reconstruir o caminho
        self.g = 0  # Custo do caminho até o nó atual
        self.h = 0  # Heurística
        self.f = 0  # Custo total (g + h)

    def __lt__(self, other):
        return self.f < other.f  # Para a fila de prioridade

def a_estrela(start: Ator, goal: Ator, heuristic:dict):
    listaAberta = []  # Nós a serem explorados
    listaFechada = set()  # Nós já explorados
    g_cost = {}  # Armazena o custo real mais baixo para cada ator

    noInicial = NoExploracao(start)
    noInicial.h = heuristic.get(start, float('inf'))
    noInicial.f = noInicial.g + noInicial.h

    heapq.heappush(listaAberta, noInicial)
    g_cost[start] = 0

    while listaAberta:
        noAtual:NoExploracao = heapq.heappop(listaAberta)  # Pega o nó com menor f

        if noAtual.ator == goal:
            return reconstruct_path(noAtual)

        listaFechada.add(noAtual.ator)

        for vizinho in noAtual.ator.conexoes:
            if vizinho in listaFechada:
                continue

            novo_custo_g = noAtual.g + 1

            # Se encontrarmos um caminho melhor, ou se o vizinho não foi visitado
            if vizinho not in g_cost or novo_custo_g < g_cost[vizinho]:
                g_cost[vizinho] = novo_custo_g  # Atualiza o melhor custo conhecido

                noVizinho = NoExploracao(vizinho, noAtual)
                noVizinho.g = novo_custo_g  # Atualiza o custo g do vizinho
                noVizinho.h = heuristic.get(vizinho, float('inf'))  # Calcula a heurística
                noVizinho.f = noVizinho.g + noVizinho.h

                heapq.heappush(listaAberta, noVizinho)  # Adiciona o vizinho à lista aberta

    return None

def reconstruct_path(no: NoExploracao):
    path = []
    while no is not None:
        path.append(no.ator.nome)
        no = no.pai
    return path[::-1]
