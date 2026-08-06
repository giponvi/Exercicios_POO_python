from rich.panel import Panel 
from rich import print

class Churrasco:
    def __init__(self, nome, quantidade=1):
        self.titulo=nome
        self.quantidade=quantidade

    def analisar(self):
        carne = self.quantidade*400
        carneKg = carne/1000
        custoTotal=(carne/1000)*82.40
        custoPessoa=custoTotal/self.quantidade
        quadro=Panel(f"Analisando o [green]{self.titulo}[/] com [cyan]{self.quantidade} convidados[/]. Cada participante comerá 0.4Kg e cada Kg custo [red]R$82,40[/]. Recomendo comprar [dark_orange3]{carne}g[/], isto é, [dark_orange3]{carneKg}Kg[/]. O custo total será de [dark_slate_gray2]R${custoTotal:.2f}[/], saindo [dark_slate_gray2]R${custoPessoa:.2f}[/] por pessoa.", title=self.titulo, width=60)
        return print(quadro)

c1=Churrasco("Churras dos amigos", 15)
c1.analisar()