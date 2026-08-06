from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Gamer:
    def __init__(self, nome="", nick = ""):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()
        print(f"Bem vindo(a), a Steam {self.nick}")

    def add_favoritos(self, nome):
        self.favoritos.append(nome)
        self.favoritos=sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome}[/]"
        conteudo += f"\nJogos Favoritos:"
        for num, game in enumerate(self.favoritos):
            conteudo+= f'\n:video_game:[blue]{game}[/]'
        quadro = Panel(conteudo,title=f"Jogador <{self.nick}>", width=40)
        return quadro

j1 = Gamer("Claudio", "Rokemal")
j1.add_favoritos("Fortnite")
j1.add_favoritos("Minecraft")
print(j1.ficha())