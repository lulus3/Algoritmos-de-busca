from funcoes import *
from ClasseAtor import Ator
from algoritmo_a_estrela import *
import random, time
from busca_bidirecional import *

atores = []
objetosAtores = []
listaFilmes = []
heuristic = {}
print("carregando atores...")
carregarAtores(atores, objetosAtores, listaFilmes)
preencherGeneros(atores, objetosAtores, listaFilmes)
conectarAtores(atores, objetosAtores, listaFilmes)
gerarHeuristica(atores, objetosAtores, heuristic)

listaComparativaEstrela = []
listaComparativaBidirecional = []
tempoExecucaoEstrela = []
tempoExecucaoBidirecional = []

numeroExecucoes = int(input("numero de atores que deseja buscar: "))

for i in range(numeroExecucoes):
    ator = random.choice(atores)
    print(f"\n\n\nencontrando o caminho a partir de {ator}")
    atorInicial = objetosAtores[atores.index(ator)]
    atorAlvo = objetosAtores[atores.index("Kevin Bacon")]
    comeco = time.time()
    caminho = a_estrela(atorInicial, atorAlvo, heuristic)
    fim = time.time()

    print("BUSCA A*")
    if caminho:
        print(f"Caminho encontrado: {caminho}")
        print(f"tempo de execução: {(fim-comeco):.4f}")
        print(f"graus de separação: {len(caminho)-1}")
        listaComparativaEstrela.append(len(caminho)-1)
        tempoExecucaoEstrela.append(fim-comeco)
    else:
        print("Nenhum caminho encontrado.")

    # Realizar a busca bidirecional
    origem = ator
    destino = "Kevin Bacon"
    caminho, tempo_execucao, passos = busca_bidirecional(objetosAtores, origem, destino)

    print("\nBUSCA BIDIRECIONAL")
    if caminho:
        print(f"Caminho encontrado: {' -> '.join(caminho)}")
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Número de passos (graus de separação): {passos}")
        listaComparativaBidirecional.append(len(caminho)-1)
        tempoExecucaoBidirecional.append(tempo_execucao)
    else:
        print(f"Não foi possível encontrar uma conexão entre {origem} e {destino}.")

print("\n\nComparações de grau de separação:")
print("A*  :  Bidirecional")
for i in range(len(listaComparativaEstrela)):
    if listaComparativaEstrela[i] >= 10:
        print(f"{listaComparativaEstrela[i]}  :  {listaComparativaBidirecional[i]}")
    else:
        print(f" {listaComparativaEstrela[i]}  :  {listaComparativaBidirecional[i]}")
mediaEstrela = sum(tempoExecucaoEstrela) / len(tempoExecucaoEstrela)
mediaBidirecional = sum(tempoExecucaoBidirecional) / len(tempoExecucaoBidirecional)
print(f"\na media dos tempos foram: \nA* = {mediaEstrela} \nBidirecional = {mediaBidirecional}")

