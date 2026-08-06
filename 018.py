from rich.panel import Panel 
from rich import print

class Churrasco:
    consumo_Padrao = 0.400
    preco_Kg = 82.40
    def __init__(self, nome, quantidade=1):
        self.titulo=nome
        self.quantidade=quantidade


    def analisar(self):
        conteudo = f"Analisando o [green]{self.titulo}[/] com [cyan]{self.quantidade} convidados[/]." 
        conteudo += f"Cada participante comerá {Churrasco.consumo_Padrao} e cada Kg custa [red]{Churrasco.preco_Kg}[/]." 
        conteudo += f"Recomendo comprar [dark_orange3]{self.calcular_quantidade_carne()}g[/]." 
        conteudo += f"O custo total será de [dark_slate_gray2]R${self.calcular_custos_total():.2f}[/], saindo [dark_slate_gray2]R${self.calcular_custos_pessoal():.2f}[/] por pessoa."
        quadro=Panel(conteudo, title=self.titulo, width=60)
        return print(quadro)
        
        

    def calcular_quantidade_carne(self):
        return self.quantidade * Churrasco.consumo_Padrao

    def calcular_custos_total(self):
        return self.calcular_quantidade_carne()*Churrasco.preco_Kg

    def calcular_custos_pessoal(self):
        return self.calcular_custos_total()/self.quantidade


c1=Churrasco("Churras dos amigos", 15)
c1.analisar()

c2=Churrasco("Churrasco do fim de ano com amigos", 30)
c2.analisar()