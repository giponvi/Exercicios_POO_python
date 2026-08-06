from rich import print

class Funcionario:
    def __init__(self, nome="", setor="", cargo=""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = "Curso em vídeo"

    def apresenteacao(self):
        return f":handshake: Olá, sou [cyan3]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa [red]{self.empresa}[/]"

c1 = Funcionario("Maria", "Adm", "Diretora")
c2 = Funcionario("Carlos", "Chão de fabrica", "Pião")
print(c1.apresenteacao())
print(c2.apresenteacao())