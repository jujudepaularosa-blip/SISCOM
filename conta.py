class Conta:
    def __init__ (self, nome_titular):
        self.nome_titular = nome_titular
        self.poupanca = 0

    def depositar(self, valor):
        
        self.poupanca += valor
        
    def poupanca(self):
        return self._poupanca
    
conta1= Conta("Juliana")

print(conta1.nome_titular )
print(conta1.poupanca)