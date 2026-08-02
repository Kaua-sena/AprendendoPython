class ContaBancaria:
    def __init__(self, ID, titular, saldo = 0):
        self.id = ID
        self.nome = titular
        self.saldo = saldo
        
    def Depositar(self, valor): # Depositar saldo a conta.
        if valor > self.saldo:
            print("Deposito NEGADO saldo insuficiente.")
        else:
            self.saldo += valor
            
    def Sacar(self, valor): # Sacar saldo da conta.
        self.saldo -= valor
        print("Saque autorizado SEM EXITO.")
        
    def __str__(self):
        return f"O titular {self.nome} do ID {self.id} tem {self.saldo:,.2f} de saldo."
    
usuario1 = ContaBancaria(435, "Kaua William", 2000)
usuario1.Depositar(2000)
print(usuario1)