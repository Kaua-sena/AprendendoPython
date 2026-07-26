class Usuario:
    def __init__(self): # Método Contrutor
        # Atributos de Intância
        
        self.nome = ""
        self.idade = 0
        self.tickets = 0
        
        # Métodos de Intância
    def Entrada(self):
        self.tickets = self.tickets + 1
    def Saida(self):
        return f"O usuario {self.nome} tem {self.idade} anos e {self.tickets} entrada."

# Declaração do Objeto    
usuario1 = Usuario()
usuario1.nome = "Kaua William"
usuario1.idade = 18
usuario1.Entrada()
print(usuario1.Saida())

