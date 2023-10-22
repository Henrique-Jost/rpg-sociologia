from .personagem import Personagem

class Jogador(Personagem):
    def __init__(self, nome, vida, ataque, defesa, inventario):
        super().__init__(nome, vida, ataque, defesa)
        self.inventario = inventario

    def mostrarInventario(self):
        return ", ".join(self.inventario)

    def __str__(self):
        return f"{super().__str__()} - Inventário: {self.mostrarInventario()}"
