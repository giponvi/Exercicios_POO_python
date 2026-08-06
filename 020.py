from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome="", nick = "", favoritos=[]):
        self.nome = nome
        self.nick = nick
        self.favoritos = favoritos
        print(f"Bem vindo(a), a Steam {self.nick}")

    def add_favoritos(self, nome):
        self.favoritos.append(nome)

    def ficha(self):
        quadro = Panel(f"Nome real: {self.nome}                                                        Jogos Favoritos:{self.favoritos}",title=f"Jogador <{self.nick}>", width=50)
        return quadro

j1 = Gamer("Claudio", "Rokemal")
j1.add_favoritos("Fortnite")
j1.add_favoritos("Minecraft")
print(j1.ficha())