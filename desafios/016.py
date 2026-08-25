from rich import print

class Funcionario:
    empresa = "Curso em vídeo"
    def __init__(self, nome="", setor="", cargo=""):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresenteacao(self):
        return f":handshake: Olá, sou [cyan3]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa [red]{Funcionario.empresa}[/]"

c1 = Funcionario("Maria", "Adm", "Diretora")
c2 = Funcionario("Carlos", "Chão de fabrica", "Pião")
print(c1.apresenteacao())
print(c2.apresenteacao())
