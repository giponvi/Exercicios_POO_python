from rich import print
from rich.traceback import install
install()

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampado = True

    def destampar(self):
        if self.tampado:
            self.tampado=False

    def escrever(self, conteudo):
        if self.tampado:
            print('Não pode escrever, destampe a caneta!')
        else:
            print(f"[{self.cor}]{conteudo}[/]")

    def quebrar_linhas(self, quantidade):
        for i in range(quantidade):
            print()

c1=Caneta("red")
c2=Caneta("Blue")
c3=Caneta("Green")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("HAHA")
c1.quebrar_linhas(1)
c2.escrever("HAHA")
c2.quebrar_linhas(2)
c3.escrever("HAHA")