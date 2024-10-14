import json
from ClasseAtor import Ator

def carregarAtores(atores:list, objetosAtores:list, listaFilmes:list):
    file_path = 'data_filmes.json'
    with open(file_path, 'r') as file:
        data = json.load(file)

    for filme in data:
        listaFilmes.append(filme)
        for ator in filme["Stars"]:
            if ator not in atores:
                atores.append(ator)
                objetosAtores.append(Ator(ator))


def preencherGeneros(atores:list, objetosAtores:list[Ator], listaFilmes:list):
    for filme in listaFilmes:
        for ator in filme["Stars"]:
            atorAtual = objetosAtores[atores.index(ator)]
            if filme["Movie Name"] not in atorAtual.filmes:
                atorAtual.filmes.append(filme["Movie Name"])
            for genero in filme["Genre"]:
                if genero not in atorAtual.generos:
                    atorAtual.generos.append(genero)


def conectarAtores(atores:list, objetosAtores:list[Ator], listaFilmes:list):
    for filme in listaFilmes:
        for ator in filme["Stars"]:
            atorAtual = objetosAtores[atores.index(ator)]
            outrosAtores = list(filme["Stars"])
            outrosAtores.remove(ator)
            for outroAtor in outrosAtores:
                if objetosAtores[atores.index(outroAtor)] not in atorAtual.conexoes:
                    atorAtual.conexoes.append(objetosAtores[atores.index(outroAtor)])

def gerarHeuristica(atores:list, objetosAtores:list[Ator], listaHeuristica:dict):
    for ator in objetosAtores:
        listaHeuristica[ator.nome] = 1/len(ator.filmes) + 1/len(ator.conexoes)
