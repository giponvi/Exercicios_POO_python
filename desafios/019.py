from rich import print

class Livro:
    def __init__(self, titulo, quantidade=1):
        self.titulo = titulo
        self.quantidade = quantidade
        self.pagAtual = 1
        print(f":book: [cyan]Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem {self.quantidade} páginas no total. Você agora esta na [green]página 01[/][/]")

    def avancarPag(self, quantidadePags):
        pags_restantes = self.quantidade - self.pagAtual
        if quantidadePags > pags_restantes:
            return f"O livro tem {self.quantidade} páginas. Você só pode avançar mais {pags_restantes} página(s). Você continua na página {self.pagAtual}."

        for _ in range(quantidadePags):
            self.pagAtual += 1
            print(f"{self.pagAtual} ->", end=" ")
        print() 
        
        if self.pagAtual == self.quantidade:
            return f"[bold green]Parabéns! Você avançou {quantidadePags} página(s) e CHEGOU AO FIM do livro '{self.titulo}'![/]"
        
        return f"Você avançou {quantidadePags} página(s) e agora está na página {self.pagAtual}."
    
    def voltarPag(self, quantidadePags):
        if quantidadePags > self.pagAtual-1:
                    return f'Você está na página {self.pagAtual} ainda, não pode voltar mais que {self.pagAtual} Paginas'
        else:
            for p in range(quantidadePags):
                self.pagAtual-=1
                print(self.pagAtual, " ->", end=" ")
            return f"Você voltou {quantidadePags} e agora esta na página {self.pagAtual}"

# --- Testando a classe ---
l1 = Livro("Bíblia", 476)

# Tentativa inválida (ultrapassa o limite)
print(l1.avancarPag(1000))

# Avançando com sucesso
print(l1.avancarPag(10))

print(l1.voltarPag(5))

# Chegando até o final do livro
print(l1.avancarPag(470))