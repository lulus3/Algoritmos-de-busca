import time
from collections import deque
from ClasseAtor import Ator

def busca_bidirecional(atores: list[Ator], nome_origem: str, nome_destino: str) -> tuple[list[str], float, int]:
    if nome_origem == nome_destino:
        return ([nome_origem], 0.0, 0)

    # Encontrar os objetos Ator para os nomes de origem e destino
    ator_origem = next((a for a in atores if a.nome == nome_origem), None)
    ator_destino = next((a for a in atores if a.nome == nome_destino), None)

    if not ator_origem or not ator_destino:
        return ([], 0.0, 0)

    # Inicializar fronteiras da busca
    fronteira_origem = deque([ator_origem])
    fronteira_destino = deque([ator_destino])

    # Listas para rastrear o caminho e os visitados
    visitados_origem = [ator_origem]
    visitados_destino = [ator_destino]
    caminho_origem = [None] * len(atores)
    caminho_destino = [None] * len(atores)

    inicio_tempo = time.time()

    # Realizar a busca simultaneamente a partir das duas fronteiras
    while fronteira_origem and fronteira_destino:
        # Expandir a fronteira da origem
        if expandir_fronteira(fronteira_origem, visitados_origem, visitados_destino, caminho_origem, atores):
            fim_tempo = time.time()
            caminho = reconstruir_caminho(caminho_origem, caminho_destino, visitados_origem, visitados_destino, atores)
            tempo_execucao = fim_tempo - inicio_tempo
            return (caminho, tempo_execucao, len(caminho) - 1)

        # Expandir a fronteira do destino
        if expandir_fronteira(fronteira_destino, visitados_destino, visitados_origem, caminho_destino, atores):
            fim_tempo = time.time()
            caminho = reconstruir_caminho(caminho_origem, caminho_destino, visitados_origem, visitados_destino, atores)
            tempo_execucao = fim_tempo - inicio_tempo
            return (caminho, tempo_execucao, len(caminho) - 1)

    fim_tempo = time.time()
    return ([], fim_tempo - inicio_tempo, 0)

def expandir_fronteira(fronteira: deque, visitados: list, opostos: list, caminhos: list, atores: list[Ator]) -> bool:
    # Pegar o próximo ator para expandir
    ator_atual = fronteira.popleft()

    # Expandir para cada ator conectado
    for vizinho in ator_atual.conexoes:
        if vizinho in visitados:
            continue

        # Marcar o vizinho como visitado e adicionar à fronteira
        visitados.append(vizinho)
        fronteira.append(vizinho)

        # Registrar o caminho do vizinho
        caminhos[atores.index(vizinho)] = ator_atual

        # Verificar se encontramos a fronteira oposta
        if vizinho in opostos:
            return True

    return False

def reconstruir_caminho(caminho_origem: list, caminho_destino: list, visitados_origem: list, visitados_destino: list, atores: list[Ator]) -> list[str]:
    # Encontrar o ponto de encontro
    ponto_encontro = next((a for a in visitados_origem if a in visitados_destino), None)
    if not ponto_encontro:
        return []

    # Reconstruir o caminho do início ao ponto de encontro
    caminho = []
    atual = ponto_encontro
    while atual is not None:
        caminho.append(atual.nome)
        atual = caminho_origem[atores.index(atual)]
    caminho.reverse()

    # Continuar do ponto de encontro até o final
    atual = caminho_destino[atores.index(ponto_encontro)]
    while atual is not None:
        caminho.append(atual.nome)
        atual = caminho_destino[atores.index(atual)]

    return caminho