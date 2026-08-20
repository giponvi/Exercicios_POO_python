import os
import subprocess
from rich.panel import Panel
from rich import print

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 19

    def __init__(self, canal=1, volume=2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def passar(self):
        if self.ligado:
            if self.canal_atual==ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def voltar(self):
        if self.ligado:
            if self.canal_atual== ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual-=1

    def aumentar(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual +=1

    def diminuir(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual-=1


    def mostrar_tv(self):
        conteudo=''
        if not self.ligado:
            conteudo = f":prohibited:[red] A TV esta desligada[/]"
        else:
            conteudo = f"CANAL  ="
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max+1):
                if canal != self.canal_atual:
                    conteudo+= f" {canal} "
                else:
                    conteudo+= f' [yellow on yellow] {canal} [/]  '

            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max+1):
                if volume <= self.volume_atual:
                    conteudo+= f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"
        tv = Panel(conteudo, title= "[ TV ]", width=40)
        print(tv)

t1=ControleRemoto()
while True:
    t1.mostrar_tv()
    comando=str(input(f"[< CH >  - VOL +]    "))
    match comando:
        case "@":
            t1.liga_desliga()
        case "<":
            t1.voltar()
        case ">":
            t1.passar()
        case "-":
            t1.diminuir()
        case "+":
            t1.aumentar()
        case "0":
            break
    subprocess.run('cls' if os.name == 'nt' else 'clear')
 #   os.system('cls' if os.name == 'nt' else 'clear') 