class Ator:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.generos:list = []
        self.filmes:list =[]
        self.conexoes:list[Ator] = []

    def __str__(self):
        return f"Ator(Name: {self.nome}, generos: {self.generos}, conexoes: {self.conexoes})"