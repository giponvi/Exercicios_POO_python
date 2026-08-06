from rich.panel import Panel
from rich import print
from rich.traceback import install
install()

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f'{self.nome.center(30, " ")}'
        conteudo+=f"{'='*30}"
        precof = f'R$ {self.preco:,.2f}'
        conteudo += f"{precof.center(30, ".")}"
        
        quadro = Panel(conteudo,title="Produto", width=34)
        return print(quadro)


p1 = Produto("borracha",2)
p2 = Produto("Lápis", 7)
p1.etiqueta()
p2.etiqueta()