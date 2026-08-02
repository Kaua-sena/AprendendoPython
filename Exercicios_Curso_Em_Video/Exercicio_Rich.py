from rich import print
from rich.panel import Panel

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def Apresentacao(self):
        return f":handshake: Meu nome é [blue]{self.nome}[/] trabalho no setor {self.setor} no cargo de {self.cargo}"
class Produto:
    def __init__(self, nome = str, preco = float):
        self.nome = nome
        self.preco = preco
        
    def Etiqueta(self):
       return Panel(f"{self.nome:^26}\n{"-" * 26}\n{self.preco:.^26}", title="[red]Produtos[/]", width=30)

