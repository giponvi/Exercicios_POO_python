from rich.panel import Panel
from rich import print
from rich.text import Text
from rich.traceback import install
install()

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        quadro = Panel(Text(f"{self.nome}          --------------------------.........R${self.preco:.2f}.........", justify="center"),title="Produto", width=30)
        return print(quadro)

p1 = Produto("borracha",2)
p2 = Produto("Lápis", 7)
p1.etiqueta()
p2.etiqueta()